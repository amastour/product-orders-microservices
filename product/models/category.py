from __future__ import annotations

from typing import List
from pydantic import BaseModel
from datetime import datetime
from product.models.product import Product


class Category(BaseModel):
    id: int
    name: str
    is_active: bool
    products: List[Product]
    createdAt: datetime | None = None
    updatedAt: datetime | None = None
