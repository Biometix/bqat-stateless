import os

import uvicorn
from fastapi import FastAPI

from api.config import Settings
from api.routes.scan import router as scan
from bqat.bqat_core import __version__ as ver

description = """
BQAT-Stateless API provide you with biometric quality assessment capability as stateless service. 🚀

## File

Submit biometric file for assessment.

## Base64

Submit biometric file as **base64 encoded string** for assessment.

"""

threads = os.cpu_count()

app = FastAPI(
    title="BQAT-Stateless",
    description=description,
    version=ver,
    contact={
        "url": "https://biometix.com/",
        "email": "support@biometix.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
settings = Settings()


app.include_router(scan, tags=["/"])


def create_app():
    uvicorn.run(
        "api.app:app",
        host=settings.HOST,
        workers=threads - 2 if threads > 3 else 1,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )
