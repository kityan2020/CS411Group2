from flask import Flask, jsonify, request,url_for, redirect, render_template
import spotify
import ticketmaster
import json
import mysql.connector
#Kits SQL Password = 911Apexpredator
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get the username and password from the form data
        username = request.form['username']
        password = request.form['password']
        # check if the username and password are correct (replace this with your own authentication logic)
        if username == 'admin' and password == 'password':
            # if the login is successful, redirect to the main page
            return redirect(url_for('Main.HTML'))
        else:
            # if the login is not successful, redirect back to the login page with an error message
            return render_template('login.html', error='Invalid username or password')

    # if the request method is GET, render the login page
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('Main.html',  artiststuff= "")

@app.route('/playlist')
def displaypl():
    return render_template('playlist.html')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="911Apexpredator"
)

if mydb.is_connected():
    print("Connection Established")
    mycursor = mydb.cursor()


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

    mycursor.execute('''INSERT INTO MusicApp.playlist (song_name, user_id) VALUES (%s, %s)''', (song, 1))
    mydb.commit()
    return "Song added successfully"



if __name__ == '__main__':
    app.run()
