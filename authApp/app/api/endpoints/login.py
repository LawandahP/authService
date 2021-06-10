from app.api.crudUtils.authentication import AuthService
from app.schema.token import AccessToken
from fastapi import APIRouter, Request
from pydantic import EmailStr
from app.api.service.users import is_user_present
from app.schema.login import UserLogin
from fastapi.security import OAuth2PasswordBearer


api = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')




# @app.post("/login", response_model=UserPublic)
# async def tenantLogin(login: UserLogin):
#     user = await tenant.authenticate_user(email=login.email, password=login.pas>
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Authentication was unsuccessful.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     return user


# async def authenticate_user(email: EmailStr, password: str):
# user = await read_user_by_email(email)
# if not user:
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"no user with email: {email} found"
#     )
# if not verify_password(password=password, hashed_password=user.password):
#     raise HTTPException(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         detail="Incorrect Password. Please Try Again"
#     )
# return user



@api.post("/auth/token")
async def generateLoginToken(request: Request):
  get_data = request.json()
  print(get_data)
  access_token = AccessToken(access_token=AuthService.create_access_token_for_user(user=get_data), token_type="bearer")
  return access_token