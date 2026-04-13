from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserResponse(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
