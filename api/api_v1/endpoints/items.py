from api.api_v1.models.paginated_list import PaginatedList
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi.params import Depends, Body
from api.api_v1.services.database import get_db
import api.api_v1.services.items_service as item_service
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.api_v1.models.item import ItemBase,Item, ItemQueryParams
from api.api_v1.helpers.not_found_helper import not_found_message

router = APIRouter()


@router.get("/{id}", response_model=Item)
async def get_item(id: str, db: AsyncIOMotorDatabase = Depends(get_db)):

    item = await item_service.get_item_by_id(db['items'], id)

    if item is not None:
        return item

    raise HTTPException(404, detail=not_found_message(id, 'Item'))


@router.get("/", response_model=PaginatedList)
async def get_all_items(db: AsyncIOMotorDatabase = Depends(get_db), query: ItemQueryParams = Depends()):

    return await item_service.get_all_items(db=db['items'], query=query)


@router.post("/", status_code=201, response_model=Item)
async def post_item(db: AsyncIOMotorDatabase = Depends(get_db), item: ItemBase = Body(...)):

    inserted_item = await item_service.create_item(db['items'], item)
    return inserted_item


@router.put("/{id}", status_code=200)
async def post_item(id: str, db: AsyncIOMotorDatabase = Depends(get_db), item: ItemBase = Body(...)):

    item = jsonable_encoder(item)

    updated_result = await db['items'].update_one({"_id": id}, {"$set": item})

    if updated_result.matched_count == 0:
        raise HTTPException(
            404, detail=not_found_message(id, 'Item'))

    if updated_result.modified_count == 0:
        raise HTTPException(400, detail="Unknown error occured")
