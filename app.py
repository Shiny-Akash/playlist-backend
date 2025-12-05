from flask import Flask

from api import bp
from extensions import db


app = Flask(__name__)

app.register_blueprint(bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

with app.app_context():
    db.init_app(app)
    db.create_all()
