from fastapi.encoders import jsonable_encoder
from api.api_v1.models.core_models.paginated_list import PaginatedList
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi.params import Depends, Body
from api.api_v1.services.database import get_db
import api.api_v1.services.items_service as item_service
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.api_v1.models.item import Item, ItemSchema, ItemQueryParams, PutItem
from api.api_v1.helpers.http_detail_messages_helper import not_found_message
from api.api_v1.helpers.patch_helper import remove_all_none_from_dict


router = APIRouter()


@router.get("/", response_model=PaginatedList[ItemSchema], summary="Get all Items")
async def get_all(db: AsyncIOMotorDatabase = Depends(get_db), query: ItemQueryParams = Depends()):

    return await item_service.get_all_items(db=db['items'], query=query)


@router.get("/{id}", response_model=ItemSchema, summary="Get one item by ID")
async def get_one(id: str, db: AsyncIOMotorDatabase = Depends(get_db)):

    item = await item_service.get_item_by_id(db['items'], id)

    if item is not None:
        return item

    raise HTTPException(404, detail=not_found_message(id, 'Item'))


@router.post("/", status_code=201, response_model=ItemSchema, summary="Create new item")
async def post(db: AsyncIOMotorDatabase = Depends(get_db), item: Item = Body(...)):

    inserted_item = await item_service.create_item(db['items'], item)
    return inserted_item


@router.put("/{id}", status_code=204, summary="Replace existing item")
async def put(id: str, db: AsyncIOMotorDatabase = Depends(get_db), item: Item = Body(...)):

    updated_result = await item_service.put_item(db['items'], id, item)

    if updated_result.matched_count == 0:
        raise HTTPException(
            404, detail=not_found_message(id, 'Item'))

    if updated_result.modified_count == 0:
        raise HTTPException(
            400, detail="Unknown error occured. Please make sure the update you have requested is not already implemented.")

    return


@router.patch("/{id}", summary="Partially update an item.", response_model=ItemSchema)
async def patch(id: str, db: AsyncIOMotorDatabase = Depends(get_db), item: PutItem = Body(...)):

    updated_result = await item_service.patch_item(db['items'], id, item)

    if updated_result.matched_count == 0:
        raise HTTPException(
            404, detail=not_found_message(id, 'Item'))

    if updated_result.modified_count == 0:
        raise HTTPException(
            400, detail="Unknown error occured. Please make sure the update you have requested is not already implemented.")

    return await item_service.get_item_by_id(db['items'], id)
