"""
Response for info endpoints
"""

from pydantic import BaseModel, Field


class KubeInfo(BaseModel):
    """
    Kube part of the information
    """
    namespace: str | None = Field(title="Kubernetes namespace of the running application")
    pod_name: str | None = Field(title="Kubernetes pod name of the running application")
    pod_ip: str | None = Field(title="Kubernetes pod ip of the application")


class InfoResponse(BaseModel):
    """
    Response Info Model
    """
    name: str = Field(
        description="""
        Application Name
        """
    )
    description: str = Field(
        description="""
        Short Application Description
        """
    )
    version: str = Field(
        description="""
        Version of the application release
        """
    )
    kube: KubeInfo
