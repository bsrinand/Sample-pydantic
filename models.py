from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    joined_at: Optional[datetime] = None
