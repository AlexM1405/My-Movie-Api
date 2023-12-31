from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()


@user_router.get('/login', tags=["auth"])
def login(user: User):
    if user.email == "alexm12@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content={"token": token, "message": "Login Successful"})