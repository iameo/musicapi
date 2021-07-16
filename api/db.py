import os

from sqlalchemy import sql
import sqlalchemy
from databases import Database

import ormar

from datetime import datetime

from typing import Optional, List

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


DATABASE_URI = os.getenv('SQLAlCHEMY_DATABASE_URL', f'sqlite:///vegd1gr.db')

database = Database(DATABASE_URI)
metadata = sqlalchemy.MetaData()

current_year = int(datetime.now().year)


class Artist(ormar.Model):
    class Meta:
        tablename = "artists"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, nullable=False, index=True)
    record_label: str = ormar.String(max_length=100, nullable=False, index=True, default='Not signed to any label!')





engine = sqlalchemy.create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}
)

# metadata.drop_all(engine)
# metadata.create_all(engine)