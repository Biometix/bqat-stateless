from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, validator
from uuid import uuid4


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
    type: FileType
    data: str
    id: str = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
