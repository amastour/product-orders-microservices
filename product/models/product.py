from __future__ import annotations
from typing import List
from pydantic import BaseModel
from datetime import datetime
from bson.objectid import ObjectId


class Product(BaseModel):
    id: str | None = None
    name: str
    description: str
    is_active: bool = False
    quantity: int = 0
    category: str = ""
    createdAt: datetime | None = None
    updatedAt: datetime | None = None
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UpdateProductSchedma(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None
    quantity: int | None = None
    category: str | None = None
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ProductResponse(BaseModel):
    status: str
    product: Product

class ListProductResponse(BaseModel):
    status: str
    results: int
    products: List[Product]
