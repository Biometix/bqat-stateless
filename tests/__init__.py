from fastapi import FastAPI

from api.routes.scan import router as scan

api = FastAPI()
api.include_router(scan)
