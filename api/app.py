import uvicorn

from fastapi import FastAPI


from api.config import Settings
from api.routes.index import router as index

app = FastAPI()
settings = Settings()


app.include_router(index)


def create_app():
    uvicorn.run(
        "api.app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )
