from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class ORMBase(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=ORMBase)
