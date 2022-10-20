from functools import reduce
import psycopg2

from models import Artist, Song, Album, Artist, Promo, User




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
        self.password = '1MG7oE'
        self.port = '5432'
        self.host = 'pedago.univ-avignon.fr'
        # self.db = "vinyl_dev"
        # self.user = 'postgres'
        # self.password = 'password'
        # self.port = '5432'
        # self.host = '127.0.0.1'

    def open_connexion(self):
        # establishing the connection
        return psycopg2.connect(
            database=self.db, user=self.user, password=self.password, host=self.host, port=self.port
        )

    def select_artist(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from artist;''')
        artist = cursor.fetchall()
        conn.close()
        return artist

    def select_one_artist(self, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from artist where _id ={};'''.format(id))
        res = cursor.fetchall()
        conn.close()
        return res

    def insert_artist(self, artist: Artist):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = ''' 
        insert into artist (firstname , lastname , date_of_birth , cover)
        VALUES ('{}','{}','{}','{}') RETURNING *;'''.format(artist['firstname'], artist['lastname'], artist['date_of_birth'], artist['cover'])
        cursor.execute(query)
        last_row_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_id

    def update_artist(self, artist, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''UPDATE artist SET firstname='{}', lastname='{}', date_of_birth='{}', cover='{}' 
        where _id = '{}' RETURNING *  ;'''.format(artist['firstname'], artist['lastname'], artist['date_of_birth'], artist['cover'], id)
        print("update query", query)
        cursor.execute(query)
        last_row_update = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_update

    def delete_artist(self, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''delete from artist  where _id ={} RETURNING *; '''.format(
            id)
        res = cursor.execute(query)
        conn.commit()
        conn.close()
        return res

    # album
    def select_album(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from album;''')
        album = cursor.fetchall()
        conn.close()
        return album

    def select_one_album(self, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from album where _id ={};'''.format(id))
        res = cursor.fetchall()
        conn.close()
        return res

    def insert_album(self, album: Album):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = ''' 
        insert into album ( title, release_date ,price , description , cover ,artist_id , category_id)
        VALUES ('{}','{}','{}','{}','{}','{}','{}') RETURNING *;'''.format(album['title'], album['release_date'], album['price'], album['description'], album['cover'], album['artist_id'], album['category_id'])
        cursor.execute(query)
        last_row_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_id

    def update_album(self, album, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''UPDATE album SET title='{}', release_date='{}', price='{}', description='{}', cover='{}', artist_id='{}',category_id='{}' 
        where _id = '{}' RETURNING *  ;'''.format(album['title'], album['release_date'], album['price'], album['description'], album['cover'], album['artist_id'], album['category_id'], id)
        print("update query", query)
        cursor.execute(query)
        last_row_update = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_update

    def delete_album(self, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''delete from album where _id ={} RETURNING *; '''.format(id)
        res = cursor.execute(query)
        conn.commit()
        conn.close()
        return res

    # song
    def select_song(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from song;''')
        res = cursor.fetchall()
        conn.close()
        return res

    def select_one_song(self, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from song where _id ={};'''.format(id))
        res = cursor.fetchall()
        conn.close()
        return res

    def insert_song(self, song: Song):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = ''' 
        insert into song ( title, release_date ,like_qty , cover, album_id )
        VALUES ('{}','{}','{}','{}','{}') RETURNING *;'''.format(song['title'], song['release_date'], song['like_qty'], song['cover'], song['album_id'])
        cursor.execute(query)
        last_row_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_id

    def update_song(self, song, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''UPDATE song SET title='{}', release_date='{}', like_qty='{}', cover='{}', album_id='{}' 
        where _id = '{}' RETURNING *  ;'''.format(song['title'], song['release_date'], song['like_qty'], song['cover'], song['album_id'], id)
        print("update query", query)
        cursor.execute(query)
        last_row_update = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_update

    def delete_song(self, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''delete from song where _id ={} RETURNING *; '''.format(id)
        res = cursor.execute(query)
        conn.commit()
        conn.close()
        return res

    # promo
    def select_promo(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from promo;''')
        res = cursor.fetchall()
        conn.close()
        return res

    def select_one_promo(self, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from promo where _id ={};'''.format(id))
        res = cursor.fetchall()
        conn.close()
        return res

    def insert_one_promo(self, promo: Promo):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = ''' 
        insert into promo ( start_date, end_date ,rate, album_id )
        VALUES ('{}','{}','{}','{}') RETURNING *;'''.format(promo['start_date'], promo['end_date'], promo['rate'], promo['album_id'])
        cursor.execute(query)
        last_row_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_id


    def delete_promo(self, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        query = '''delete from promo where _id ={} RETURNING *; '''.format(id)
        res = cursor.execute(query)
        conn.commit()
        conn.close()
        return res



     # user
    def select_user(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from user;''')
        res = cursor.fetchall()
        conn.close()
        return res

    def select_one_user(self, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from user where _id ={};'''.format(id))
        res = cursor.fetchall()
        conn.close()
        return res

    def insert_one_user(self, user: User):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = ''' 
        insert into user ( username,email,password, is_admin)
        VALUES ('{}','{}','{}','{}') RETURNING *;'''.format(user['username'], user['email'], user['password'], user['is_admin'])
        cursor.execute(query)
        last_row_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_id

    # category
    def select_category(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from category;''')
        category = cursor.fetchall()
        conn.close()
        return category


if __name__ == "__main__":
    # The client code.
    def convert_to_dict(item):
        return {"section": item[0], "group": item[1], "subject": item[2], "class": item[3], "time": item[4]}
    result = list(filter(lambda item: Database().get_schedule(
        item, ("M1", "alternant")), Database().select()))
