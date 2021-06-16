from fastapi.security import(
  OAuth2PasswordRequestForm,
  SecurityScopes
)
from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import EmailStr
from starlette import status
import os

# from app.schema.login import UserPublic
# from app.schema.login import UserLogin
from app.api.service.authentication import AuthService
from app.schema.token import AccessToken
from app.core.config import SECRET_KEY



api = APIRouter()


@api.post("/auth/login", response_model=AccessToken, name="Generate token on successfull sign in")
async def generateLoginToken(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
  user = AuthService.authenticate_user(email=form_data.username, password=form_data.password)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"email not found"
  )
  # if not user:
  #     raise HTTPException(
  #         status_code=status.HTTP_401_UNAUTHORIZED,
  #         detail="Authentication was unsuccessful.",
  #         headers={"WWW-Authenticate": "Bearer"},
  #     )
  access_token = AccessToken(access_token=AuthService.create_access_token_for_user(user=user), token_type="bearer")
  return access_token



@api.post("/getCurrentUser", name="verify token")
async def getCurrentUser(current_user = Depends(AuthService.getCurrentActiveUser)):
  return current_user

# @api.post("/logout")
# async def logout():
#   pass