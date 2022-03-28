"""
Info package
"""

from http import HTTPStatus
from fastapi import APIRouter, Depends, Response
from dependency_injector.wiring import inject, Provide

from application.config import ApplicationConfig
from application.container import Container
from application.version import VERSION

from .response import InfoResponse, KubeInfo

INFO_TAG = "Info"

info_api_router = APIRouter()

@info_api_router.get(
    path="/info",
    tags=[INFO_TAG],
    summary="""
    Provide information about the application
    """,
    responses={
        HTTPStatus.OK.value: {"model": InfoResponse}
    }
)
@inject
def get_info(
    response: Response,
    application_config: ApplicationConfig = Depends(Provide[Container.application_config]())
    ):
    """
    Controller for GET /api/info endpoint
    """
    response.status_code = HTTPStatus.OK
    return InfoResponse(
        name=application_config.name,
        description=application_config.description,
        version=VERSION,
        kube=KubeInfo(
            namespace=application_config.kube_namespace,
            pod_name=application_config.kube_pod_name,
            pod_ip=application_config.kube_pod_ip
        )
    )
