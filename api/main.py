from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware

from api.views.songs_view import music_view

from api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(
    title="MUSIC API",
    description="API for uploading songs!",
    version="alpha")



origins = [
    "http://127.0.0.1:5000",
    "http://127.0.0.1:8080",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Redirect to docs
@app.get("/", tags=['Docs'])
def docs():
    return RedirectResponse('/docs')

app.include_router(music_view,prefix="/api/v1/resources",tags=["Songs"])
