"""
This module contains the Pydantic Models for the Users
"""
from datetime import datetime

from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    """
    Class Model for Register User
    """
    user_id: Optional[int] = None
    user_name: str
    user_email: str
    user_password: str
    access_token: Optional[str] = None
    user_phone: str
    user_created_at: Optional[datetime] = None
    user_updated_at: Optional[datetime] = None

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
