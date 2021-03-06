from pydantic import BaseModel, Field
from .core_models.base import BaseID
from typing import Optional
from fastapi import Query


class Item(BaseModel):
    message: str = Field(..., min_length=1, max_length=100)
    second_message: Optional[str] = Field("No message was entered")


class ItemToReturn(BaseID, Item):
    pass


class ItemSchema(ItemToReturn):
    is_deleted: Optional[bool] = Field(False)
    """
    Item with ID. Represents Item in DB.
    """


class PutItem(BaseModel):
    message: Optional[str] = Field(min_length=1, max_length=100)
    second_message: Optional[str] = Field()


class ItemQueryParams:
    def __init__(self,
                 page_number: Optional[int] = Query(default=1, ge=1),
                 page_size: Optional[int] = Query(default=25, le=1000)) -> None:

        self.page_number = page_number
        self.page_size = page_size
