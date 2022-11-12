from flask import Flask, request
from flask_cors import CORS
from tmdb import get_details, get_trending

#* initialize flask app
app = Flask(__name__)

#* allow cross-origin requests
CORS(app)

@app.route("/trending")
def trending():
    media_type = request.args.get("type", default="movie", type=str)

    result = get_trending(media_type)
    return result

@app.route("/details")
def details():
    media_type = request.args.get("type", default="movie", type=str)
    media_id = request.args.get("id", default=505642, type=int)
    result = get_details(media_type, media_id)
    return result


def main():
    app.run()


if __name__ == "__main__":
    main()