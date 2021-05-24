from bson import ObjectId
from pydantic.main import BaseModel
from pydantic import Field
from fastapi.encoders import jsonable_encoder


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return ObjectId()

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class BaseClass(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

        


class BaseIn(BaseModel):


    def to_json_with_id(self):
        result = jsonable_encoder(self)
        result["_id"] = str(ObjectId())
        return result
