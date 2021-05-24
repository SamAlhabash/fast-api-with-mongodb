from api.api_v1.models.item import Item
from pydantic.main import BaseModel
from api.api_v1.models.pagination import Pagination


class PaginatedList(BaseModel):

    list: list[Item]
    pagination: Pagination

    
    # def __init__(self,  pagination: Pagination, list: list = None, list_name: str = "list", **kwargs) -> None:

    #     setattr(self, list_name, list)

    #     for key, value in kwargs:
    #         setattr(self, key, value)

    #     self.pagination = pagination

    
