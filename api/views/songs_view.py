import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

import re
import requests

from .. import schema


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
 