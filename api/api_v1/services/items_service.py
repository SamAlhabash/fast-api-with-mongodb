from api.api_v1.models.core_models.paginated_list import PaginatedList
from api.api_v1.models.core_models.pagination import Pagination
from motor.motor_asyncio import AsyncIOMotorCollection
from math import floor
from ..models.item import Item, ItemToReturn, ItemQueryParams, PutItem
from ..helpers.object_id_helpers import to_json_with_ID
from pymongo.results import UpdateResult
from fastapi.encoders import jsonable_encoder


async def get_all_items(db: AsyncIOMotorCollection, query: ItemQueryParams) -> PaginatedList[ItemToReturn]:

    items_list = await db.find({"is_deleted": False}).skip((query.page_number-1)*query.page_size).limit(query.page_size).to_list(length=1000)
    total_count = await db.count_documents({"is_deleted": False})

    total_pages = get_total_pages(total_count, query.page_size)

    pagination = Pagination(total_count=total_count, total_pages=total_pages,
                            page_size=query.page_size, current_page=query.page_number)

    return PaginatedList(list=items_list, pagination=pagination)


async def create_item(db: AsyncIOMotorCollection, item: Item) -> ItemToReturn:

    result = await db.insert_one(to_json_with_ID(item))
    inserted_item = await db.find_one({"_id": str(result.inserted_id), "is_deleted": False})

    return inserted_item


async def get_item_by_id(db: AsyncIOMotorCollection, id: str) -> ItemToReturn:

    return await db.find_one({"_id": id, "is_deleted": False})


async def put_item(db: AsyncIOMotorCollection, id: str, item: Item) -> UpdateResult:
    item = jsonable_encoder(item)
    return await db.update_one({"_id": id, "is_deleted": False}, {"$set": item})


async def patch_item(db: AsyncIOMotorCollection, id: str, item: PutItem) -> UpdateResult:
    item_dict = item.dict(exclude_unset=True)
    return await db.update_one({"_id": id, "is_deleted": False}, {"$set": item_dict})


async def delete_item(db: AsyncIOMotorCollection, id: str) -> UpdateResult:
    return await db.update_one({"_id": id}, {"$set": {'is_deleted': True}})


def get_total_pages(total_count: int, page_size: int) -> int:
    return total_count / page_size if \
        floor(total_count / page_size) == (total_count / page_size) \
        else floor(total_count / page_size) + 1
