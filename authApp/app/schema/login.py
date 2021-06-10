from pydantic import EmailStr, validator
import string
from app.schema.base import CoreModel


def validate_password(password: str) -> str:
  allowed = string.ascii_letters + string.digits + "-" + "_"
  assert all(char in allowed for char in password), "Invalid characters in username."
  assert len(password) >= 6, "Password must be 6 characters or more."
  return password


class UserLogin(CoreModel):
  email: EmailStr
  password: str

  @validator("password", pre=True)
  def username_is_valid(cls, password: str) -> str:
    return validate_password(password)