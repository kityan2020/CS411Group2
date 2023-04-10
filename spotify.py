import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import flask
from flask import Flask, Response, request, render_template, redirect, url_for, session
import random

import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# results = spotify.artist_top_tracks(taylor_uri, 'US')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
# for albums in albums:
#     print(albums['name'])


def Playlist(artist_name):
#You can change the name to any artist you want
    print(artist_name)
    results = spotify.search(q='artist:' + artist_name, type='artist')
    
    artist_id = results['artists']['items'][0]['id']
    

    # get list of artist's albums
    albums = []
    results = spotify.artist_albums(artist_id, album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    # get list of artist's tracks
    tracks = []
    for album in albums:
        results = spotify.album_tracks(album['id'])
        tracks.extend(results['items'])

    list1 = []

    # print list of track names
    for track in tracks:
        list1.append(track['name'])
    songs = list(set(list1))
    random.shuffle(songs)
    if len(songs) < 20:
        return songs
    else: 
        return songs[:20]

def singleAlbum():
    artist_name = 'BLACKPINK'
    results = spotify.search(q='artist:' + artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']

    # get list of artist's albums
    albums = []
    results = spotify.artist_albums(artist_id, album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    
    album_name = 'Born Pink'
    
    for album in albums:
        if album['name'].lower() == album_name.lower():
            album_id = album['id']
            album_details = spotify.album(album_id)
            break

# print album details
    print('Album name:', album_details['name'])
    print('Artist:', album_details['artists'][0]['name'])
    print('Release date:', album_details['release_date'])
    print('Total tracks:', album_details['total_tracks'])
    return 

