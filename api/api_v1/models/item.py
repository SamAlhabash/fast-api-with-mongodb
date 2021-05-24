from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from .base import BaseClass, BaseIn, PyObjectId
from typing import Optional
from fastapi import Query
from bson import ObjectId
from fastapi.encoders import jsonable_encoder


class ItemInDb(BaseClass):
    message: str = Field(...)
    second_message: Optional[str] = Field("No message was entered")


class ItemIn(BaseIn):
    message: str = Field(..., min_length=1)
    second_message: Optional[str] = Field("No message was entered")

    


class ItemPut(BaseModel):
    message: str = Field(..., min_length=1)
    second_message: Optional[str] = Field(None)


class ItemPatch(BaseModel):
    message: Optional[str] = Field(None, min_length=1)
    second_message: Optional[str] = Field(None)


class ItemQueryParams:
    def __init__(self,
                 page_number: Optional[int] = Query(default=1, ge=1),
                 page_size: Optional[int] = Query(default=25, le=1000)) -> None:

        self.page_number = page_number
        self.page_size = page_size
