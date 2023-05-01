from fastapi import FastAPI

from product.routes.product import product_router


app = FastAPI()

app.include_router(product_router, tags=["Products"], prefix="/api/product")

@app.get("/ping")
def ping():
    return {"msg": "pong"}