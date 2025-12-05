from http import HTTPStatus

from flask import Blueprint
from flask import jsonify


bp = Blueprint(__name__, "apis")


@bp.route("/health", strict_slashes=False)
def healt_check():
    result = {
        "message": "Health check successful",
        "code": "health.check.success",
    }
    response = jsonify(result)
    response.status = HTTPStatus.OK
    return response
