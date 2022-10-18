from asyncio import open_connection
import psycopg2


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
        self.db = "vinyl"
        self.user = 'postgres'
        self.password = 'password'
        self.port = '5432'
        self.host = '127.0.0.1'

        data = {
            'name': "agenda",
            'columns':"section, grp, name, room, time",
            'values': ('M1', 'classique', 'outils pour apprentis', 'S4', '13:00')
        }
        
        # self.insert(data)

    def open_connexion(self):
        # establishing the connection
        return psycopg2.connect(
            database=self.db, user=self.user, password=self.password, host=self.host, port=self.port
        )
    
    def select(self, table_name):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from {};'''.format(table_name))
        res_tuple = cursor.fetchall()
        conn.close()
        return res_tuple

    def select_one(self, table_name, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        cursor.execute('''select * from {} where _id ={};'''.format(table_name,id))
        res_tuple = cursor.fetchall()
        conn.close()
        return res_tuple


    def delete_one(self, table_name, id):
        conn = self.open_connexion()
        cursor = conn.cursor()
        query = '''delete from {} where _id ={};'''.format(table_name,id)
        res=cursor.execute(query)
        conn.commit()
        conn.close()
        return res

        
    def insert(self,data):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''INSERT INTO {} ({}) VALUES {} RETURNING _id;'''.format(data['name'],data['columns'],data['values'])
        cursor.execute(query)
        last_row_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_id


    def update_one(self,data, new_val, id):
        conn = self.open_connexion()
        conn.autocommit = True
        cursor = conn.cursor()
        query = '''UPDATE {} SET {}  where _id = {} RETURNING _id , {} ;'''.format(data['name'],new_val,id,data['columns'])
        cursor.execute(query)
        last_row_update = cursor.fetchone()
        conn.commit()
        conn.close()
        return last_row_update

    def get_schedule(self,item,data):
        if(item[0]==data[0] and item[1]==data[1]):
            return True
        else: 
            return False


if __name__ == "__main__":
    # The client code.
    def convert_to_dict(item):
        return {"section":item[0], "group":item[1], "subject":item[2], "class": item[3], "time": item[4]}
    result=list(filter(lambda item:Database().get_schedule(item, ("M1","alternant")),Database().select()))
    

   

#create table album (_id SERIAL PRIMARY KEY ,category varchar(50),  titre varchar(50),realease_date varchar(50), cover TEXT, artist_id INTEGER, CONSTRAINT fk_artist FOREIGN KEY(artist_id) REFERENCES artist(_id));
#insert into artist(firstname, lastname, date_of_birth, cover) VALUES ('Amos', 'DORCEUS', '01/01/2010', 'URL');
#create table artist (_id SERIAL PRIMARY KEY ,firstname varchar(50), lastname varchar(50), date_of_birth varchar(50), cover TEXT);
#insert into album (category, titre, realease_date, cover, artist_id) values ('Love', 'You are beautiful','date', 'url', 1);
#create table song (_id SERIAL PRIMARY KEY , titre varchar(50), realease_date varchar(50), like_qty INTEGER, cover TEXT, album_id INTEGER, CONSTRAINT fk_album FOREIGN KEY (album_id) REFERENCES album(_id));