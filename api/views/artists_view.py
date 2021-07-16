import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

import re
import requests

from .. import schema, crud
from ..db import Artist


from typing import List
from fastapi import APIRouter, Path
import json

import ormar

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


artist_view = APIRouter()

@artist_view.put("/artists/{artist_id}")
async def update_artist(artist_id: int, artist: schema.ArtistBase):
    results = {"artist_id": artist_id, "artist": artist}
    return results
 

@artist_view.post("/artists/", response_model=schema.ArtistBase)
async def add_artist(
    payload: schema.ArtistBase
):
    return await crud.add_artist(payload) 




# @artist_view.get("/artists/", response_model=List[schema.MusicDetail])
# async def get_artists(skip: int = 0, limit: int = 10):
#     artist_list = await crud.get_artists(skip=skip, limit=limit)
#     if artist_list is None:
#         raise HTTPException(status_code=404, detail="No artist at this time!")
#     return artist_list


@artist_view.get("/artists/{title}")
async def get_artists_by_title(title: str):
    try:
        artist_list = await crud.get_artist(title)
    except ormar.NoMatch:
        raise HTTPException(status_code=404, detail=f"No artist with title {title} at this time!")
    return artist_list


@artist_view.get("/artists/")
async def get_artists():
    try:
        artist_list = await crud.get_artist()
    except ormar.NoMatch:
        raise HTTPException(status_code=404, detail=f"No artists at this time!")
    return artist_list