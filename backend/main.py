from typing import Union
from src.model_type import AlbumModel
from src.searchengine.index import Index
from src.models import Artist, Album, CartItem, OrderDetail, OrderItem, PaymentDetail, ShoppingSession, Song, Category, User, Promo, UserAddress


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

@app.put("/api/artist")
async def update_artist(artist: Artist):
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

@app.put("/api/album")
async def update_album(album: Album):
    return db.update_album(dict(album))

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

@app.get("/api/cart_item")
def read_cart_item():
    return db.select_cart_item()

@app.get("/api/cart_item/{id}")
def read_cart_item(id: int):
    return db.select_one_cart_item(id)

@app.get("/api/cart_item_by_shopsess/{shoppingsession_id}")
def read_cart_item_by_shoppingsessionid(shoppingsession_id: int):
    return db.select_one_cart_item_by_shoppingsession(shoppingsession_id)

@app.post("/api/cart_item")
async def create_cart_item(cart_item: CartItem):
    print("icart_item", cart_item)
    return db.insert_cart_item(dict(cart_item))

@app.put("/api/cart_item/{id}")
async def update_cart_item(cart_item: CartItem, id):
    return db.update_cart_item(dict(cart_item), id)

@app.delete("/api/cart_item_shopsessalbum/{shopsess_id}/{album_id}")
def delete_cart_item(shopsess_id: int, album_id:int):
     return db.delete_cart_item_by_shopsession_albumid(shopsess_id,album_id)

@app.delete("/api/cart_item/{id}")
def delete_cart_item(id: int):
     return db.delete_cart_item( id)

@app.get("/api/order_detail")
def read_order_detail():
    return db.select_order_detail()

@app.get("/api/pie_orders_per_category")
def pie_ordered_per_category():
    return db.pie_orders_per_category()

@app.get("/api/turnover_per_month/{year}")
def turnover_per_month_year(year:int):
    return db.turnover_per_month(year)

@app.get("/api/order_detail/{id}")
def read_order_detail(id: int):
    return db.select_one_order_detail(id)

@app.get("/api/order_detail_byid/{user_id}")
def read_order_detail(user_id: int):
    return db.select_last_one_order_detail_byuserid(user_id)

@app.post("/api/order_detail")
async def create_order_detail(order_detail: OrderDetail):
    print("iorder_detail", order_detail)
    return db.insert_order_detail(dict(order_detail))

@app.put("/api/order_detail")
async def update_order_detail(order_detail: OrderDetail):
    return db.update_order_detail(dict(order_detail))


@app.delete("/api/order_detail/{id}")
def delete_order_detail(id: int):
     return db.delete_order_detail( id)

@app.get("/api/order_item")
def read_order_item():
    return db.select_order_item()

@app.get("/api/order_item/{id}")
def read_order_item(id: int):
    return db.select_one_order_item(id)

@app.get("/api/order_item_by_orderdetailid/{id_orderdetail}")
def read_order_item(id_orderdetail: int):
    return db.select_order_items_by_orderdetailid(id_orderdetail)

@app.post("/api/order_item")
async def create_order_item(order_item: OrderItem):
    return db.insert_order_item(dict(order_item))

@app.put("/api/order_item/{id}")
async def update_order_item(order_item: OrderItem, id):
    return db.update_order_item(dict(order_item), id)

@app.delete("/api/order_item/{id}")
def delete_order_item(id: int):
     return db.delete_order_item( id)  

@app.get("/api/payment_detail")
def read_payment_detail():
    return db.select_payment_detail()

@app.get("/api/payment_detail/{id}")
def read_payment_detail(id: int):
    return db.select_one_payment_detail(id)

@app.post("/api/payment_detail")
async def create_payment_detail(payment_detail: PaymentDetail):
    return db.insert_payment_detail(dict(payment_detail))

@app.put("/api/payment_detail/{id}")
async def update_payment_detail(payment_detail: PaymentDetail, id):
    return db.update_payment_detail(dict(payment_detail), id)

@app.delete("/api/payment_detail/{id}")
def delete_payment_detail(id: int):
     return db.delete_payment_detail( id)

@app.get("/api/shopping_session")
def read_shopping_session():
    return db.select_shopping_session()

@app.get("/api/shopping_session/{id}")
def read_shopping_session(id: int):
    return db.select_one_shopping_session(id)

@app.get("/api/shopping_session_byuserid/{user_id}")
def read_last_one_shopping_session_byidalbum(user_id:int):
    return db.select_last_one_shopping_session_by_userid(user_id) 

@app.post("/api/shopping_session")
async def create_shopping_session(shopping_session: ShoppingSession):
    print("ishopping_session", shopping_session)
    return db.insert_shopping_session(dict(shopping_session))

@app.put("/api/shopping_session/{id}")
async def update_shopping_session(shopping_session: ShoppingSession, id):
    return db.update_shopping_session(dict(shopping_session), id)

@app.delete("/api/shopping_session/{id}")
def delete_shopping_session(id: int):
     return db.delete_shopping_session( id)

@app.get("/api/user_address")
def read_user_address():
    return db.select_user_address()

@app.get("/api/user_address/{id}")
def read_user_address(id: int):
    return db.select_one_user_address(id)

@app.post("/api/user_address")
async def create_user_address(user_address: UserAddress):
    print("iuser_address", user_address)
    return db.insert_user_address(dict(user_address))

@app.put("/api/user_address/{id}")
async def update_user_address(user_address: UserAddress, id):
    return db.update_user_address(dict(user_address), id)

@app.delete("/api/user_address/{id}")
def delete_user_address(id: int):
     return db.delete_user_address( id)

@app.get("/api/category")
def read_category():
    return db.select_category()

@app.post("/api/category")
async def create_category(category: Category):
    return db.insert_category(dict(category))

@app.put("/api/category")
async def update_category(category: Category):
    return db.update_category(dict(category))

@app.get("/api/promo")
def read_promo():
    return db.select_promo()

@app.post("/api/promo")
async def create_promo(promo: Promo):
    return db.insert_promo(dict(promo))

@app.get("/api/user")
def read_user():
    return db.select_user()

@app.get("/api/user/{id}")
def read_user(id: int):
    return db.select_one_user(id)

@app.post("/api/user")
async def create_user(user: User):
    print("iuser", user)
    return db.insert_user(dict(user))

@app.put("/api/user/{id}")
async def update_user(user: User, id):
    return db.update_user(dict(user), id)

@app.delete("/api/user/{id}")
def delete_user(id: int):
     return db.delete_user( id)


@app.delete("/api/artist/{id}")
def delete_artist(id: int):
     return db.delete_artist( id)

@app.delete("/api/album/{id}")
def delete_album(id: int):
    return db.delete_album(id)

@app.delete("/api/song/{id}")
def delete_song(id: int):
    return db.delete_song(id)

@app.get("/api/index/search/{text}")
def search_item(text: str):
    return Index().make_search(text)

@app.post("/api/index/add/album")
def add_album_to_index(obj: dict):
    #AlbumModel(obj.id, obj.title, obj.release_date, obj.cover, obj.artist_id, obj.price, obj.stock_qty,obj.description, obj.category_id, obj.created_date)
    return Index().insert_to_index(obj)
       

@app.post("/api/index/add/albums")
def add_all_to_index(obj: dict):
    return Index().init_album_index(obj)
      
# @app.post("/api/login")
# def read_user(data: Login):
#     return db.login(data)
