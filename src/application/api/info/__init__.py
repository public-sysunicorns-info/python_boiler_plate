"""
Info package
"""

import fastapi
from dependency_injector.wiring import inject


info_api_router = fastapi.APIRouter()

@inject
@info_api_router.get(
    path="/info"
)
def get_info():
    """
    Controller for GET /api/info endpoint
    """
    pass
