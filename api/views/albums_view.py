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


album_view = APIRouter()



@album_view.post("/albums/")
async def add_album(
    payload: schema.AlbumBase
):
    _album = await crud.get_album_detail(name=payload.name, artist=payload.artist)
    if _album:
        raise HTTPException(status_code=400, detail="album already exists!")
    return await crud.add_album(payload)

@album_view.get("/albums/{name}", response_model=schema.AlbumBase)
async def get_album(name: str):
    album = await crud.get_album(name=name)
    if album is None:
        raise HTTPException(status_code=404, detail=f"No album found with name {name}!")
    return album


@album_view.get("/albums/", response_model=List[schema.AlbumBase])
async def get_albums(skip: int = 0, limit: int = 10):
    album_list = await crud.get_albums(skip=skip, limit=limit)
    if album_list is None:
        raise HTTPException(status_code=404, detail="No album at this time!")
    return album_list

@album_view.get("/album/{id}", response_model=schema.AlbumBase)
async def get_album_by_id(id: int):
    album = await crud.get_album_by_id(id=id)
    if album is None:
        raise HTTPException(status_code=404, detail=f"No album found with id {id}!")
    return album