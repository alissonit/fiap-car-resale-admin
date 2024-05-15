from fastapi import APIRouter, Depends
from fastapi_login import LoginManager

from dependency_injector.wiring import Provide, inject

from src.application.ports.users import UserPort
from src.application.models.users import User

from src.adapters.driving.rest.v1.login import manager
from src.adapters.driving.rest.v1.dto.user import (
    RegisterUserV1Request,
    RegisterUserV1Response,
    RegisterUserV1ListResponse,
    UpdateUserV1Request,
    DeleteUserV1Response
)

from src.configuration.dependency_injection import Container


router = APIRouter()


@router.post("/api/v1/users", response_model=RegisterUserV1Response)
@inject
async def register_user(
    user_request: RegisterUserV1Request,
    user_port: UserPort = Depends(Provide[Container.user_repository]),
    auth: LoginManager = Depends(manager)
):
    """
    Register a user
    """

    user = User(
        user_name=user_request.user_name,
        user_email=user_request.user_email,
        user_password=user_request.user_password,
        user_phone=user_request.user_phone
    )

    response = await user_port.register_user(user)

    return RegisterUserV1Response(
        user_id=response.user_id,
        user_name=response.user_name,
        user_email=response.user_email,
        user_phone=response.user_phone,
        user_created_at=response.user_created_at,
        user_updated_at=response.user_updated_at
    )


@router.get("/api/v1/users", response_model=RegisterUserV1ListResponse)
@inject
async def list_users(
    user_port: UserPort = Depends(Provide[Container.user_repository]),
    auth: LoginManager = Depends(manager)
) -> RegisterUserV1ListResponse:
    """
    List all users
    """

    users = await user_port.list_users()

    return RegisterUserV1ListResponse(
        users=users
    )


@router.get("/api/v1/users/{user_name}", response_model=RegisterUserV1Response)
@inject
async def list_by_user_email(
    user_name: str,
    user_port: UserPort = Depends(Provide[Container.user_repository]),
    auth: LoginManager = Depends(manager)
):
    """
    List user by user_name
    """

    user = await user_port.list_by_user_email(user_name)

    return user


@router.get("/api/v1/users/{user_id}", response_model=RegisterUserV1Response)
@inject
async def list_by_user_id(
    user_id: int,
    user_port: UserPort = Depends(Provide[Container.user_repository]),
    auth: LoginManager = Depends(manager)
):
    """
    List user by user_id
    """

    user = await user_port.list_by_user_id(user_id)

    return RegisterUserV1Response(
        user_id=user.user_id,
        user_name=user.user_name,
        user_email=user.user_email,
        user_phone=user.user_phone,
        user_created_at=user.user_created_at,
        user_updated_at=user.user_updated_at
    )


@router.put("/api/v1/users", response_model=UpdateUserV1Request)
@inject
async def update_user(
    user_request: UpdateUserV1Request,
    user_port: UserPort = Depends(Provide[Container.user_repository]),
    auth: LoginManager = Depends(manager)
) -> RegisterUserV1Response:
    """
    Update a user
    """

    user = User(
        user_id=user_request.user_id,
        user_name=user_request.user_name,
        user_email=user_request.user_email,
        user_phone=user_request.user_phone,
        user_password=user_request.user_password
    )

    user = await user_port.update_user(user)

    updated_user = await user_port.list_by_user_id(user_request.user_id)

    return UpdateUserV1Request(
        user_id=updated_user.user_id,
        user_name=updated_user.user_name,
        user_password=updated_user.user_password,
        user_email=updated_user.user_email,
        user_phone=updated_user.user_phone,
        user_created_at=updated_user.user_created_at,
        user_updated_at=updated_user.user_updated_at
    )


@router.delete("/api/v1/users{user_id}", response_model=DeleteUserV1Response)
@inject
async def delete_user(
    user_id: int,
    user_port: UserPort = Depends(Provide[Container.user_repository]),
    auth: LoginManager = Depends(manager)
):
    """
    Delete a user
    """

    await user_port.delete_user(user_id)

    return DeleteUserV1Response(
        user_id=user_id
    )
