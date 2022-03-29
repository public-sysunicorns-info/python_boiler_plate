"""
Tests covering the ApplicationConfig Class
"""

from fastapi.testclient import TestClient

from application import Application
from application.config import ApplicationConfig


def test_application_config_init_with_success():
    """
    Validate that ApplicationConfig is provide
    """
    _application = Application()
    with TestClient(app=_application) as _test_client:        
        _application_config = _application.container.application_config()
        assert isinstance(_application_config, ApplicationConfig)


def test_application_config_is_singleton():
    """
    Validate Singleton of ApplicationConfig in Container
    """
    _application = Application()
    with TestClient(app=_application) as _test_client:        
        _application_config_a = _application.container.application_config()
        _application_config_b = _application.container.application_config()
        assert \
            isinstance(_application_config_a, _application_config_b.__class__), \
            "object has same class"
        assert _application_config_a == _application_config_b, "instance is equal"
