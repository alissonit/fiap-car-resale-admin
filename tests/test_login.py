import pytest
from unittest.mock import Mock, AsyncMock


@pytest.fixture
def user_port():
    return Mock()


@pytest.mark.asyncio
async def test_login_invalid_credentials(user_port):
    user_port.list_by_user_email = AsyncMock(return_value=None)
    assert user_port.update_user.call_count == 0
