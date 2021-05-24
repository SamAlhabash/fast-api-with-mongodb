from bson import ObjectId
from pydantic.fields import Field
from pydantic.main import BaseModel
from fastapi.encoders import jsonable_encoder
from ..helpers.object_id_helper import str_object_id


class BaseID(BaseModel):
    id: str = Field(default_factory=str_object_id, alias="_id")

    class Config:
        allow_population_by_field_name = True
