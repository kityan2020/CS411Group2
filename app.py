from flask import Flask, jsonify, request, url_for, redirect, render_template
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
        # print(username,password)
        # check if the username and password are correct (replace this with your own authentication logic)
        mycursor.execute("SELECT password FROM MusicApp.users WHERE email = '{0}'".format(username))
        real_password= mycursor.fetchone()
        real_password_int=str(int(real_password[0]))
        # print(real_password,real_password_int,real_password_int==password)
        if real_password_int==password:
            # if the login is successful, redirect to the main page
            # print("redirect to main")
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
        return redirect(url_for('register'))
    mycursor.execute('''INSERT INTO MusicApp.users(email,password) VALUES (%s, %s)''', (email, password))
    mydb.commit()
    return render_template('Main.HTML')



@app.route('/playlist')
def displaypl():
    return render_template('playlist.html')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dd020912#"
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

    mycursor.execute('''INSERT INTO MusicApp.playlist (song_name, user_id) VALUES (%s, %s)''', (song, 1))
    mydb.commit()
    return "Song added successfully!"



if __name__ == '__main__':
    app.run(debug=True)
