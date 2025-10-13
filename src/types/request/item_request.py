from pydantic import BaseModel
from typing import Optional

class ItemRequest(BaseModel):
    name: str
    description: Optional[str] = ""
    price: float