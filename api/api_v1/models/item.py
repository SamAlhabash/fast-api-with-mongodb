from pydantic import BaseModel, Field
from bson import ObjectId
from pydantic.utils import Obj
from .base import BaseClass


class ItemInDb(BaseClass):
    message: str = Field("no message was entered")
