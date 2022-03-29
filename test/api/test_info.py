"""
    Tests corresponding to the API Info Endpoint
"""

import json
import re
import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient

from test import VERSION_REGEX, CONTENT_TYPE_JSON
from application import Application


API_INFO_PATH = "/api/info"


def test_api_info_exist():
    with TestClient(app=Application()) as _test_client:        
        _response = _test_client.get(API_INFO_PATH)
        assert _response.status_code == HTTPStatus.OK.value, "Response is not HTTPStatus.OK (200)"

def test_api_info_response_is_json():
    with TestClient(app=Application()) as _test_client:
        _response = _test_client.get(API_INFO_PATH)
        assert _response.headers.get("Content-Type", None) == CONTENT_TYPE_JSON, f"Content-Type Header is not {CONTENT_TYPE_JSON}"        
        try:
            _content_json = json.loads(_response.content)
        except RuntimeError as e:
            assert False, "JSON Parsing Failed with exception"
        else:
            assert True, "JSON Parse with Success"
            
def test_api_provide_version_with_correct_format():
    with TestClient(app=Application()) as _test_client:        
        _response = _test_client.get(API_INFO_PATH)
        _content_json = json.loads(_response.content)
        assert isinstance(re.match(pattern=VERSION_REGEX, string=_content_json.get("version")), re.Match)
        
@pytest.mark.skip(reason="TODO-TEST")
def test_api_provide_name_with_correct_format():
    """
    TODO-TEST : Define application_nane regex format
    """

@pytest.mark.skip(reason="TODO-TEST")
def test_api_provide_description_with_correct_format():
    """
    TODO-TEST : Define description regex format
    """
