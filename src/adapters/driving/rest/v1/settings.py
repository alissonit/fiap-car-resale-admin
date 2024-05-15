from fastapi import APIRouter, Depends
from typing import Annotated

from src.adapters.driving.rest.v1.login import manager

from src.configuration.settings import DBSettings, get_db_settings

from fastapi_login import LoginManager

router = APIRouter(prefix="/v1")


@router.get("/settings", response_model=DBSettings)
async def get_settings(
    db_settings: Annotated[DBSettings, Depends(
        get_db_settings)],
    user: LoginManager = Depends(manager)
) -> DBSettings:
    """
    Get settings
    """
    return db_settings
