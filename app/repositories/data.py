import redis.asyncio as redis


class DataRepository:
    def __init__(self, redis_connection: redis.Redis):
        self.redis = redis_connection

    async def create(self, phone: str, address: str):
        await self.redis.set(phone, address)

    async def get_address(self, phone: str):
        return await self.redis.get(phone)

