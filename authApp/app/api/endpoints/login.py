from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Request, HTTPException
from pydantic import EmailStr
from starlette import status
import os

from app.api.service.users import is_user_present
from app.schema.login import UserLogin
from app.api.service.authentication import AuthService, verify_password
from app.schema.token import AccessToken



api = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

# async def get_user_by_email():


async def authenticate_user(email: EmailStr, password: str):

  users = is_user_present("tenants")
  # print(users)
  
  for user in users:
    if user["email"] == email:
      if verify_password(password, user["password"]):
        print(user)
        return user
      else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect Password and or Email. Please Try Again"
      )
    

    


@api.post("/auth/login")
async def generateLoginToken(user: UserLogin):
  user = await authenticate_user(email=user.email, password=user.password)
  # if not user:
  #     raise HTTPException(
  #         status_code=status.HTTP_401_UNAUTHORIZED,
  #         detail="Authentication was unsuccessful.",
  #         headers={"WWW-Authenticate": "Bearer"},
  #     )
  access_token = AccessToken(access_token=AuthService.create_access_token_for_user(user=user), token_type="bearer")
  return access_token

