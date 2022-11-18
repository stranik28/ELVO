from pydantic import BaseModel
from typing import Optional

class UserBaseSchema(BaseModel):
    email: Optional[str] = None
    login: Optional[str] = None
    fio: Optional[str] = None
