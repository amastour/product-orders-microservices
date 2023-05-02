from  decouple import config
from pydantic import BaseSettings

class Setting(BaseSettings):
    CLIENT_SERVICE_URL: str =  config("CLIENT_SERVICE_URL", default=False, cast=str)  # type: ignore
    PRODUCT_SERVICE_URL: str = config("PRODUCT_SERVICE_URL", default=False, cast=str)  # type: ignore
    GATEWAY_TIMEOUT: int = 59

settings = Setting()
