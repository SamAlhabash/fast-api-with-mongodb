

from pydantic.main import BaseModel


class Pagination(BaseModel):

    total_count : int
    page_size : int 
    total_pages: int
    current_page: int

    # def __init__(self, total_count: int, page_size: int, total_pages: int, current_page: int) -> None:
    #     self.total_count = total_count
    #     self. page_size = page_size
    #     self.total_pages = total_pages
    #     self.current_page = current_page


class testPagination(BaseModel):
    total_count: int 
    page_size: int 
    total_pages: int 
    current_page: int 
