"""
Packaging the container class
"""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Provider

from .config import ApplicationConfig, application_config_factory

class Container(DeclarativeContainer):
    """
    Application container to register element for the dependency-injector
    """
    application_config: Provider[ApplicationConfig] = \
        Singleton(provides=application_config_factory)
