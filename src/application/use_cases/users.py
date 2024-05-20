from fastapi import APIRouter, Depends, HTTPException

from dependency_injector.wiring import Provide, inject

from src.application.ports.users import UserPort

from src.adapters.driving.rest.v1.dto.user import (
    RegisterUserV1Request,
    RegisterUserV1Response,
    RegisterUserV1ListResponse,
    UpdateUserV1Request
)

from src.configuration.dependency_injection import Container


router = APIRouter()


class UserUseCase:

    @staticmethod
    @inject
    async def register_user(
        user_request: RegisterUserV1Request,
        user_port: UserPort = Depends(Provide[Container.user_repository])
    ):
        """
        Register a user
        """

        user = await user_port.register_user(user_request)

        return user

    @staticmethod
    @inject
    async def list_users(
        user_port: UserPort = Depends(Provide[Container.user_repository])
    ) -> RegisterUserV1ListResponse:
        """
        List all users
        """

        users = await user_port.list_users()

        return RegisterUserV1ListResponse(
            users=users
        )

    @staticmethod
    @inject
    async def list_by_user_email(
        user_name: str,
        user_port: UserPort = Depends(Provide[Container.user_repository])
    ):
        """
        List user by user_name
        """

        user = await user_port.list_by_user_email(user_name)

        return user

    @staticmethod
    @inject
    async def list_by_user_id(
        user_id: int,
        user_port: UserPort = Depends(Provide[Container.user_repository])
    ):
        """
        List user by user_id
        """

        user = await user_port.list_by_user_id(user_id)

        return user

    @staticmethod
    @inject
    async def update_user(
        user_request: UpdateUserV1Request,
        user_port: UserPort = Depends(Provide[Container.user_repository])
    ) -> RegisterUserV1Response:
        """
        Update a user
        """

        if await user_port.update_user(user_request):
            updated_user = await user_port.list_by_user_id(
                user_request.user_id)
            return updated_user

        return HTTPException(
            status_code=404,
            detail="User not found"
        )

    @staticmethod
    @inject
    async def delete_user(
        user_id: int,
        user_port: UserPort = Depends(Provide[Container.user_repository]),
    ):
        """
        Delete a user
        """

        user = await user_port.delete_user(user_id)
        
        if user:
            return user

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
