from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field

from schema.schema_constants import PyObjectId


class BookmarkModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_oid: ObjectId = Field(...)
    content_oid: ObjectId = Field(...)
    content_type: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "user_oid": "user_oid",
                "content_oid": "content_oid",
                "content_type": "content_type",
                "created_at": "2024-04-04T08:00:00",
                "updated_at": "2024-04-04T08:00:00",
            }
        },
    )
