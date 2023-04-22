from flask import Flask, jsonify, request, url_for, redirect, render_template, session
import spotify
import ticketmaster
import json
import mysql.connector
import os
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import secrets
#Kits SQL Password = 911Apexpredator
secret_key = secrets.token_hex(16)
print(secret_key)
app = Flask(__name__)
app.secret_key = secret_key
app.config['SESSION_COOKIE_NAME'] = 'Kits Cookie'
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get the username and password from the form data
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        # check if the username and password are correct (replace this with your own authentication logic)
        mycursor.execute("SELECT password FROM MusicApp.users WHERE email = '{0}'".format(username))
        real_password= mycursor.fetchone()
        real_password_int=str(int(real_password[0]))
        # print(real_password,real_password_int,real_password_int==password)
        if real_password_int==password:
            # if the login is successful, redirect to the main page
            # print("redirect to main")
            session['email'] = username
            return render_template('Main.HTML')

        else:
            # if the login is not successful, redirect back to the login page with an error message
            return render_template('login.html', error='Invalid username or password')

    # if the request method is GET, render the login page
    return render_template('login.html')

@app.route('/')
def start():
    return render_template('register.html')
@app.route('/', methods=['GET', 'POST'])
def register():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        print(email,password)
    except:
        print("please make sure enter all information")
        return redirect(url_for('start'))
    mycursor.execute('''INSERT INTO MusicApp.users(email,password) VALUES (%s, %s)''', (email, password))
    mydb.commit()
    session['email'] = email
    return render_template('Main.HTML')


# @app.route('/')
# def start():
#     sp_oauth = create_spotify_oauth()
#     author_url = sp_oauth.get_authorize_url()
#     return redirect(author_url)

# def create_spotify_oauth():
#     return SpotifyOAuth(
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         redirect_uri=url_for('register',_external=True),
#         scope="user-library-read",
#     )

@app.route('/Main')
def playlist():
    return render_template('Main.html')


@app.route('/playlist')
def displaypl():
    email=session.get('email')
    print(email)
    mycursor.execute("SELECT user_id FROM MusicApp.users WHERE email = '{0}'".format(email))
    uid= mycursor.fetchone()
    uid_int=uid[0]
    print(uid_int)
    mycursor.execute("SELECT song_name FROM MusicApp.playlist WHERE user_id = '{0}'".format(uid_int))
    songs=mycursor.fetchall()
    print(songs)
    return render_template('playlist.html',songs=songs)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="911Apexpredator"
)

if mydb.is_connected():
    print("Connection Established")
    mycursor = mydb.cursor()
    mydb.commit()
    

@app.route('/api/search', methods=['GET', 'POST'])
def search():
   
    query = request.args.get('q')
    results = spotify.Playlist(query)
    events=ticketmaster.events(query)
    if len(results)==0:
        results=["OOPS, NO SONGS FOUND"]
    if len(events)==0:
        events=["OOPS, NO EVENTS FOUND"]
    return jsonify(["Here are the songs:"]+[" "]+results+[" "]+["Here are the events:"]+[" "]+events)

@app.route('/add/song',methods=['POST','GET'])
def add():
    song=request.args.get('s')
    email=session.get('email')
    mycursor.execute("SELECT user_id FROM MusicApp.users WHERE email = '{0}'".format(email))
    uid= mycursor.fetchone()
    uid_int=uid[0]
    mycursor.execute('''INSERT INTO MusicApp.playlist (song_name, user_id) VALUES (%s, %s)''', (song, uid_int))
    mydb.commit()
    return "Song added successfully!"



if __name__ == '__main__':
    app.run(debug=True)
