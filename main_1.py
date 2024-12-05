from flask import Flask

app = Flask(__name__)

@app.route("/albums/<album_number>")
def albums(album_number):
    return "The {} album".format((album_number))

if __name__ == '__main__':
    app.run()