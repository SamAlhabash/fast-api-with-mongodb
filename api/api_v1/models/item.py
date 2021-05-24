from pydantic import BaseModel, Field
from .base import BaseID
from typing import Optional
from fastapi import Query


class ItemBase(BaseModel):
    message: str = Field(...,min_length=1, max_length= 100)
    second_message: Optional[str] = Field("No message was entered")

class Item(BaseID, ItemBase):
    pass

class ItemQueryParams:
    def __init__(self,
                 page_number: Optional[int] = Query(default=1, ge=1),
                 page_size: Optional[int] = Query(default=25, le=1000)) -> None:

        self.page_number = page_number
        self.page_size = page_size
