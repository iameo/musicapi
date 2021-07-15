import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

import re
import requests

from .. import schema, crud


from typing import List
from fastapi import APIRouter, Path
import json

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
    payload: schema.MusicBase
):
    _song = await crud.get_song_detail(artist=payload.artist, title=payload.title)
    if _song:
        raise HTTPException(status_code=400, detail="song already exists!")
    return await crud.add_song(payload)

