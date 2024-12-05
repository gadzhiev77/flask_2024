from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index/")
def index():
    return '<h1>Hello world!</h>'

@app.route("/albums/<album_number>/<song_number>")
def song(album_number, song_number):
    return f"The {album_number} album and {song_number} musican performer"

if __name__ == '__main__':
    app.run()

