from fastapi import FastAPI
from app.routers.home import home_router 


app = FastAPI()

app.include_router(router=home_router)