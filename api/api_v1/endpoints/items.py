from bson.objectid import ObjectId
from fastapi import APIRouter
from fastapi.datastructures import Default
from fastapi.param_functions import Query
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from starlette.responses import JSONResponse
from api.api_v1.services.database import get_db
import api.api_v1.services.items_service as item_service
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.api_v1.models.item import ItemInDb
from typing import Optional

router = APIRouter()


test_dict = {}
@router.get("/")
async def get_all_items(
    page_number: Optional[int] = Query(default=1, ge=1),
    page_size: Optional[int] = Query(default=25, le=1000),
    db: AsyncIOMotorDatabase = Depends(get_db)
):

    return await item_service.get_all_items(db = db['items'], page_number= page_number, page_size= page_size)


@router.post("/")
async def post(db: AsyncIOMotorDatabase = Depends(get_db)):
    items_db = db['items']
    item = jsonable_encoder(ItemInDb())
    print(item)
    await items_db.insert_one(item)
