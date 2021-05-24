from api.api_v1.models.core_models.paginated_list import PaginatedList
from api.api_v1.models.core_models.pagination import Pagination
from motor.motor_asyncio import AsyncIOMotorCollection
from math import floor
from ..models.item import Item, ItemSchema, ItemQueryParams
from ..helpers.object_id_helpers import to_json_with_ID


async def get_all_items(db: AsyncIOMotorCollection, query: ItemQueryParams) -> PaginatedList[ItemSchema]:

    items_list = await db.find().skip((query.page_number-1)*query.page_size).limit(query.page_size).to_list(length=1000)
    total_count = await db.count_documents({})

    total_pages = get_total_pages(total_count, query.page_size)

    pagination = Pagination(total_count=total_count, total_pages=total_pages,
                            page_size=query.page_size, current_page=query.page_number)

    return PaginatedList(list=items_list, pagination=pagination)


async def create_item(db: AsyncIOMotorCollection, item: Item) -> ItemSchema:

    result = await db.insert_one(to_json_with_ID(item))
    inserted_item = await db.find_one({"_id": str(result.inserted_id)})

    return inserted_item


async def get_item_by_id(db: AsyncIOMotorCollection, id: str) -> ItemSchema:

    return await db.find_one({"_id": id})

    # TODO
    # Replace Item Function here


def get_total_pages(total_count: int, page_size: int) -> int:
    return total_count / page_size if \
        floor(total_count / page_size) == (total_count / page_size) \
        else floor(total_count / page_size) + 1
