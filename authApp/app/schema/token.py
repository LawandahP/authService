from datetime import datetime, timedelta
from typing import List, Optional
from pydantic import EmailStr
from app.core.config import JWT_AUDIENCE, ACCESS_TOKEN_EXPIRE_MINUTES
from app.schema.base import CoreModel


class JWTMeta(CoreModel):
  iss: str = "kgHomes.io"
  aud: str = JWT_AUDIENCE
  iat: float = datetime.timestamp(datetime.utcnow())
  exp: float = datetime.timestamp(datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

class JWTCreds(CoreModel):
  # How we'll identify users
  sub: EmailStr
  scopes: List[str] = []
  # username: str

class JWTPayload(JWTMeta, JWTCreds):
  
  # JWT Payload right before it's encoded - combine meta and username
  
  pass

class AccessToken(CoreModel):
  access_token: str
  token_type: str


  