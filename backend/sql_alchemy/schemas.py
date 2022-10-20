from typing import Union
from typing import List
from unicodedata import category

from pydantic import BaseModel

class Song(BaseModel):
    _id: int
    title: str
    release_date: str
    like_qty: int
    cover: str
    album_id: int


class Album(BaseModel):
    _id: int
    category: str
    title: str
    release_date: str
    cover: str
    artist_id: int
    songs: List[Song] = []

    class Config:
        orm_mode = True


class Artist(BaseModel):
    _id: Union[int, None] = None
    firstname: str
    lastname: str
    date_of_birth: str
    cover: str
    albums: List[Album] =[]

    class Config:
        orm_mode = True
