import json

from models import Song
from extensions import db
from utils import convert_model_to_dict


def init_songs_tbl():
    with open("data/playlist.json", "r") as f:
        data = json.load(f)

    songs = []
    for idx in data["id"].keys():
        # Check if this entry already exists in DB
        song = Song.read_by_index(idx)
        if song is not None:
            continue

        song = Song()
        song.index = int(idx)
        song.song_id = data["id"][idx]
        song.title = data["title"][idx]
        song.danceability = data["danceability"][idx]
        song.energy = data["energy"][idx]
        song.key = data["key"][idx]
        song.loudness = data["loudness"][idx]
        song.mode = data["mode"][idx]
        song.acousticness = data["acousticness"][idx]
        song.instrumentalness = data["instrumentalness"][idx]
        song.liveness = data["liveness"][idx]
        song.valence = data["valence"][idx]
        song.tempo = data["tempo"][idx]
        song.duration_ms = data["duration_ms"][idx]
        song.time_signature = data["time_signature"][idx]
        song.num_bars = data["num_bars"][idx]
        song.num_sections = data["num_sections"][idx]
        song.num_segments = data["num_segments"][idx]
        song.song_class = data["class"][idx]

        songs.append(song)

    if len(songs) == 0:
        return

    db.session.add_all(songs)
    db.session.commit()


def read_songs(page_size: int, page_no: int) -> list[Song]:
    songs = Song.read_paginated(page_size, page_no)
    songs = [convert_model_to_dict(song) for song in songs]

    return songs
