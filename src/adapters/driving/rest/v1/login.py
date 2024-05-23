import os
from datetime import timedelta

from fastapi import Depends, APIRouter, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager

from dependency_injector.wiring import Provide, inject
from src.configuration.dependency_injection import Container

from src.application.ports.users import UserPort
from src.application.models.users import User


try:
    SECRET = os.environ['SECRET']
except KeyError:
    SECRET = "secret_alisson-xpto122"

manager = LoginManager(SECRET, token_url='/auth/token')

router = APIRouter()


@inject
async def update_access_token(
    user: User,
    user_port: UserPort = Depends(Provide[Container.user_repository])
):

    access_token = manager.create_access_token(
        data=dict(sub=user.user_email),
        expires=timedelta(hours=1)
    )

    user.access_token = access_token

    user = await user_port.update_user(user)

    return user.access_token


@manager.user_loader()
@inject
async def load_user(
    email: str,
    fist_login: bool = False,
    user_port: UserPort = Depends(Provide[Container.user_repository])
):

    user = await user_port.list_by_user_email(email)

    try:
        if fist_login:
            return user
        if user.access_token:
            return user
        raise InvalidCredentialsException
    except AttributeError:
        raise InvalidCredentialsException


@router.post('/auth/logout')
@inject
async def logout(
    request: Request,
    user_port: UserPort = Depends(Provide[Container.user_repository])
):
    user = await user_port.list_user_by_access_token(
        request.headers.get('Authorization').split(' ')[1])
    if user:
        user.access_token = None
        await user_port.update_user(user)
        return {'message': 'Successfully logged out'}
    return {'message': 'access_token not found'}


@router.post('/auth/login')
async def login(
    data: OAuth2PasswordRequestForm = Depends(),
):
    user_name = data.username
    password = data.password

    user = await load_user(email=user_name, fist_login=True)

    if not user:
        raise InvalidCredentialsException
    elif password != user.user_password:
        raise InvalidCredentialsException

    access_token = await update_access_token(user)

    return {'access_token': access_token, 'token_type': 'bearer'}
