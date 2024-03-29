import shutil
from base64 import standard_b64decode, urlsafe_b64decode
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse

from api.config.models import Modality, Task
from bqat.bqat_core import __version__, scan

router = APIRouter()


@router.post("/file", summary="Post biometric file for assessment")
async def scan_file(
    modality: Modality,
    file: UploadFile,
):
    """
    Upload a biometric file for quality assessment:

    - **file**: biometric file
    - **modality**: specify modality of the biometric
    """
    temp = Path("temp")
    if not temp.exists():
        temp.mkdir(parents=True)
    temp_file = Path("temp") / f"{str(uuid4())}.{file.filename.split('.')[1]}"
    data = await file.read()
    with open(temp_file, "wb") as out:
        out.write(data)

    options = {"type": "file"}
    if modality == "face":
        options.update({"engine": "biqt"})

    try:
        result = {
            "results": scan(
                file=str(temp_file),
                mode=modality,
                **options,
            ),
            "engine": f"BQAT-core {__version__}",
        }
        result["results"].update({"file": file.filename})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"scan failed, please request params: {str(e)}",
        )
    finally:
        # shutil.rmtree(str(temp))
        pass
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@router.post("/base64", summary="Post biometric file (base64) for assessment")
async def scan_file(
    urlsafe: bool = True,
    task: Task = Body(...),
):
    """
    Upload a biometric file (base64) for quality assessment:

    - **urlsafe**: (bool) urlsafe encoded or not.
    - **modality**: specify modality of the biometric.
    - **type**: biometric file type (png, jpg, wav, jp2, etc.).
    - **data**: biometric file encoded as base64 string.
    - **id**: biometric file identifier.
    - **timestamp**: ISO 8601 date and time format.
    """
    temp = Path("temp")
    if not temp.exists():
        temp.mkdir(parents=True)
    try:
        data = (
            urlsafe_b64decode(task.data) if urlsafe else standard_b64decode(task.data)
        )
    except Exception as e:
        print(f"retry: {str(e)}")
        try:
            data = (
                urlsafe_b64decode(task.data + "=" * (4 - len(task.data) % 4))
                if urlsafe
                else standard_b64decode(task.data + "=" * (4 - len(task.data) % 4))
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"failed to decode base64 data: {str(e)}",
            )
    temp_file = Path("temp") / f"{str(uuid4())}.{task.type}"
    with open(temp_file, "wb") as out:
        out.write(data)

    options = {"type": "file"}
    if task.modality == "face":
        options.update({"engine": "biqt"})

    try:
        result = {
            "results": scan(
                file=str(temp_file),
                mode=task.modality,
                **options,
            ),
            "engine": f"BQAT-core {__version__}",
        }
        result["results"].update({"file": f"{str(task.id)}.{task.type}"})
        result.update(
            {
                "modality": task.modality,
                "id": str(task.id),
                "timestamp": str(task.timestamp),
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"scan failed, please request params: {str(e)}",
        )
    finally:
        # shutil.rmtree(str(temp))
        pass
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)
