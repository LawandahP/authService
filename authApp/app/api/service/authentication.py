from jose import jwt
from datetime import datetime, timedelta  

from app.core.config import SECRET_KEY, JWT_ALGORITHM, JWT_AUDIENCE, JWT_TOKEN_PREFIX, ACCESS_TOKEN_EXPIRE_MINUTES
from app.schema.token import JWTMeta, JWTCreds, JWTPayload

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_password: str):
  return pwd_context.verify(password, hashed_password)



class UserInDB:
  pass


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