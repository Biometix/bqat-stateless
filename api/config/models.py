from datetime import datetime
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class Engine(str, Enum):
    bqat = "bqat"
    ofiq = "ofiq"
    biqt = "biqt"


class Modality(str, Enum):
    face = "face"
    iris = "iris"
    fingerprint = "fingerprint"
    speech = "speech"


class FileType(str, Enum):
    jpg = "jpg"
    jpeg = "jpeg"
    png = "png"
    bmp = "bmp"
    wsq = "wsq"
    jp2 = "jp2"
    wav = "wav"


class Task(BaseModel):
    modality: Modality
    engine: Engine | None = Engine.bqat
    type: FileType
    data: str
    id: str = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "modality": "face",
                "engine": "ofiq",
                "type": "jpg",
                "data": "<base64>",
                "id": "123e4567-e89b-12d3-a456-426655440000",
            }
        }
    )
