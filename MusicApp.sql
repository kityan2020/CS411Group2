drop database MusicApp;
create database MusicApp;

use MusicApp;

CREATE TABLE users (
    user_id int4  AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY (user_id) 
    );

CREATE TABLE playlist(
    song_id  int4 AUTO_INCREMENT,
    song_name VARCHAR(500),
    user_id  int4,
    PRIMARY KEY (song_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


--default playlist (liked songs)
INSERT INTO MusicApp.playlists (pl_id,pl_name) VALUES (1,'liked songs');


