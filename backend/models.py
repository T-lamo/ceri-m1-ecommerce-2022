from typing import Union
from unicodedata import category
from xmlrpc.client import Boolean

from pydantic import BaseModel


class Album(BaseModel):
    _id: int
    title: str
    release_date: str
    cover: str
    artist_id: int
    price: int
    description: str
    category_id: int

   
    def __str__(self):
        return '''title='{}',release_date='{}',cover='{}',artist_id='{}',price='{}',description='{}',category_id='{}' '''.format(self.title,self.release_date,self.cover, self.artist_id,self.price,self.description,self.category_id)


class Artist(BaseModel):
    _id: Union[int, None] = None
    firstname: str
    lastname: str
    date_of_birth: str
    cover: str


    def __str__(self):
        return '''firstname='{}',lastname='{}',date_of_birth='{}',cover='{}' '''.format(self.firstname,self.lastname,self.date_of_birth,self.cover)

class Category(BaseModel):
    _id: Union[int, None]= None
    label: str

    def __str__(self):
        return '''title='{}' '''.format(self.label)

class Promo(BaseModel):
    _id: int
    start_date: str
    end_date: str
    rate: int
    album_id: int


    def __str__(self):
        return '''start_date='{}', end_date='{}',rate='{}',album_id='{}' '''.format(self.start_date,self.end_date,self.rate,self.album_id)

class Song(BaseModel):
    _id: int
    title: str
    release_date: str
    like_qty: int
    cover: str
    album_id: int

    def __str__(self):
        return '''title='{}', release_date='{}',like_qty='{}',cover='{}', album_id='{}' '''.format(self.title,self.release_date,self.like_qty,self.cover,self.album_id)

class User(BaseModel):
    _id: int
    username: str
    email: str
    password: str = "password"
    is_admin: Boolean
