from extensions import ORMBase


def convert_model_to_dict(model: ORMBase) -> dict:
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}
