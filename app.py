from flask import Flask, jsonify, request
import spotify

app = Flask(__name__)

@app.route('/api/search')
def search():
    query = request.args.get('q')
    results = spotify.Playlist(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
