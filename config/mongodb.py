from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import setting


mongodb_client = AsyncIOMotorClient(setting.mongodb_url)
sereal_database = mongodb_client.get_database("seereal")
