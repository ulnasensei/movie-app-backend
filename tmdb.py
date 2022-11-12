import requests
from dotenv import load_dotenv
import os

#* get tmdb api key and base endpoint
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_API_URL_BASE = os.getenv("TMDB_API_URL_BASE")

def get_trending(media_type:str):
    request_url = f'{TMDB_API_URL_BASE}/trending/{media_type}/week?api_key={TMDB_API_KEY}'
    result = requests.get(request_url)
    return result.json()

def get_details(media_type:str, media_id:int):
    request_url = f'{TMDB_API_URL_BASE}/{media_type}/{media_id}?api_key={TMDB_API_KEY}&language=en-US'
    result = requests.get(request_url)
    return result.json()