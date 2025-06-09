from fastapi import APIRouter,status
from database import engine
from sqlalchemy.orm import Session



order_router=APIRouter(
    prefix='/orders',
    tags=["orders"]
)


session = Session(bind=engine)



@order_router.get('/')
async def hello():
    return {"message":"Hello I am order router"}


