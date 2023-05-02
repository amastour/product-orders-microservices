from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from bson.objectid import ObjectId


class Client(BaseModel):
    id: Optional[str]
    first_name: str
    last_name: str
    phone_number: Optional[str]
    adress: Optional[str]
    is_active: bool = False
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]



class UpdateClientSchedma(BaseModel):
    first_name: str
    last_name: str
    phone_number: Optional[str]
    adress: Optional[str]


class ClientResponse(BaseModel):
    status: str
    client: Client

class ListClientResponse(BaseModel):
    status: str
    results: int
    clients: List[Client]
