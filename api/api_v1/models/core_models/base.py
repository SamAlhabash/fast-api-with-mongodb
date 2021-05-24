from pydantic.fields import Field
from pydantic.main import BaseModel
from ...helpers.object_id_helpers import str_object_id


class BaseID(BaseModel):

    """
    Base class for any model that requires a mongoDB ID.
    """
    id: str = Field(default_factory=str_object_id, alias="_id")

    class Config:
        allow_population_by_field_name = True
