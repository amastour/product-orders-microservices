from datetime import datetime
from fastapi import APIRouter, status, HTTPException, Response
from pymongo.collection import ReturnDocument
from client.models import client as clientModel
from client.serializers.client import clientEntiry, clientListEntity
from client.settings.database import Clients
from bson.objectid import ObjectId

client_router = APIRouter()

@client_router.get('/', response_model=clientModel.ListClientResponse)
def get_clients(limit: int= 10, page: int = 1, search: str = ""):
    skip = (page - 1) * limit
    pipeline = [
        {'$match': {'first_name': {'$regex': search, '$options': 'i'}}},
        {
            '$skip': skip
        }, {
            '$limit': limit
        }
    ]
    clients = clientListEntity(Clients.aggregate(pipeline))
    print("==========================")
    print(clients)
    return {'status': 'success', 'results': len(clients), 'clients': clients}


@client_router.post('/', status_code=status.HTTP_201_CREATED, response_model=clientModel.ClientResponse)
def create_client(payload: clientModel.Client):
    payload.createdAt = datetime.utcnow()
    payload.updatedAt = payload.createdAt
    try:
        result = Clients.insert_one(payload.dict(exclude_none=True))
        new_client = Clients.find_one({"_id": result.inserted_id})
        return {"status": "success", "client": new_client}
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Client with name: {payload.first_name} {payload.last_name}  already exists")

@client_router.patch('/{clientId}', response_model=clientModel.ClientResponse)
def update_client(clientId: str, payload: clientModel.Client):
    if not ObjectId.is_valid(clientId):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {clientId}")
    updated_client = Clients.find_one_and_update(
        {'_id': ObjectId(clientId)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No client with this id: {clientId} found')
    return {"status": "success", "client": updated_client}
    

@client_router.get('/{clientId}', response_model=clientModel.ClientResponse)
def get_client(clientId: str):
    if not ObjectId.is_valid(clientId):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {clientId}")
    client = Clients.find_one({'_id': ObjectId(clientId)})
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No client with this id: {clientId} found')
    return {"status": "success", "client": client}


@client_router.delete('/{clientId}')
def delete_client(clientId: str):
    if not ObjectId.is_valid(clientId):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {clientId}")
    client = Clients.find_one_and_delete({'_id': ObjectId(clientId)})
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No client with this id: {clientId} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
