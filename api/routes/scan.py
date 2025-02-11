import tempfile
from base64 import standard_b64decode, urlsafe_b64decode
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse

from api.config.models import Engine, Modality, Task
from bqat.bqat_core import __version__, scan

router = APIRouter()


@router.post("/file", summary="Post biometric file for assessment")
async def scan_file_raw(
    modality: Modality,
    file: UploadFile,
    engine: Engine = Engine.bqat,
):
    """
    Upload a biometric file for quality assessment:

    - **file**: biometric file
    - **modality**: specify modality of the biometric
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = Path(tmpdir) / f"{str(uuid4())}.{file.filename.split('.')[1]}"
        data = await file.read()
        with open(temp_file, "wb") as out:
            out.write(data)

        options = {"type": "file"}
        if modality == "face":
            options.update({"engine": engine})
        else:
            engine = "default"

        try:
            result = {
                "results": scan(
                    input=str(temp_file),
                    mode=modality,
                    **options,
                ),
                "engine": engine,
                "version": f"BQAT-core {__version__}",
            }
            result["results"].update({"file": file.filename})
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"scan failed: {str(e)}",
            )
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@router.post("/base64", summary="Post biometric file (base64) for assessment")
async def scan_file_base64(
    urlsafe: bool = True,
    task: Task = Body(...),
):
    """
    ### Upload a biometric file (in _base64_ string) for quality assessment:

    #### Query Parameters:
    - **urlsafe**: (bool) urlsafe encoded or not.

    #### Body Parameters (JSON):
    ``` json
    {
        "modality": "face",
        "engine": "ofiq",
        "type": "jpg",
        "data": "<base64 string>",
        "id": "123e4567-e89b-12d3-a456-426655440000",
    }
    ```
    - **modality**: specify modality of the biometric.
    - **engine**: specify processing engine for the biometric sample.
    - **type**: biometric file type (png, jpg, wav, jp2, etc.).
    - **data**: biometric file encoded as base64 string.
    - **id**: biometric file identifier.
    - **timestamp**: ISO 8601 date and time format.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            data = (
                urlsafe_b64decode(task.data)
                if urlsafe
                else standard_b64decode(task.data)
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
        temp_file = Path(tmpdir) / f"{str(uuid4())}.{task.type}"
        with open(temp_file, "wb") as out:
            out.write(data)

        options = {"type": "file"}
        if task.modality == "face":
            options.update({"engine": task.engine})
        else:
            task.engine = "default"

        try:
            result = {
                "results": scan(
                    input=str(temp_file),
                    mode=task.modality,
                    **options,
                ),
                "engine": task.engine,
                "version": f"BQAT-core {__version__}",
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
                detail=f"scan failed: {str(e)}",
            )
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)
