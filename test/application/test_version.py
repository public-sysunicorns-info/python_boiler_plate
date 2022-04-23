"""
    Tests application/version.py behavior
"""

import inspect
import re
import subprocess

from test import VERSION_REGEX
from application import version


def test_version_attribute_exist_in_version():
    """
    Test that verifiy if VERSION attribute exist on the module
    """
    assert inspect.getattr_static(version, "VERSION", None) is not None


def test_version_format():
    """
    Test that verify the good format of the version
    """
    assert isinstance(re.match(pattern=VERSION_REGEX,
                      string=version.VERSION), re.Match)


def test_version_is_print_when_call():
    """
    Test that verify the success printing of the version
    """
    try:
        _completed_process = subprocess.run(
            [
                "python3",
                "src/application/version.py"
            ],
            capture_output=True,
            check=True,
            encoding="utf-8",
            timeout=2
        )
    except subprocess.CalledProcessError:
        assert False, "Execution failed with CalledProcessError"
    except RuntimeError:
        assert False, "Execution failed with RuntimeError"
    else:
        assert _completed_process.returncode == 0, "python3 execution failed"
        assert str(_completed_process.stdout).replace(
            "\n", "") == str(version.VERSION), ""
