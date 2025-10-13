from pydantic import BaseModel
from typing import Optional

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True
