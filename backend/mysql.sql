create table artist(
   id INT NOT NULL AUTO_INCREMENT,
   firstname VARCHAR(50) NOT NULL,
   lastname VARCHAR(50) NOT NULL,
   date_of_birth text,
   cover text,
   PRIMARY KEY ( id )
);

CREATE TABLE category (
    id int NOT NULL AUTO_INCREMENT,
    label VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE album (
    id int NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    release_date VARCHAR(50),
    price int,
    description text,
    cover text,
    artist_id int,
    category_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (artist_id) REFERENCES artist(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE song (
    id int NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    release_date text,
    like_qty int,
    cover text,
    album_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (album_id) REFERENCES album(id)
);

CREATE TABLE promo (
    id int NOT NULL AUTO_INCREMENT,
    start_date text,
    end_date text,
    rate int,
    album_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (album_id) REFERENCES album(id)
);

CREATE TABLE user (
    id int NOT NULL AUTO_INCREMENT,
    username character varying(50),
    email character varying(50),
    password text,
    PRIMARY KEY (id),
    is_admin boolean
);
