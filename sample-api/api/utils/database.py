from motor.motor_asyncio import AsyncIOMotorClient

async def get_db():
    uri = "mongodb://academia:academia@172.17.0.2:27017"
    client = AsyncIOMotorClient(uri)

    return client.academia