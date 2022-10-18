from typing import Union
from unicodedata import category

from pydantic import BaseModel

class Album(BaseModel):
    _id: int
    category: str
    titre: str
    realease_date: str
    cover: str
    artist_id: int

def __str__(self):
    return f'category={self.category}, titre={self.titre},realease_date={self.realease_date},cover={self.cover}, artist_id={self.artist_id}'
