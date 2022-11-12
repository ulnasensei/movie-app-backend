from flask import Flask, request
from flask_cors import CORS
from tmdb import get_details, get_trending, get_search_result

#* initialize flask app
app = Flask(__name__)

#* allow cross-origin requests
CORS(app)

@app.route("/")
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

@app.route("/search")
def search():
    media_type = request.args.get("type", default="movie", type=str)
    query = request.args.get("query", default="Back to the future", type=str)
    result = get_search_result(media_type, query)
    return result

def main():
    app.run()


if __name__ == "__main__":
    main()