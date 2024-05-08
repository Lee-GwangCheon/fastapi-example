from motor.motor_asyncio import AsyncIOMotorCollection


class FeedRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def get_feeds(self):
        pipeline = [
            {
                "$lookup": {
                    "from": "users",
                    "localField": "user_oid",
                    "foreignField": "_id",
                    "as": "user_info",
                }
            },
            {"$unwind": "$user_info"},
            {
                "$lookup": {
                    "from": "reactions",
                    "localField": "_id",
                    "foreignField": "content_oid",
                    "as": "reactions",
                }
            },
            {
                "$addFields": {
                    "reactions": {
                        "$filter": {
                            "input": "$reactions",
                            "as": "reaction",
                            "cond": {"$eq": ["$$reaction.content_type", "feed"]},
                        }
                    }
                }
            },
            {
                "$lookup": {
                    "from": "bookmarks",
                    "localField": "_id",
                    "foreignField": "content_oid",
                    "as": "bookmarks",
                }
            },
            {
                "$addFields": {
                    "bookmarks": {
                        "$filter": {
                            "input": "$bookmarks",
                            "as": "bookmarks",
                            "cond": {"$eq": ["$$bookmarks.content_type", "feed"]},
                        }
                    }
                }
            },
        ]
        documents = await self.collection.aggregate(pipeline).to_list(None)
        return documents
