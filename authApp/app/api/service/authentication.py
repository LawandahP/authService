from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Optional
from pydantic import ValidationError
from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta
from pydantic import EmailStr  

from app.api.service.dependencies import is_user_present
from app.core.config import SECRET_KEY, JWT_ALGORITHM, JWT_AUDIENCE, JWT_TOKEN_PREFIX, ACCESS_TOKEN_EXPIRE_MINUTES
from app.schema.token import JWTMeta, JWTCreds, JWTPayload

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def verify_password(password: str, hashed_password: str):
  return pwd_context.verify(password, hashed_password)



class AuthException(BaseException):
    pass

class AuthService:

  def create_access_token_for_user(
    user,
    secret_key: str = str(SECRET_KEY),
    audience: str = JWT_AUDIENCE,
    expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES,
) -> str:

    # if not user or not isinstance(user, UserInDB):
    #     return None

    jwt_meta = JWTMeta(
        aud=audience,
        iat=datetime.timestamp(datetime.utcnow()),
        exp=datetime.timestamp(datetime.utcnow() + timedelta(minutes=expires_in)),
    )
    jwt_creds = JWTCreds(sub=user["email"])
    token_payload = JWTPayload(
        **jwt_meta.dict(),
        **jwt_creds.dict(),
    )
    access_token = jwt.encode(token_payload.dict(), secret_key, algorithm=JWT_ALGORITHM)
    return access_token
  
# Decode token and return user  
  def getCurrentUser(token: str = Depends(oauth2_scheme)) -> Optional[str]:
    try:
      decoded_token = jwt.decode(token, str(SECRET_KEY), audience=JWT_AUDIENCE, algorithms=[JWT_ALGORITHM])
      payload = JWTPayload(**decoded_token)

      # get all users(tenants)
      
      users = is_user_present("tenants")
      for user in users:
        if user["email"] == payload.sub:
          return user
      
    except (ExpiredSignatureError, JWTError, ValidationError):
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Could not validate token credentials.",
          headers={"WWW-Authenticate": "Bearer"},
      )

  # Get current active user
  def getCurrentActiveUser(current_user = Depends(getCurrentUser)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials or user inactive",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not current_user:
        raise credentials_exception
    if not current_user["is_active"]:
        raise credentials_exception
    return current_user
    
  # checks whether user is present in the database or not
  # uses

  def authenticate_user(email: EmailStr, password: str):
    users = is_user_present("tenants")
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