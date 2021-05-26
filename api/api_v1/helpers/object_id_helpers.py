from fastapi.encoders import jsonable_encoder
from bson import ObjectId


def to_json_with_ID(obj: object) -> dict:
    obj = jsonable_encoder(obj)
    obj["_id"] = str(ObjectId())
    obj["is_deleted"] = False
    return obj


def str_object_id() -> str:
    return str(ObjectId())
