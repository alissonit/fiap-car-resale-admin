from datetime import datetime
from sqlalchemy.engine import Engine
from sqlalchemy import text

from src.application.models.users import User
from src.application.ports.users import UserPort


class UserRepository(UserPort):
    """
    Class Repository for User
    """

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    async def register_user(self, user: User) -> User:
        async with self.engine.connect() as conn:
            query = text("INSERT INTO users (user_name, user_email, user_password, user_phone, user_created_at, user_updated_at) VALUES (:user_name, :user_email, :user_password, :user_phone, :user_created_at, :user_updated_at) RETURNING *")
            query = query.bindparams(
                user_name=user.user_name,
                user_email=user.user_email,
                user_password=user.user_password,
                user_phone=user.user_phone,
                user_created_at=datetime.now(),
                user_updated_at=None
            )

            result = await conn.execute(query)
            user_raw = result.fetchone()

            return User.model_validate(user_raw._mapping)

    async def list_user_by_access_token(self, access_token: str) -> User:
        async with self.engine.connect() as conn:
            query = text(
                "SELECT * FROM users WHERE access_token = :access_token")
            query = query.bindparams(access_token=access_token)
            result = await conn.execute(query)
            raw_user = result.fetchone()

            if raw_user:
                return User.model_validate(raw_user._mapping)
            return None

    async def list_by_user_email(self, user_email: str) -> User:
        async with self.engine.connect() as conn:
            query = text(
                "SELECT * FROM users WHERE user_email = :user_email")
            query = query.bindparams(user_email=user_email)
            result = await conn.execute(query)
            raw_user = result.fetchone()

            if raw_user:
                return User.model_validate(raw_user._mapping)
            return None

    async def list_users(self) -> list[User]:
        async with self.engine.connect() as conn:
            query = text("""SELECT * FROM users""")
            result = await conn.execute(query)
            return [dict(row) for row in result]

    async def list_by_user_id(self, user_id: int) -> User:
        async with self.engine.connect() as conn:
            query = text(
                "SELECT * FROM users WHERE user_id = :user_id")
            query = query.bindparams(user_id=user_id)
            result = await conn.execute(query)
            raw_user = result.fetchone()

            if raw_user:
                return User.model_validate(raw_user._mapping)
            return None

    async def update_user(self, user: User) -> User:
        async with self.engine.connect() as conn:
            query = text("UPDATE users SET user_name = :user_name, user_email = :user_email, user_password = :user_password, user_updated_at = :user_updated_at, access_token = :access_token WHERE user_id = :user_id RETURNING *")
            query = query.bindparams(
                user_id=user.user_id,
                user_name=user.user_name,
                user_email=user.user_email,
                user_password=user.user_password,
                access_token=user.access_token,
                user_updated_at=datetime.now()
            )
            result = await conn.execute(query)

            raw_user = result.fetchone()

            if raw_user:
                return User.model_validate(raw_user._mapping)

            return None

    async def delete_user(self, user_id: str) -> User:
        async with self.engine.connect() as conn:
            query = text("DELETE FROM users WHERE user_id = :user_id")
            await conn.execute(query, {"user_id": user_id})
            return user_id
