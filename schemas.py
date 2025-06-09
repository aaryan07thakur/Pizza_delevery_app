from pydantic import BaseModel, Field
from typing import Optional

class SingUpModel(BaseModel):
    id: Optional[int] = Field(default=None)
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "username": "Dipeshthakur",
                "email": "abc@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True,
            }
        }
    }