from http import HTTPStatus

from flask import Blueprint
from flask import jsonify
from flask import request

from services import read_songs


bp = Blueprint(__name__, "apis")


@bp.get("/health", strict_slashes=False)
def api_health_check():
    result = {
        "message": "Health check successful",
        "code": "health.check.success",
    }
    response = jsonify(result)
    response.status = HTTPStatus.OK
    return response


@bp.get("/songs", strict_slashes=False)
def api_read_songs():
    page_size = int(request.args.get("pageSize", 10))
    page_no = int(request.args.get("pageNo", 1))

    songs = read_songs(page_size, page_no)

    result = {
        "message": "Songs read successfully",
        "code": "songs.read.success",
        "data": songs
    }
    response = jsonify(result)
    response.status = HTTPStatus.OK
    return response
