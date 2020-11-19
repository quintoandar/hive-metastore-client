from unittest.mock import Mock

import pytest


@pytest.fixture(scope="function")
def foo():
    return Mock()
