# from sqlalchemy.orm import Session, session

from api import schema

from api.db import Song, Album



###########################SONG#####################################

async def add_song(payload: schema.MusicCreate):
    song = Song.objects.create(**payload.dict())
    return await song

async def get_song(title):
    song = Song.objects.get(title=title)
    return await song

async def get_songs_by_title(title: str):
    song = Song.objects.all(title=title)
    return await song

async def get_songs(skip: int = 0, limit: int = 10):
    songs = Song.objects.order_by(Song.id.desc()).offset(skip).limit(limit).all()
    return await songs



# ######################## ALBUM ################################


async def add_album(payload: schema.AlbumCreate):
    album = Album.objects.create(**payload.dict())
    return await album

async def get_album(name):
    album = Album.objects.get(name=name)
    return await album

async def get_albums_by_name(name: str):
    album = Album.objects.all(name=name)
    return await album

async def get_albums(skip: int = 0, limit: int = 10):
    albums = Album.objects.order_by(Album.id.desc()).offset(skip).limit(limit).all()
    return await albums