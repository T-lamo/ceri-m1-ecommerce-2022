

from typing import Optional,List
from xmlrpc.client import Boolean
from datetime import datetime


from sqlmodel import Field, SQLModel, Relationship

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    label: str
    albums: List["Album"] = Relationship(back_populates="category")
    created_date: datetime 
    

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
    created_date: datetime 

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
    stock_qty:int
    description: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    created_date: datetime 

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
    created_date: datetime 

class Song(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    release_date: str
    cover: str
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    album: Optional[Album] = Relationship(back_populates="songs")
    created_date: datetime 


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    telephone: str
    email: str
    username: str
    firstname: str
    password: str = "password"
    is_admin: Boolean
    created_date: datetime 



class UserAddress(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    address_line1: str
    address_line2: str
    city: str
    postal_code: str
    country: str
    mobile: str
    user_id: int
    created_date: datetime 


class ShoppingSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: float
    user_id: int
    created_date: datetime 

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    album_id: int
    qty: int
    shopping_session_id: int
    created_date: datetime 

class OrderDetail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: str
    user_id: int
    payment_status: Boolean
    delivery_status: Boolean
    send_status: Boolean
    orders_status: str 
    created_date: datetime 


class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    qty: int
    order_detail_id: int
    album_id:int
    created_date: datetime 

class PaymentDetail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    amount: int
    credit_card_number: str
    provider: str
    order_detail_id: int
    expiration_date: str
    cvv: str
    status: Boolean
    created_date: datetime 

class Login():
    username: str
    password: str

