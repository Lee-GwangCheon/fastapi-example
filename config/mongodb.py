from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)

from config.settings import setting


mongodb_client = AsyncIOMotorClient(setting.mongodb_url)
sereal_database: AsyncIOMotorDatabase = mongodb_client.get_database("seereal")
feeds_collection: AsyncIOMotorCollection = sereal_database.get_collection("feeds")
users_collection: AsyncIOMotorCollection = sereal_database.get_collection("users")
