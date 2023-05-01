import os

from pydantic import BaseSettings

class Setting(BaseSettings):
    CLIENT_SERVICE_URL: str
    PRODUCT_SERVICE_URL: str
    GATEWAY_TIMEOUT: int = 59

settings = Setting()