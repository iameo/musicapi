# from sqlalchemy.orm import Session, session

from api import schema

from api.db import song, Album, database



###########################MUSIC#####################################

async def add_song(payload: schema.MusicCreate):
    query = song.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_song(title):
    query = song.select(song.c.title==title)
    return await database.fetch_one(query=query)

async def get_song_detail(artist, title):
    query = song.select().where(song.c.artist==artist).where(song.c.title==title)
    return await database.fetch_one(query=query)

async def get_songs(skip: int = 0, limit: int = 10):
    query = song.select().order_by(song.c.id.desc()).offset(skip).limit(limit)
    return await database.fetch_all(query=query)

async def delete_song(id: int):
    query = song.delete().where(song.c.id==id)
    return await database.execute(query=query)

async def update_song(id: int, payload: schema.MusicCreate): #I can't think of a possible usecase for now
    query = (
        song
        .update()
        .where(song.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
