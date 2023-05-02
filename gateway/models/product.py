from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from bson.objectid import ObjectId


class Product(BaseModel):
    id: Optional[str]
    name: str
    description: str
    is_active: bool = False
    quantity: int = 0
    category: str = ""
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UpdateProductSchedma(BaseModel):
    name: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    quantity: Optional[int]
    category: Optional[str]
    
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
