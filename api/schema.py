from typing import List, Optional
from pydantic import BaseModel, Field

from datetime import datetime



class MusicBase(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    audio_file: Optional[str] = None


class MusicDetail(MusicBase):
    cover_image: str
    album: str
    audio_length: str


class MusicCreate(MusicBase):
    pass

class MusicSchema():
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id":3,
                "title": "Fret Not",
                "artist": "Mr Alchemy",
                "audio_file": "fret_not.mp3",
                "cover_image": "fret-not.jpg",
                "audio_length": "3:23",
                "uploaded_at": "2021-04-23T02:16:45"
            }
        }


class MusicOut(MusicDetail):
    created_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "Fret Not",
                "artist": "Mr Alchemy",
                "audio_file": "fret_not.mp3",
                "cover_image": "fret-not.jpg",
                "audio_length": "3:23",
                "uploaded_at": "2021-04-23T02:16:45"
            }
        }





##################### RESPONSE #####################################

def ResponseModel(data, status, code):
    return {
        "data": data,
        "status": status,
        "code": code
    }


def ErrorResponseModel(error, message, code):
    return {
        "error": error,
        "message": message,
        "code": code
    }