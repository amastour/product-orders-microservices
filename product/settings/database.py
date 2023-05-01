from pymongo import mongo_client, ASCENDING
from product.settings.config import settings


client = mongo_client.MongoClient(settings.DATABASE_URL)
print('🚀 Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]

Products = db.products
Categories = db.categories

Products.create_index([("name", ASCENDING)], unique=True)
Categories.create_index([("name", ASCENDING)], unique=True)
