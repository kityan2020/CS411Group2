from flask import Flask, jsonify, request, url_for, redirect, render_template, session
import spotify
import ticketmaster
import json
import mysql.connector
import os
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import secrets
import requests
import spotipy
#Kits SQL Password = 911Apexpredator

secret_key = secrets.token_hex(16)
print(secret_key)
app = Flask(__name__)
app.secret_key = secret_key
app.config['SESSION_COOKIE_NAME'] = 'Kits Cookie'
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@app.route('/login_function', methods=['GET', 'POST'])
def login_function():
    function_name = request.form['function']
    if function_name == 'login':
        return login()
    elif function_name == 'oauth':
        return oauth()
def login():
    if request.method == 'POST':
        # get the username and password from the form data
        username = request.form['username']
        password = request.form['password']
        if username=="" or password=="":
            return render_template('login.html', error1=True)
        else:# print(username,password)
            mycursor.execute("SELECT password FROM MusicApp.users WHERE email = '{0}'".format(username))
            real_password= mycursor.fetchone()
            real_password_int=str(int(real_password[0]))
        # print(real_password,real_password_int,real_password_int==password)
        if real_password_int==password:
            # if the passwords are the same, then login
            # print("redirect to main")
            session['email'] = username
            return render_template('Main.HTML')

        else:
            # if the login is not successful, redirect back to the login page with an error message
            return render_template('login.html', error2=True)

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
    if email=="" or password=="":
        return redirect(url_for('start'))
    mycursor.execute("SELECT email FROM MusicApp.users WHERE email = '{0}'".format(email))
    email= mycursor.fetchone()
    e=email[0]
    if e!=None:
        return render_template('register.html', error=True)
    mycursor.execute('''INSERT INTO MusicApp.users(email,password) VALUES (%s, %s)''', (email, password))
    mydb.commit()
    session['email'] = email
    return render_template('Main.HTML')

@app.route('/logout')
def logout():
    token_info = session.get('token_info')
    print("##########",token_info)
    if token_info:
        session.clear()
        print("session:",session)
     
    return render_template('login.html')

@app.route('/login')
def oauth():
    print('start oauth login')
    # session.clear()
    sp_oauth = create_spotify_oauth()
    author_url = sp_oauth.get_authorize_url()
    return redirect(author_url)

@app.route('/login')
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=url_for('callback',_external=True),
        scope="user-library-read",
        show_dialog=True
    )

@app.route('/switchtologin')
def switchtologin():
    return render_template('login.html')

@app.route('/callback')
def callback():
    sp_oauth=create_spotify_oauth()
    code = request.args.get('code')
    print(code)
    token = sp_oauth.get_access_token(code,check_cache=False)
    print(token,"token info added to session")
    session['token_info'] = token
    print("session:",session)
    if not token:
        return redirect('/login')
    else:
        spotify=spotipy.Spotify(auth=token['access_token'])
        user=spotify.current_user()
        userid=user['id']
        print("userid:",userid,type(userid))
    
        mycursor.execute("SELECT email FROM MusicApp.users WHERE email = '{0}'".format((userid),))
        e = mycursor.fetchone()
        print(e)
        if e == None:
            mycursor.execute('''INSERT INTO MusicApp.users(email, password) VALUES (%s,%s)''', ((userid),0))
            mydb.commit()
            session['email'] = str(userid)
        else:
            session['email'] = e[0]
        return render_template('Main.html')

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
    if song=="":
        return render_template('Main.html',error1=True)
    email=session.get('email')
    mycursor.execute("SELECT user_id FROM MusicApp.users WHERE email = '{0}'".format(email))
    uid= mycursor.fetchone()
    uid_int=uid[0]
    mycursor.execute('''INSERT INTO MusicApp.playlist (song_name, user_id) VALUES (%s, %s)''', (song, uid_int))
    mydb.commit()
    return render_template('Main.html',message1=True)



if __name__ == '__main__':
    app.run(debug=True)
