from enum import Enum

from pydantic import BaseModel, Field, validator


class Modality(str, Enum):
    face = "face"
    iris = "iris"
    fingerprint = "fingerprint"
    speech = "speech"
