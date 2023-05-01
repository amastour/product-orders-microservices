def clientEntiry(client) -> dict:
    return {
        "id": str(client["_id"]),
        "first_name": client["first_name"],
        "last_name": client["last_name"],
        "is_active": client["is_active"],
        "phone_number": client["phone_number"],
        "adress": client["adress"],
        "createdAt": client["createdAt"],
        "updatedAt": client["updatedAt"]
    }

def clientListEntity(clients) -> list:
    return [clientEntiry(client) for client in clients]
