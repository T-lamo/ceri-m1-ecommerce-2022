from datetime import datetime
from functools import reduce
import mysql.connector
from mysql.connector import Error
from .models import Album, Artist, CartItem, Category, OrderDetail, OrderItem, PaymentDetail, Promo, ShoppingSession, Song, User, UserAddress


from sqlmodel import Field, Session, SQLModel, create_engine,select



class DatabaseSingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=DatabaseSingletonMeta):

    def __init__(self):
        self.db = "uapv2201069"
        self.user = 'uapv2201069'
        self.password = 'WmAsN1'
        self.host = 'pedago.univ-avignon.fr'
        print("test")
        self.db = "ecom_db"
        self.user = 'root'
        self.password = 'mypass'
        self.host = 'db'
        


        mysql_url = f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.db}?charset=utf8mb4"
        self.engine = create_engine(mysql_url, echo=True)
           

        SQLModel.metadata.create_all(self.engine)
 

    def select_artist(self):
        with Session(self.engine) as session:
            statement = select(Artist)
            results = session.exec(statement)
            results = map(Artist.get_list_album,results)
            return list(results)

    def select_one_artist(self, id):
        with Session(self.engine) as session:
            statement=select(Artist).where(Artist.id == id)
            result = session.exec(statement).first()
            return Artist.get_list_album(result)
            
    def insert_artist(self, artist:Artist):
        data = Artist(firstname=artist['firstname'], lastname=artist['lastname'], date_of_birth=artist['date_of_birth'], cover=artist['cover'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_artist(self,artist:Artist, id):
        with Session(self.engine) as session:
            statement = select(Artist).where(Artist.id == id)
            results = session.exec(statement)
            update = results.one()
            update.firstname=artist['firstname']
            update.lastname=artist['lastname']
            update.date_of_birth=artist['date_of_birth']
            update.cover=artist['cover']
            update.created_date= datetime.now()
            update.created_date= datetime.now()
            session.add(update)
            session.commit()

    def delete_artist(self,id):
        with Session(self.engine) as session:
            statement = select(Artist).where(Artist.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def delete_album(self,id):
        with Session(self.engine) as session:
            statement = select(Album).where(Album.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def delete_song(self,id):
        with Session(self.engine) as session:
            statement = select(Song).where(Song.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()


    def select_album(self):
        with Session(self.engine) as session:
            statement = select(Album)
            results = session.exec(statement)
            results = map(Album.get_list_song,results)
            return list(results)

    def select_one_album(self, id):
        with Session(self.engine) as session:
            statement=select(Album).where(Album.id == id)
            result = session.exec(statement).first()
            return Album.get_list_song(result)
            
    def insert_album(self, album:Album):
        data = Album(title=album['title'], release_date=album['release_date'], price=album['price'],stock_qty=album['stock_qty'], description=album['description'], cover=album['cover'], artist_id=album['artist_id'], category_id=album['category_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_album(self,album:Album, id):
        with Session(self.engine) as session:
            statement = select(Album).where(Album.id == id)
            results = session.exec(statement)
            update = results.one()
            update.title= album['title'] 
            update.release_date=album['release_date']
            update.price=album['price']
            update.stock_qty=album['stock_qty']
            update.description=album['description'] 
            update.cover=album['cover'] 
            update.created_date= datetime.now()
            update.artist_id=album['artist_id'] 
            update.category_id=album['category_id']
            update.created_date= datetime.now()

            session.add(update)
            session.commit()

    def select_song(self):
        with Session(self.engine) as session:
            return list(session.exec(select(Song)))

    def select_one_song(self, id):
        with Session(self.engine) as session:
            return session.exec(select(Song).where(Song.id == id)).first()
            
    def insert_song(self, song:Song):
        data = Song(title=song['title'], release_date=song['release_date'],  cover=song['cover'], album_id=song['album_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_song(self,song:Song, id):
        with Session(self.engine) as session:
            statement = select(Song).where(Song.id == id)
            results = session.exec(statement)
            update = results.one()
            update.title=song['title']
            update.release_date=song['release_date'] 
            update.cover=song['cover'] 
            update.created_date= datetime.now()
            update.album_id=song['album_id']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()

# Ajout table
    def select_cart_item(self):
        with Session(self.engine) as session:
            return list(session.exec(select(CartItem)))

    def select_one_cart_item(self, id):
        with Session(self.engine) as session:
            return session.exec(select(CartItem).where(CartItem.id == id)).first()
            
    def insert_cart_item(self, item:CartItem):
        data = CartItem(total=item['total'], album_id=item['album_id'],  qty=item['qty'], shopping_session_id=item['shopping_session_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_cart_item(self,item:CartItem, id):
        with Session(self.engine) as session:
            statement = select(CartItem).where(CartItem.id == id)
            results = session.exec(statement)
            update = results.one()
            update.total=item['total']
            update.qty=item['qty'] 
            update.shopping_session_id=item['shopping_session_id'] 
            update.album_id=item['album_id']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()

    def delete_cart_item(self,id):
        with Session(self.engine) as session:
            statement = select(CartItem).where(CartItem.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_order_detail(self):
        with Session(self.engine) as session:
            return list(session.exec(select(OrderDetail)))

    def select_one_order_detail(self, id):
        with Session(self.engine) as session:
            return session.exec(select(OrderDetail).where(OrderDetail.id == id)).first()
            
    def insert_order_detail(self, item:OrderDetail):
        data = OrderDetail(total=item['total'], user_id=item['user_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_order_detail(self,item:OrderDetail, id):
        with Session(self.engine) as session:
            statement = select(OrderDetail).where(OrderDetail.id == id)
            results = session.exec(statement)
            update = results.one()
            update.total=item['total']
            update.user_id=item['user_id']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()

    def delete_order_detail(self,id):
        with Session(self.engine) as session:
            statement = select(OrderDetail).where(OrderDetail.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_order_item(self):
        with Session(self.engine) as session:
            return list(session.exec(select(OrderItem)))

    def select_one_order_item(self, id):
        with Session(self.engine) as session:
            return session.exec(select(OrderItem).where(OrderItem.id == id)).first()
            
    def insert_order_item(self, item:OrderItem):
        data = OrderItem(qty=item['qty'], order_detail_id=item['order_detail_id'],  created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_order_item(self,item:OrderItem, id):
        with Session(self.engine) as session:
            statement = select(OrderItem).where(OrderItem.id == id)
            results = session.exec(statement)
            update = results.one()
            update.qty=item['qty'] 
            update.order_detail_id=item['order_detail_id']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()
    
    def delete_order_item(self,id):
        with Session(self.engine) as session:
            statement = select(OrderItem).where(OrderItem.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_payment_detail(self):
        with Session(self.engine) as session:
            return list(session.exec(select(PaymentDetail)))

    def select_one_payment_detail(self, id):
        with Session(self.engine) as session:
            return session.exec(select(PaymentDetail).where(PaymentDetail.id == id)).first()
            
    def insert_payment_detail(self, item:PaymentDetail):
        data = PaymentDetail(amount=item['amount'], status=item['status'],  order_detail_id=item['order_detail_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_payment_detail(self,item:PaymentDetail, id):
        with Session(self.engine) as session:
            statement = select(PaymentDetail).where(PaymentDetail.id == id)
            results = session.exec(statement)
            update = results.one()
            update.amount=item['amount']
            update.status=item['status'] 
            update.order_detail_id=item['order_detail_id'] 
            update.created_date= datetime.now()
            session.add(update)
            session.commit()

    def delete_payment_detail(self,id):
        with Session(self.engine) as session:
            statement = select(PaymentDetail).where(PaymentDetail.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_shopping_session(self):
        with Session(self.engine) as session:
            return list(session.exec(select(ShoppingSession)))

    def select_one_shopping_session(self, id):
        with Session(self.engine) as session:
            return session.exec(select(ShoppingSession).where(ShoppingSession.id == id)).first()
            
    def insert_shopping_session(self, item:ShoppingSession):
        data = ShoppingSession(total=item['total'], user_id=item['user_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_shopping_session(self,item:ShoppingSession, id):
        with Session(self.engine) as session:
            statement = select(ShoppingSession).where(ShoppingSession.id == id)
            results = session.exec(statement)
            update = results.one()
            update.total=item['total']
            update.user_id=item['user_id']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()

    def delete_shopping_session(self,id):
        with Session(self.engine) as session:
            statement = select(ShoppingSession).where(ShoppingSession.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_user_address(self):
        with Session(self.engine) as session:
            return list(session.exec(select(UserAddress)))

    def select_one_user_address(self, id):
        with Session(self.engine) as session:
            return session.exec(select(UserAddress).where(UserAddress.id == id)).first()
            
    def insert_user_address(self, item:UserAddress):
        data = UserAddress(address_line1=item['address_line1'], address_line2=item['address_line2'],  city=item['city'], postal_code=item['postal_code'],country=item['country'],mobile=item['mobile'],user_id=item['user_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_user_address(self,item:UserAddress, id):
        with Session(self.engine) as session:
            statement = select(UserAddress).where(UserAddress.id == id)
            results = session.exec(statement)
            update = results.one()
            update.address_line1=item['address_line1']
            update.address_line2=item['address_line2'] 
            update.city=item['city'] 
            update.postal_code=item['postal_code']
            update.country=item['country']
            update.mobile=item['mobile']
            update.user_id=item['user_id']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()
    
    def delete_user_address(self,id):
        with Session(self.engine) as session:
            statement = select(UserAddress).where(UserAddress.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()
   
    def select_category(self):
            with Session(self.engine) as session:
                statement = select(Category)
                results = session.exec(statement)
                results = map(Category.get_list_album,results)
                return list(results)

  
    def insert_category(self, category:Category):
        data = Category(label=category['label'],created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def delete_category(self,id):
        with Session(self.engine) as session:
            statement = select(Category).where(Category.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_promo(self):
            with Session(self.engine) as session:
                return list(session.exec(select(Promo)))

    def insert_promo(self, promo:Promo):
        data = Promo(start_date=promo['start_date'], end_date=promo['end_date'], rate=promo['rate'], album_id=promo['album_id'], created_date=datetime.now())
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def delete_promo(self,id):
        with Session(self.engine) as session:
            statement = select(Promo).where(Promo.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()

    def select_user(self):
            with Session(self.engine) as session:
                return list(session.exec(select(User)))

  
    def select_one_user(self, id):
        with Session(self.engine) as session:
            return session.exec(select(User).where(User.id == id)).first()
            
    def insert_user(self, item:User):
            data = User(telephone=item['telephone'], firstname=item['firstname'], lastname=item['lastname'],email=item['email'],username=item['username'], password=item['password'], is_admin=item['is_admin'], created_date=datetime.now())
            session = Session(self.engine)
            session.add(data)
            session.commit()
           

    def update_user(self,item:User, id):
        with Session(self.engine) as session:
            statement = select(User).where(User.id == id)
            results = session.exec(statement)
            update = results.one()
            update.telephone=item['telephone'] 
            update.email=item['username']
            update.email=item['firtname']
            update.email=item['lastname']
            update.email=item['email']
            update.password=item['password']
            update.is_admin=item['is_admin']
            update.created_date= datetime.now()
            session.add(update)
            session.commit()
    
    def delete_user(self,id):
        with Session(self.engine) as session:
            statement = select(User).where(User.id == id)
            results = session.exec(statement)
            results = results.one()
            session.delete(results)
            session.commit()