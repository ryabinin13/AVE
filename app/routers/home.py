from fastapi import APIRouter, Depends, HTTPException
from app.schemas.data import AddDataSchema
from app.dependencies import get_home_service
from app.services.home import HomeService


home_router = APIRouter()

@home_router.post('/data')
async def write_data(
    add_data_schema: AddDataSchema,
    home_service: HomeService = Depends(get_home_service)
    ):
    return await home_service.add_data(add_data_schema=add_data_schema)


@home_router.get('/data')
async def check_data(
    phone: str,
    home_service: HomeService = Depends(get_home_service)
    ):
    try:   
        return await home_service.get_address(phone=phone)
    except ValueError:
        raise HTTPException(status_code=401, detail='Номер телефона должен начинаться с "+" и содержать 11 цифр')

