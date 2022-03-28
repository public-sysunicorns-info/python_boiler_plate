"""
Package root for all the api (http)
"""

from fastapi import APIRouter

API_ROUTER_PREFIX="/api"

# Initialize the root api router
api_router = APIRouter(
    prefix=API_ROUTER_PREFIX
)

# Include here child Api

# Include Info Api
from .info import info_api_router
api_router.include_router(router=info_api_router)
