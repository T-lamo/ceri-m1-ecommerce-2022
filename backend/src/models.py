

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
    stock_qty:int
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
    cover: str
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    album: Optional[Album] = Relationship(back_populates="songs")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    firstname: str
    lastname: str
    telephone: str
    email: str
    password: str = "password"
    is_admin: Boolean
    user_payment: List["UserPayment"] = Relationship(back_populates="user")

    def get_list_album(item):
        data = dict(item)
        data["list_album"]= item.albums
        return data

class UserAddress(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    address_line1: str
    address_line2: str
    city: str
    postal_code: str
    country: str
    mobile: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    
class ShoppingSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: float
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: float
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    qty: int
    shopping_session_id: Optional[int] = Field(default=None, foreign_key="shoppingsession.id")

class UserPayment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    payment_type: str
    provider: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="user_payment")

    



class OrderDetail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    qty: int
    order_detail_id: Optional[int] = Field(default=None, foreign_key="orderdetail.id")
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
class PaymentDetail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    status: Boolean
    order_detail_id: Optional[int] = Field(default=None, foreign_key="orderdetail.id")

    
    
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
#     stock_qty: int
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
#     cover: str
#     album_id: int

# class UserCreate():
#     id: Optional[int] = Field(default=None, primary_key=True)
#     username: str
#     email: str
#     password: str = "password"
#     is_admin: Boolean


