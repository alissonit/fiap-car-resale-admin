from abc import ABC, abstractmethod

from src.application.models.users import User


class UserPort(ABC):
    """
    Interface for User Port
    """

    @abstractmethod
    async def register_user(self, user: User) -> User:
        """
        Register User
        """
        pass

    @abstractmethod
    async def list_users(self) -> list[User]:
        """
        List Users
        """
        pass

    @abstractmethod
    async def list_user_by_access_token(self, access_token: str) -> User:
        """
        List User by Access Token
        """
        pass

    @abstractmethod
    async def list_by_user_email(self, user_email: str) -> User:
        """
        List User by User Email
        """
        pass

    @abstractmethod
    async def list_by_user_id(self, user_id: str) -> User:
        """
        List User by User ID
        """
        pass

    @abstractmethod
    async def update_user(self, user: User) -> User:
        """
        Update User
        """
        pass

    @abstractmethod
    async def delete_user(self, user_id: str) -> User:
        """
        Delete User
        """
        pass
