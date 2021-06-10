from pydantic import BaseModel, validator, EmailStr
from datetime import datetime
from typing import Optional



class CoreModel(BaseModel):
    pass


class CreatedDateTimeModelMixin(BaseModel):
  created_at: Optional[datetime]

  @validator("created_at", pre=True)
  def default_datetime(cls, date: datetime):
    return date or datetime.now()


class UpdateDateTimeModelMixin(BaseModel):
  updated_at: Optional[datetime]

  @validator("updated_at", pre=True)
  def default_datetime(cls, date: datetime):
      return date or datetime.now()


class IDModelMixin(BaseModel):
  id: int




