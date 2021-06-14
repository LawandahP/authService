from datetime import datetime
from typing import Optional
from pydantic import EmailStr, validator
import string
from app.schema.base import CoreModel




# class UserPublic(CoreModel):
#   id: Optional[int]
#   username: Optional[str]
#   full_name: Optional[str]
#   email: Optional[EmailStr]
#   is_active: bool = True
#   is_tenant: bool = True
#   phone_number: Optional[str]
#   created_at: Optional[datetime]
#   updated_at: Optional[datetime]

 