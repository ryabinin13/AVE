from app.cache.accessor import get_redis_connection
from app.repositories.data import DataRepository
from app.services.home import HomeService


async def get_data_repository() -> DataRepository:
    redis_conn = await get_redis_connection()
    return DataRepository(redis_connection=redis_conn)

async def get_home_service() -> HomeService:
    data_repository = await get_data_repository()
    return HomeService(data_repository=data_repository)