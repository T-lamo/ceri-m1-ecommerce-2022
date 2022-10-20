from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = "vinyl"
user = 'postgres'
password = 'password'
port = '5432'
host = '127.0.0.1'

SQLALCHEMY_DATABASE_URL = '''postgresql://{}:{}@{}:{}/{}'''.format(user,password,host,port,db)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
