from flask import Flask, jsonify, request, render_template
import spotify
import ticketmaster
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main.html',  artiststuff= "")

@app.route('/api/search', methods=['GET', 'POST'])
def search():
   
    query = request.args.get('q')
    results = spotify.Playlist(query)
    events=ticketmaster.events(query)
    print(results)
    print(events)
    return jsonify(["Here are the songs:"]+[" "]+results+[" "]+["Here are the events:"]+[" "]+events)

if __name__ == '__main__':
    app.run()
