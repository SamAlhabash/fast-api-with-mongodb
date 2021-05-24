from fastapi.encoders import jsonable_encoder
from bson import ObjectId


def to_json_with_ID(obj: object) -> dict:
    obj = jsonable_encoder(obj)
    obj["_id"] = str(ObjectId())
    return obj
