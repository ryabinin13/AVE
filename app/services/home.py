from app.repositories.data import DataRepository
from app.schemas.data import AddDataSchema
import re


class HomeService:
    def __init__(self, data_repository: DataRepository):
        self.data_repository = data_repository

    async def add_data(self, add_data_schema: AddDataSchema):
        phone = add_data_schema.phone
        address = add_data_schema.address
        return await self.data_repository.create(phone=phone, address=address)
    
    async def get_address(self, phone: str):
        if not re.match(r'^\+\d{11}$', phone):
            raise ValueError()
        address = await self.data_repository.get_address(phone=phone)
        return address