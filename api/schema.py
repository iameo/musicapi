from typing import List, Optional
from pydantic import BaseModel, Field

from datetime import datetime

from api.db import Song, Album


current_year = int(datetime.now().year)


class MusicBase(BaseModel):
    title: Optional[str] = None
    artist: Optional[int] = 1
    audio_file: Optional[bytes] = None



class MusicDetail(MusicBase):
    cover_image: Optional[bytes] = None
    # album_id: Optional[int] = None
    # audio_length: Optional[str] = '00:00'


class MusicCreate(MusicDetail):
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
                "cover_image": "fret-not-cover-image.jpg",
                "audio_length": "3:23",
                "uploaded_at": "2021-04-23T02:16:45"
            }
        }


class MusicOut(MusicDetail):
    uploaded_at: datetime

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


##################### ALBUM ########################################

class AlbumBase(BaseModel):
    name: Optional[str] = 'AlbumName'
    artist: Optional[int] = 1
    cover_image: Optional[bytes] = None
    tracks: Optional[List[Song]] = [None]
    production_year: Optional[int] = current_year


class AlbumCreate(AlbumBase):
    pass



######################## ARTIST ###############################

class ArtistBase(BaseModel):
    name: Optional[str] = 'ArtistName'
    record_label: Optional[str] = 'ArtistRecordLabel'


# class ArtistOut(BaseModel):
#     pass





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