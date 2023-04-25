import uvicorn
from fastapi import FastAPI

from api.config import Settings
from api.routes.index import router as index
from bqat.bqat_core import __version__ as ver

description = """
BQAT-Stateless API provide you with biometric quality assessment capability as stateless service. 🚀

## File

You can **submit biometric file as is** for assessment.

## Base64

You can **submit biometric file as Base64 encoded string** for assessment.

"""

app = FastAPI(
    title="BQAT-Stateless",
    description=description,
    version=ver,
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
settings = Settings()


app.include_router(index)


def create_app():
    uvicorn.run(
        "api.app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )
