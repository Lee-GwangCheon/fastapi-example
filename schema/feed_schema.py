from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from schema.schema_constants import PyObjectId


class ImageModel(BaseModel):
    width: int
    height: int
    url: str
    media_type: str


class FeedModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_oid: str = Field(..., description="User OID for referencing the related user.")
    author_name: str = Field(...)
    author_tag_name: str = Field(...)
    text: str = Field(...)
    images: List[ImageModel]
    hashtags: List[str]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "user_oid": "123456789abcdef",
                "author_name": "Jane Doe",
                "author_tag_name": "jane_doe",
                "text": "text",
                "images": [
                    {
                        "width": 1920,
                        "height": 1080,
                        "url": "https://example.com/image.jpg",
                        "media_type": "image/jpeg",
                    }
                ],
                "hashtags": ["#example"],
                "created_at": "2024-04-04T08:00:00",
                "updated_at": "2024-04-04T08:00:00",
            }
        },
    )
