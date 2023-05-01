def productEntiry(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "is_active": product["is_active"],
        "quantity": product["quantity"],
        "category": product["category"],
        "createdAt": product["createdAt"],
        "updatedAt": product["updatedAt"]
    }

def productListEntity(products) -> list:
    print(products)
    return [productEntiry(product) for product in products] 