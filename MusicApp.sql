drop database MusicApp;
create database MusicApp;

use MusicApp;

CREATE TABLE users (
    user_id int4  AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY (user_id) 
    );

CREATE TABLE playlists(
    pl_id  int4 AUTO_INCREMENT,
    pl_name VARCHAR(100),
    user_id  int4,
    PRIMARY KEY (pl_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE in_pl(
    pl_id int4,
    music_id int4,
    PRIMARY KEY (pl_id,music_id),
    FOREIGN KEY (pl_id) REFERENCES playlists(pl_id)
)

CREATE TABLE search_history(
    sh_id int4 AUTO_INCREMENT,
    keyword VARCHAR(500),
    user_id int4,
    PRIMARY KEY (sh_id),
    FOREIGN KEY user_id REFERENCES users(user_id)
)
--default playlist (liked songs)
INSERT INTO MusicApp.playlists (pl_id,pl_name) VALUES (1,'liked songs');


