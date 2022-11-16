from functools import reduce
from typing import Union
from src.models import Artist, Album, Song, Category, User, Promo


from src.crud import Database


from fastapi import  FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()


@app.get("/")
def read_root():
    #test = Database().select()
    return {"Hello"}



@app.get("/api/artist",status_code=200)
def read_artist():
    return db.select_artist()

@app.get("/api/artist/{id}")
def read_artist(id: int):
    
     return db.select_one_artist( id)

@app.post("/api/artist",status_code=201)
async def create_artist(artist: Artist):
    return db.insert_artist(dict(artist))

@app.put("/api/artist/{id}")
async def update(artist: Artist):
    return db.update_artist(dict(artist))

@app.get("/api/album")
def read_album():
    return db.select_album()

@app.get("/api/album/{id}")
def read_album(id: int):
    return db.select_one_album(id)

@app.post("/api/album")
async def create_album(album: Album):
    print("ialbum", album)
    return db.insert_album(dict(album))

@app.put("/api/album/{id}")
async def update_album(album: Album, id):
    return db.update_album(dict(album), id)

@app.get("/api/song")
def read_song():
    return db.select_song()


@app.get("/api/song/{id}")
def read_song(id: int):
    return db.select_one_song(id)

@app.post("/api/song")
async def create_song(song: Song):
    return db.insert_song(dict(song))

@app.put("/api/song/{id}")
async def update_song(song: Song,id):
    return db.update_song(dict(song), id)

@app.get("/api/category")
def read_category():
    return db.select_category()

@app.post("/api/category")
async def create_category(category: Category):
    return db.insert_category(dict(category))


@app.get("/api/promo")
def read_promo():
    return db.select_promo()

@app.post("/api/promo")
async def create_promo(promo: Promo):
    return db.insert_promo(dict(promo))

@app.get("/api/user")
def read_user():
    return db.select_user()


@app.post("/api/user")
async def create_user(user: User):
    return db.insert_user(dict(user))


@app.delete("/api/artist/{id}")
def delete_artist(id: int):
     return db.delete_artist( id)

@app.delete("/api/album/{id}")
def delete_album(id: int):
    return db.delete_album(id)

@app.delete("/api/song/{id}")
def delete_song(id: int):
    return db.delete_song(id)

'''
@app.post("/api/login")
def read_user(data: Login):
    return db.login(data)
'''