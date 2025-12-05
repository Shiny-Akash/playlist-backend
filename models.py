from __future__ import annotations

from typing import Optional

from sqlalchemy import Column
from sqlalchemy import BIGINT
from sqlalchemy import VARCHAR
from sqlalchemy import DOUBLE
from sqlalchemy.orm import Session
from sqlalchemy import select

from extensions import db


class Song(db.Model):

    index = Column(
        "index",
        BIGINT,
        primary_key=True,
    )

    song_id = Column(
        "song_id",
        VARCHAR(255),
    )

    title = Column(
        "title",
        VARCHAR(255),
    )

    danceability = Column(
        "danceability",
        DOUBLE,
    )

    energy = Column(
        "energy",
        DOUBLE,
    )

    key = Column(
        "key",
        BIGINT,
    )

    loudness = Column(
        "loudness",
        DOUBLE,
    )

    mode = Column(
        "mode",
        DOUBLE,
    )

    acousticness = Column(
        "acousticness",
        DOUBLE,
    )

    instrumentalness = Column(
        "instrumentalness",
        DOUBLE,
    )

    liveness = Column(
        "liveness",
        DOUBLE,
    )

    valence = Column(
        "valence",
        DOUBLE,
    )

    tempo = Column(
        "tempo",
        DOUBLE,
    )

    duration_ms = Column(
        "duration_ms",
        BIGINT,
    )

    time_signature = Column(
        "time_signature",
        BIGINT,
    )

    num_bars = Column(
        "num_bars",
        BIGINT,
    )

    num_sections = Column(
        "num_sections",
        BIGINT,
    )

    num_segments = Column(
        "num_segments",
        BIGINT,
    )

    song_class = Column(
        "song_class",
        BIGINT,
    )

    @classmethod
    def read_by_index(cls, db_sess: Session, index: int) -> Optional[Song]:
        filter_cond = cls.index == index
        query = select(cls).where(filter_cond)

        result = db_sess.execute(query).scalar_one_or_none()
        return result
