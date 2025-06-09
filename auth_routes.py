"""Defines authentication-related routes for the Pizza Delivery App."""
from fastapi import APIRouter,status
from schemas import SingUpModel
from models import User
from fastapi import HTTPException
from database import session,engine
from werkzeug.security import generate_password_hash, check_password_hash


auth_router=APIRouter(
    prefix='/auth',
    tags=['auth']
)


@auth_router.get('/')
async def hello():
    return {"message":"Hello world I will do it"}




@auth_router.post('/singup',response_model=SingUpModel,
        status_code=status.HTTP_201_CREATED
        )
async def signup(user:SingUpModel):
    db=session()
    db_email=db.query(User).filter(User.email==user.email).first()

    if db_email is not None: 
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                   detail="User with the email already exists"         
        )


    db_username=db.query(User).filter(User.username==user.username).first()

    if db_username is not None: 
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                   detail="User with the username already exists"         
        )
    

    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(str(user.password)),
        is_active=user.is_active,
        is_staff=user.is_staff

    )

    db.add(new_user)
    db.commit()

    return new_user

