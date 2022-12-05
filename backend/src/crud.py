from functools import reduce
import mysql.connector
from mysql.connector import Error
from .models import Album, Artist, Category, Promo, Song, User


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
        data = Artist(firstname=artist['firstname'], lastname=artist['lastname'], date_of_birth=artist['date_of_birth'], cover=artist['cover'])
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_artist(self,artist:Artist):
        with Session(self.engine) as session:
            statement = select(Artist).where(Artist.id == artist['id'])
            results = session.exec(statement)
            update = results.one()
            update.firstname=artist['firstname']
            update.lastname=artist['lastname']
            update.date_of_birth=artist['date_of_birth']
            update.cover=artist['cover']
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
        data = Album(title=album['title'], release_date=album['release_date'], price=album['price'],stock_qty=album['stock_qty'], description=album['description'], cover=album['cover'], artist_id=album['artist_id'], category_id=album['category_id'])
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_album(self,album:Album):
        with Session(self.engine) as session:
            statement = select(Album).where(Album.id == album['id'])
            results = session.exec(statement)
            update = results.one()
            update.title= album['title'] 
            update.release_date=album['release_date']
            update.price=album['price']
            update.stock_qty=album['stock_qty']
            update.description=album['description'] 
            update.cover=album['cover'] 
            update.artist_id=album['artist_id'] 
            update.category_id=album['category_id']
            session.add(update)
            session.commit()

    def select_song(self):
        with Session(self.engine) as session:
            return list(session.exec(select(Song)))

    def select_one_song(self, id):
        with Session(self.engine) as session:
            return session.exec(select(Song).where(Song.id == id)).first()
            
    def insert_song(self, song:Song):
        data = Song(title=song['title'], release_date=song['release_date'],  cover=song['cover'], album_id=song['album_id'])
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def update_song(self,song:Song):
        with Session(self.engine) as session:
            statement = select(Song).where(Song.id == song['id'])
            results = session.exec(statement)
            update = results.one()
            update.title=song['title']
            update.release_date=song['release_date'] 
            update.cover=song['cover'] 
            update.album_id=song['album_id']
            session.add(update)
            session.commit()


   
   
    def select_category(self):
            with Session(self.engine) as session:
                statement = select(Category)
                results = session.exec(statement)
                results = map(Category.get_list_album,results)
                return list(results)

  
    def insert_category(self, category:Category):
        data = Category(label=category['label'])
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def select_promo(self):
            with Session(self.engine) as session:
                return list(session.exec(select(Promo)))

    def insert_promo(self, promo:Promo):
        data = Promo(start_date=promo['start_date'], end_date=promo['end_date'], rate=promo['rate'], album_id=promo['album_id'])
        session = Session(self.engine)
        session.add(data)
        session.commit()

    def select_user(self):
            with Session(self.engine) as session:
                return list(session.exec(select(User)))

  
    def insert_user(self, user:User):
        data = User(username=user['username'], email=user['email'],password=user['password'],is_admin=['is_admin'])
        session = Session(self.engine)
        session.add(data)
        session.commit()