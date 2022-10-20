

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Song(Base):
    __tablename__ = "song"
    __table_args__= {
        'mysql_engine':'InnoDB'
    }

    _id= Column(Integer, primary_key=True, index=True)
    title= Column(String)
    release_date= Column(String)
    like_qty= Column(Integer)
    cover= Column(String)
    album_id= Column(Integer, ForeignKey("album._id"))
    album = relationship("Album", back_populates="song")


class Album(Base):
    __tablename__ = "album"
    __table_args__= {
        'mysql_engine':'InnoDB'
    }

    _id= Column(Integer, primary_key=True, index=True)
    category= Column(String)
    title= Column(String)
    release_date= Column(String)
    cover= Column(String)
    artist_id = Column(Integer, ForeignKey("artist._id"))
    
    song = relationship("Song", back_populates="album", uselist=False)
    artist_list = relationship("Artist", back_populates="album_list")

class Artist(Base):
    __tablename__ = "artist"
    __table_args__= {
        'mysql_engine':'InnoDB'
    }

    _id= Column(Integer, primary_key=True, index=True)
    firstname= Column(String)
    lastname= Column(String)
    date_of_birth= Column(String)
    cover= Column(String)
    album_list = relationship("Album", back_populates="artist_list",uselist=True)


   


