# Playlist Backend

## Setup

**Python version**: 3.10

Create a virtual environment and activate it.

```
$ python -m venv venv
$ source ./venv/bin/activate
```

Install required packages.

```
$ pip install -r ./requirements.txt
```

## App run

Bring the API up with the following command.

```
$ flask run
```

The application should be availble in `127.0.0.1:5000`.


## Sample cURL commands and responses

### Health check endpoint

`curl --location '127.0.0.1:5000/health'`

**Response**
```json
{
    "code": "health.check.success",
    "message": "Health check successful"
}
```

### Read all songs paginated

`curl --location '127.0.0.1:5000/songs?pageSize=1&pageNo=2'`

**Response**
```json
{
    "code": "songs.read.success",
    "data": [
        {
            "acousticness": 0.1,
            "danceability": 0.762,
            "duration_ms": 243324,
            "energy": 0.594,
            "index": 5,
            "instrumentalness": 0.0,
            "key": 0,
            "liveness": 0.123,
            "loudness": -5.465,
            "mode": 1.0,
            "num_bars": 97,
            "num_sections": 10,
            "num_segments": 908,
            "song_class": 1,
            "song_id": "7kcCB7oh6X4bSoFCvrHLvG",
            "tempo": 98.025,
            "time_signature": 4,
            "title": "24/7",
            "valence": 0.337
        }
    ],
    "message": "Songs read successfully"
}
```


### Read song by title

`curl --location '127.0.0.1:5000/song?title=24K%20Magic'`

**Response**
```json
{
    "code": "song.read.success",
    "data": {
        "acousticness": 0.034,
        "danceability": 0.818,
        "duration_ms": 225983,
        "energy": 0.803,
        "index": 6,
        "instrumentalness": 0.0,
        "key": 1,
        "liveness": 0.153,
        "loudness": -4.282,
        "mode": 1.0,
        "num_bars": 101,
        "num_sections": 9,
        "num_segments": 966,
        "song_class": 1,
        "song_id": "6b8Be6ljOzmkOmFslEb23P",
        "tempo": 106.97,
        "time_signature": 4,
        "title": "24K Magic",
        "valence": 0.632
    },
    "message": "Song read successfully"
}
```
