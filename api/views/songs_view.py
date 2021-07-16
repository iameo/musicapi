import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

import re
import requests

from .. import schema, crud
from ..db import Song

from typing import List
from fastapi import APIRouter, Path
import json

import ormar

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


music_view = APIRouter()

@music_view.put("/songs/{song_id}")
async def update_song(song_id: int, song: schema.MusicBase):
    results = {"song_id": song_id, "song": song}
    return results
 

@music_view.post("/songs/")
async def add_song(
    payload: schema.MusicCreate
):
    return await crud.add_song(payload) 



@music_view.get("/songs/")
async def get_songs(skip: int = 0, limit: int = 10):
    song_list = await crud.get_songs(skip=skip, limit=limit)
    if song_list is None:
        raise HTTPException(status_code=404, detail="No song at this time!")
    return song_list


@music_view.get("/songs/{title}", response_model=List[schema.MusicDetail])
async def get_songs_by_title(title: str):
    try:
        song_list = await crud.get_song(title)
    except ormar.NoMatch:
        raise HTTPException(status_code=404, detail=f"No song with title {title} at this time!")
    return song_list