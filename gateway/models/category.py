from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from gateway.models.product import Product


class Category(BaseModel):
    id: int
    name: str
    is_active: bool
    products: List[Product]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
