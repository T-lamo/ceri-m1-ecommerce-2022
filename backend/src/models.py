

from typing import Optional,List
from xmlrpc.client import Boolean

from sqlmodel import Field, SQLModel, Relationship

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    label: str
    albums: List["Album"] = Relationship(back_populates="category")

    def get_list_album(item):
        data = dict(item)
        data["list_album"]= item.albums
        return data

class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    date_of_birth: str
    cover: str
    albums: List["Album"] = Relationship(back_populates="artist")

    def get_list_album(item):
        data = dict(item)
        data["list_album"]= item.albums
        return data

class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    title: str
    release_date: str
    cover: str
    artist_id:  Optional[int] = Field(default=None, foreign_key="artist.id")
    price: int
    description: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
   
    artist: Optional[Artist] = Relationship(back_populates="albums")
    category: Optional[Category] = Relationship(back_populates="albums")

    songs: List["Song"] = Relationship(back_populates="album")

    def get_list_song(item):
        data = dict(item)
        data["list_song"]= item.songs
        return data
    
class Promo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_date: str
    end_date: str
    rate: int
    album_id: int

class Song(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    release_date: str
    like_qty: int
    cover: str
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    album: Optional[Album] = Relationship(back_populates="songs")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str = "password"
    is_admin: Boolean

class Login():
    username: str
    password: str


#Create 
# class ArtistCreate():
#     list_album= [] 



# class AlbumCreate():
#     id: Optional[int] = Field(default=None, primary_key=True) 
#     title: str
#     release_date: str
#     cover: str
#     artist_id:  Optional[int] = Field(default=None, foreign_key="artist.id")
#     price: int
#     description: str
#     category_id: int
#     artist: Optional[Artist] = Relationship(back_populates="list_album")


   
# class CategoryCreate():
#     id: Optional[int] = Field(default=None, primary_key=True)
#     label: str

    
# class PromoCreate():
#     id: Optional[int] = Field(default=None, primary_key=True)
#     start_date: str
#     end_date: str
#     rate: int
#     album_id: int

# class SongCreate():
#     id: Optional[int] = Field(default=None, primary_key=True)
#     title: str
#     release_date: str
#     like_qty: int
#     cover: str
#     album_id: int

# class UserCreate():
#     id: Optional[int] = Field(default=None, primary_key=True)
#     username: str
#     email: str
#     password: str = "password"
#     is_admin: Boolean


