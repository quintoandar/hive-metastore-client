from unittest.mock import Mock

import pytest


@pytest.fixture()
def foo() -> Mock:
    return Mock()
