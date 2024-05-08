from fastapi import Depends
from feeds.repositories.feeds_repository import FeedRepository
from config.mongodb import feeds_collection


feeds_repository = FeedRepository(feeds_collection)


async def get_feeds():
    return await feeds_repository.get_feeds()
