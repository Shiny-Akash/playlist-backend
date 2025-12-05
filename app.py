from flask import Flask

from api import bp
from extensions import db
from services import init_songs_tbl


app = Flask(__name__)

app.register_blueprint(bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

with app.app_context():
    db.init_app(app)
    db.create_all()

    init_songs_tbl()
