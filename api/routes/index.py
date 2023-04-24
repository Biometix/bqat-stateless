import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import (
    APIRouter,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.responses import JSONResponse

from bqat.bqat_core import __name__, __version__, scan
from api.config.models import Modality

router = APIRouter()


@router.post("/", summary="Post biometric file for scan")
async def scan_file(
    file: UploadFile,
    modality: Modality,
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

    try:
        result = {
            "results": scan(file=str(temp_file), **{"mode": modality, "type": "file"}),
            "engine": f"BQAT-core {__version__}",
        }
        result["results"].update({"file": file.filename})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"scan failed, please request params: {str(e)}",
        )
    finally:
        shutil.rmtree(str(temp))
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)
