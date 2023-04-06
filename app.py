<<<<<<< Updated upstream
from flask import Flask, jsonify, request
import spotify

app = Flask(__name__)

@app.route('/api/search')
def search():
=======

from flask import Flask, jsonify, request, render_template
import spotify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main.html',  artiststuff= "")

@app.route('/api/search', methods=['GET', 'POST'])
def search():
   
>>>>>>> Stashed changes
    query = request.args.get('q')
    results = spotify.Playlist(query)
    print(results)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
