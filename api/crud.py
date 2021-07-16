# from sqlalchemy.orm import Session, session

from api import schema

from api.db import Song, Album, Artist



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


# async def get_song_detail(artist, title):
#     query = Song.objects().where(Song.c.artist==artist).where(song.c.title==title)
#     return await database.fetch_one(query=query)

# async def delete_song(id: int):
#     query = Song.delete().where(Song.c.id==id)
#     return await database.execute(query=query)

# async def update_song(id: int, payload: schema.MusicCreate): #I can't think of a possible usecase for now
#     query = (
#         Song
#         .update()
#         .where(Song.c.id == id)
#         .values(**payload.dict())
#     )
#     return await database.execute(query=query)


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

async def get_album_detail(name, artist):
    album = Album.objects.filter(name=name, artist=artist)
    return await album


################ ARTIST #########################

async def add_artist(payload: schema.ArtistBase):
    artist = Artist.objects.create(**payload.dict())
    return await artist

async def get_artist():
    artist = Artist.objects.all()
    return await artist
