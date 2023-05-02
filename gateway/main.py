from fastapi import (
    FastAPI,
    status,
    Request,
    Response
    )
from gateway.settings.conf import settings
from gateway.utils.core import route

from gateway.models.client import Client


app = FastAPI()


@route(
    request_method=app.get,
    path="/api/client",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.CLIENT_SERVICE_URL,
    authentication_required=False,
    post_processing_func=None,
    authentication_token_decoder="gateway.utils.auth.decode_access_token",
    service_authorization_checker="gateway.utils.auth.generate_request_header",
    service_header_generator=None,
    response_model="gateway.models.client.ListClientResponse",
    response_list=False
)
async def list_clients(request: Request, response: Response):
    pass

@app.get("/ping")
def ping():
    return {
        "CLIENT_SERVICE_URL": settings.CLIENT_SERVICE_URL,
        "PRODUCT_SERVICE_URL":settings.PRODUCT_SERVICE_URL,
        }