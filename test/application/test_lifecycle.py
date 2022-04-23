"""
Tests covering the Application StartUp/Init and Shutdown
"""

import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from dependency_injector.containers import Container

from application import Application


def test_application_init():
    """
    Verify that application is initialize sucessfully
    """
    _application = Application()
    with TestClient(app=_application) as _test_client:
        assert isinstance(_application.fastapi_object,
                          FastAPI), "fastapi object is not instanciate after initialization"

        print(_application.container)

        assert isinstance(_application.container,
                          Container), "container object is not instanciate after initialization"


@ pytest.mark.skip(reason="TODO-TEST")
def test_application_shutdown():
    """
    TODO-TEST : Verify that application is shutdown successfully
    """
    assert False
