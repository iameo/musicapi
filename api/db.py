import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, sql, ListColumn, Image, File, ForeignKey)
import sqlalchemy
from databases import Database
from datetime import datetime

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DATABASE_URI = os.getenv('SQLAlCHEMY_DATABASE_URL')

metadata = sqlalchemy.MetaData()


song = Table(
    'song',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('title', String(100), index=True),
    Column('artist', String(100)),
    Column('cover_image', Image()),
    Column('audio_file', File()),
    Column('uploaded_at', DateTime(timezone=True), server_default=sql.func.now())
)


album = Table(
    'album',
    metadata,
    Column('album_id', Integer, ForeignKey('song.id'), primary_key=True, index=True),
    Column('title', String(100), index=True),
    Column('cover_image', String(100)),
    Column('tracks', ListColumn()),
    Column('production_year', DateTime(timezone=True), server_default=sql.func.now())
)

engine = sqlalchemy.create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}
)

database = Database(DATABASE_URI)