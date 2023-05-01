from fastapi import FastAPI

from client.routes.client import client_router


app = FastAPI()

app.include_router(client_router, tags=["Clients"], prefix="/api/client")

@app.get("/ping")
def ping():
    return {"msg": "pong"}