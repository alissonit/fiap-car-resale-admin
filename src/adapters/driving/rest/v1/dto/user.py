"""
This module contains the Pydantic Models for the Users
"""
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from datetime import datetime

from typing import Optional


@dataclass
class RegisterUserV1Request(BaseModel):
    """
    Class Model for Register User
    """
    user_name: str
    user_email: str
    user_password: str
    user_phone: str

    class Config:
        """
        Class config for Register User
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_name": "John Doe",
                "user_email": "user@email.com",
                "user_password": "password",
                "user_phone": "1234567890"
            }
        }


class RegisterUserV1Response(BaseModel):
    """
    Class Model for Register User Response
    """
    user_id: Optional[int]
    user_name: str
    user_email: str
    user_phone: str
    user_created_at: Optional[datetime] = None
    user_updated_at: Optional[datetime] = None

    class Config:
        """
        Class config for Register User Response
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_name": "John Doe",
                "user_email": "user@email.com",
                "user_phone": "1234567890",
                "user_address": "1234 Main St, City, State, Zip"
            }
        }


class UpdateUserV1Request(BaseModel):
    """
    Class Model for Update User
    """
    user_id: int
    user_name: str
    user_email: str
    user_password: str
    user_phone: str
    user_created_at: Optional[datetime] = None
    user_updated_at: Optional[datetime] = None

    class Config:
        """
        Class config for Update User
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "user_name": "John Doe",
                "user_email": "user@email.com",
                "user_password": "password",
                "user_phone": "1234567890",
                "user_address": "1234 Main St, City, State, Zip"
            }
        }


class RegisterUserV1ListResponse(BaseModel):
    users: list[RegisterUserV1Response]


class DeleteUserV1Request(BaseModel):
    user_id: int

    class Config:
        """
        Class config for Delete User
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": 1
            }
        }


class DeleteUserV1Response(BaseModel):
    user_id: int

    class Config:
        """
        Class config for Delete User
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": 1
            }
        }
