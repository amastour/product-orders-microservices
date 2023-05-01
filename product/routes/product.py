from datetime import datetime
from fastapi import APIRouter, status, HTTPException, Response
from pymongo.collection import ReturnDocument
from product.models import product as productModel
from product.serializers.product import productEntiry, productListEntity
from product.settings.database import Products
from bson.objectid import ObjectId

product_router = APIRouter()

@product_router.get('/', response_model=productModel.ListProductResponse)
def get_products(limit: int= 10, page: int = 1, search: str = ""):
    skip = (page - 1) * limit
    pipeline = [
        {'$match': {'name': {'$regex': search, '$options': 'i'}}},
        {
            '$skip': skip
        }, {
            '$limit': limit
        }
    ]
    products = productListEntity(Products.aggregate(pipeline))
    print(products)
    return {'status': 'success', 'results': len(products), 'products': products}


@product_router.post('/', status_code=status.HTTP_201_CREATED, response_model=productModel.ProductResponse)
def create_product(payload: productModel.Product):
    payload.createdAt = datetime.utcnow()
    payload.updatedAt = payload.createdAt
    try:
        result = Products.insert_one(payload.dict(exclude_none=True))
        new_product = Products.find_one({"_id": result.inserted_id})
        return {"status": "success", "product": new_product}
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Product with name: {payload.name} already exists")

@product_router.patch('/{productId}', response_model=productModel.ProductResponse)
def update_product(productId: str, payload: productModel.Product):
    if not ObjectId.is_valid(productId):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {productId}")
    updated_product = Products.find_one_and_update(
        {'_id': ObjectId(productId)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No product with this id: {productId} found')
    return {"status": "success", "product": updated_product}
    

@product_router.get('/{productId}', response_model=productModel.ProductResponse)
def get_product(productId: str):
    if not ObjectId.is_valid(productId):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {productId}")
    product = Products.find_one({'_id': ObjectId(productId)})
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No product with this id: {productId} found')
    return {"status": "success", "product": product}


@product_router.delete('/{productId}')
def delete_product(productId: str):
    if not ObjectId.is_valid(productId):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {productId}")
    product = Products.find_one_and_delete({'_id': ObjectId(productId)})
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No product with this id: {productId} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
