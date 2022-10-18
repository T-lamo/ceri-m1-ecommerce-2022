from typing import Union

from pydantic import BaseModel

class Song(BaseModel):
    _id: int
    titre: str
    realease_date: str
    like_qty: int
    cover: str
    album_id: int

def __str__(self):
    return f'titre={self.titre}, realease_date={self.realease_date},like_qty={self.like_qty},cover={self.cover}, album_id={self.album_id}'
