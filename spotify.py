import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="e825b2eb9d73456fb74b50108dd1f8a3", client_secret="f06de69fc67c4ce185cb5deea4748141"))

# results = spotify.artist_top_tracks(taylor_uri, 'US')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
# for albums in albums:
#     print(albums['name'])

artist_name = 'BLACKPINK'
results = sp.search(q='artist:' + artist_name, type='artist')
artist_id = results['artists']['items'][0]['id']

# get list of artist's albums
albums = []
results = sp.artist_albums(artist_id, album_type='album')
albums.extend(results['items'])
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

# get list of artist's tracks
tracks = []
for album in albums:
    results = sp.album_tracks(album['id'])
    tracks.extend(results['items'])

list =[]

# print list of track names
for track in tracks:
    list.append(track['name'])
print(list)
