import pytest
from unittest.mock import Mock, AsyncMock
from src.adapters.driven.repositories.users import UserRepository
from src.application.models.users import User


@pytest.fixture
def user():
    return User(
        user_email="test@hotmail.com",
        user_name="test",
        user_password="test",
        user_phone="11999999999"
    )


@pytest.fixture
def engine():
    engine = Mock()
    engine.connect = AsyncMock()
    return engine


@pytest.mark.asyncio
async def test_register_user(user, engine):
    user_repository = UserRepository(engine)
    user_repository.register_user = AsyncMock(return_value=user)
    user = await user_repository.register_user(user)
    assert user.user_email == "test@hotmail.com"
    

@pytest.mark.asyncio
async def test_list_user_by_access_token(user, engine):
    user_repository = UserRepository(engine)
    user_repository.list_user_by_access_token = AsyncMock(return_value=user)
    user = await user_repository.list_user_by_access_token("test")
    assert user.user_email == "test@hotmail.com"


