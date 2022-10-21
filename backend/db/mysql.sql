

create table artist(
   _id INT NOT NULL AUTO_INCREMENT,
   firstname VARCHAR(50) NOT NULL,
   lastname VARCHAR(50) NOT NULL,
   date_of_birth text,
   cover text,
   PRIMARY KEY ( _id )
);




CREATE TABLE category (
    _id int NOT NULL AUTO_INCREMENT,
    label VARCHAR(50),
    PRIMARY KEY (_id)
);

CREATE TABLE album (
    _id int NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    release_date VARCHAR(50),
    price int,
    description text,
    cover text,
    artist_id int,
    category_id int,
    PRIMARY KEY (_id),
    FOREIGN KEY (artist_id) REFERENCES artist(_id),
    FOREIGN KEY (category_id) REFERENCES category(_id)
);

CREATE TABLE song (
    _id int NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    release_date text,
    like_qty int,
    cover text,
    album_id int,
    PRIMARY KEY (_id),
    FOREIGN KEY (album_id) REFERENCES album(_id)
);

CREATE TABLE promo (
    _id int NOT NULL AUTO_INCREMENT,
    start_date text,
    end_date text,
    rate int,
    album_id int,
    PRIMARY KEY (_id),
    FOREIGN KEY (album_id) REFERENCES album(_id)
);

CREATE TABLE user (
    _id int NOT NULL AUTO_INCREMENT,
    username character varying(50),
    email character varying(50),
    password text,
    PRIMARY KEY (_id),
    is_admin boolean
);
