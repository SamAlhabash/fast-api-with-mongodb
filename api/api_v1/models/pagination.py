from pydantic.main import BaseModel


class Pagination(BaseModel):

    """
    A class that provides basic pagination parameters to include in HTTP response.
    """

    total_count: int
    page_size: int
    total_pages: int
    current_page: int
