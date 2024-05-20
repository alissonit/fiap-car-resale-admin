from fastapi import APIRouter, Depends
from fastapi_login import LoginManager

from src.adapters.driving.rest.v1.login import manager
from src.adapters.driving.rest.v1.dto.user import (
    RegisterUserV1Request,
    RegisterUserV1Response,
    RegisterUserV1ListResponse,
    UpdateUserV1Request,
    DeleteUserV1Response
)

from src.application.use_cases.users import UserUseCase

router = APIRouter()


@router.post("/api/v1/users", response_model=RegisterUserV1Response)
async def register_user(
    user_request: RegisterUserV1Request
):
    """
    Register a user
    """

    user = await UserUseCase.register_user(user_request)

    return user


@router.get("/api/v1/users", response_model=RegisterUserV1ListResponse)
async def list_users(
    auth: LoginManager = Depends(manager)
) -> RegisterUserV1ListResponse:
    """
    List all users
    """

    users = await UserUseCase.list_users()

    return users


@router.get("/api/v1/users/{user_name}", response_model=RegisterUserV1Response)
async def list_by_user_email(
    user_name: str,
    auth: LoginManager = Depends(manager)
):
    """
    List user by user_name
    """

    user = await UserUseCase.list_by_user_email(user_name)

    return user


@router.get("/api/v1/users/{user_id}", response_model=RegisterUserV1Response)
async def list_by_user_id(
    user_id: int,
    auth: LoginManager = Depends(manager)
):
    """
    List user by user_id
    """

    user = await UserUseCase.list_by_user_id(user_id)

    return user


@router.put("/api/v1/users", response_model=UpdateUserV1Request)
async def update_user(
    user_request: UpdateUserV1Request,
    auth: LoginManager = Depends(manager)
) -> RegisterUserV1Response:
    """
    Update a user
    """

    user = await UserUseCase.update_user(user_request)

    return user


@router.delete("/api/v1/users/{user_id}", response_model=DeleteUserV1Response)
async def delete_user(
    user_id: int,
    auth: LoginManager = Depends(manager)
):
    """
    Delete a user
    """

    user = await UserUseCase.delete_user(user_id)

    return {"user_id": user}
