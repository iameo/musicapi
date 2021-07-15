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
