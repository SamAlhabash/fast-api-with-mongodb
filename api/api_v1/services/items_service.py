from motor.motor_asyncio import AsyncIOMotorCollection
from math import floor


async def get_all_items(db: AsyncIOMotorCollection, page_size: int = 25, page_number: int = 1):
    items_list = await db.find().skip((page_number-1)*page_size).limit(page_size).to_list(length=1000)
    total_count = await db.count_documents({})
    total_pages = total_count / \
        page_size if floor(
            total_count / page_size) == (
            total_count / page_size) else floor(total_count / page_size) + 1
    return {
        'item_list': items_list,
        'pagination': {
            "total_count": total_count,
            "total_pages": total_pages
        }
    }
