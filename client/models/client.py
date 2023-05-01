from __future__ import annotations
from typing import List
from pydantic import BaseModel
from datetime import datetime
from bson.objectid import ObjectId


class Client(BaseModel):
    id: str | None = None
    first_name: str
    last_name: str
    phone_number: str | None = None
    adress: str | None = None
    is_active: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UpdateClientSchedma(BaseModel):
    first_name: str
    last_name: str
    phone_number: str | None = None
    adress: str | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class ClientResponse(BaseModel):
    status: str
    client: Client

class ListClientResponse(BaseModel):
    status: str
    results: int
    clients: List[Client]
