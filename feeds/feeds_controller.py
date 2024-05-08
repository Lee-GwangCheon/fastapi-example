from bson import json_util
import json
from fastapi import APIRouter
from feeds import feeds_service

router = APIRouter(prefix="/feeds")


@router.get("/", tags=["feeds"])
async def get_feeds():
    documents = await feeds_service.get_feeds()
    response = json.loads(json_util.dumps(documents))
    return response
