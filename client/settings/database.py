from pymongo import mongo_client, ASCENDING
from product.settings.config import settings


client = mongo_client.MongoClient(settings.DATABASE_URL)
print('🚀 Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]

Clients = db.clients

Clients.create_index([("first_name", ASCENDING)], unique=True)
