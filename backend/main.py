from functools import reduce
from typing import Union
from models.Album import Album
from models.Song import Song
from models.Artist import Artist
from db.database import Database
from services.db_utils import generate_query_columns_value

from fastapi import FastAPI


app = FastAPI()
db = Database()


@app.get("/")
def read_root():
    test = Database().select()

    return {"Hello": test}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/artist")
def read_artist():
    return db.select("artist")


@app.get("/artist/{id}")
def read_artist(id: int):
     return db.select_one("artist", id)

@app.post("/artist")
async def create_artist(artist: Artist):
    return db.insert(generate_query_columns_value(artist))

@app.put("/artist/{id}")
async def update_song(artist: Artist, id):
    return db.update_one(generate_query_columns_value(artist),artist.__str__().replace(" ",", "),id )


@app.delete("/artist/{id}")
def delete_artist(id: int):
     return db.delete_one("artist", id)



@app.get("/album")
def read_album():
    return db.select("album")

@app.get("/album/{id}")
def read_album(id: int):
    return db.select_one("album", id)

@app.post("/album")
async def create_album(album: Album):
    return db.insert(generate_query_columns_value(album))

@app.put("/album/{id}")
async def update_song(album: Album, id):
    return db.update_one(generate_query_columns_value(album),album.__str__().replace(" ",", "),id )


@app.delete("/album/{id}")
def delete_album(id: int):
    return db.delete_one("album", id)




@app.get("/song")
def read_song():
    return db.select("song")


@app.get("/song/{id}")
def read_song(id: int):
    return db.select_one("song",id)

@app.post("/song")
async def create_song(song: Song):
    return db.insert(generate_query_columns_value(song))

@app.put("/song/{id}")
async def update_song(song: Song,id):
    return db.update_one(generate_query_columns_value(song),song.__str__().replace(" ",", "),id )


@app.delete("/song/{id}")
def delete_song(id: int):
    return db.delete_one("song",id)