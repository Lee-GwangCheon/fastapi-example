from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from schema.schema_constants import PyObjectId


class UserModel(BaseModel):
    """
    single user record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    tag_name: str = Field(...)
    profile_img: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "tag_name": "johnny",
                "profile_img": "https://url.com",
                "created_at": "2024-04-04T08:00:00",
                "updated_at": "2024-04-04T08:00:00",
            }
        },
    )
