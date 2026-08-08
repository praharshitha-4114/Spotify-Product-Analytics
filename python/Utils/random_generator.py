import random

from python.constants.genres import GENRES
from python.constants.languages import LANGUAGES
from python.constants.song_titles import SONG_TITLES


def random_genre():
    return random.choice(GENRES)


def random_language():
    return random.choice(LANGUAGES)


def random_song():
    return random.choice(SONG_TITLES)