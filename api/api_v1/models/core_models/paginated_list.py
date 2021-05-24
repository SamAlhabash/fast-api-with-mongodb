
from pydantic.generics import GenericModel
from api.api_v1.models.core_models.pagination import Pagination
from typing import Generic, TypeVar

T = TypeVar('T')


class PaginatedList(GenericModel, Generic[T]):

    """
    A class that provides a Paginated List Model to return in HTTP response.
    """

    list: list[T]
    pagination: Pagination
