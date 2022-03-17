from dependency_injector import containers, providers

from .config import ApplicationConfig, application_config_factory

class Container(containers.DeclarativeContainer):
    application_config: providers.Provider[ApplicationConfig] = providers.Factory(provides=application_config_factory)
