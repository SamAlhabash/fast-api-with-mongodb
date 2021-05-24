from api.api_v1.models.paginated_list import PaginatedList
from api.api_v1.models.pagination import Pagination
from motor.motor_asyncio import AsyncIOMotorCollection
from math import floor
from ..models.item import ItemIn, ItemInDb, ItemQueryParams


async def get_all_items(db: AsyncIOMotorCollection, query: ItemQueryParams):
    items_list = await db.find().skip((query.page_number-1)*query.page_size).limit(query.page_size).to_list(length=1000)
    total_count = await db.count_documents({})
    total_pages = total_count / \
        query.page_size if floor(
            total_count / query.page_size) == (
            total_count / query.page_size) else floor(total_count / query.page_size) + 1

    pagination = Pagination(total_count=total_count, total_pages=total_pages,
                            page_size=query.page_size, current_page=query.page_number)
    return PaginatedList(list=items_list, pagination=pagination)


async def create_item(db: AsyncIOMotorCollection, item: ItemIn) -> ItemInDb:
    result = await db.insert_one(item.to_json_with_id())
    inserted_item = await db.find_one({"_id": str(result.inserted_id)})

    return inserted_item

async def get_item_by_id(db: AsyncIOMotorCollection, id: str) -> ItemInDb:
    item = await db.find_one({"_id": id})
    return item

    #TODO 
    # Replace Item Function here