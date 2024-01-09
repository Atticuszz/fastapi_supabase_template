import logging

from gotrue import AuthResponse, User, UserResponse
from supabase_py_async import AsyncClient

from .base import CRUDBase
from ..schemas.auth import UserCreate, UserUpdate, UserOut


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    async def create_user_by_email(self, db: AsyncClient, *, obj_in: UserCreate) -> UserOut | None:
        rps: AuthResponse = await db.auth.sign_up(obj_in.model_dump())
        # NOTE: failed what will happen?
        if rps.user:
            return UserOut.from_auth_rsp(rps)
        else:
            logging.error(f"create_user_by_email failed: {rps}")
            return None

    async def update(
            self, db: AsyncClient, *,obj_in: UserUpdate
    ) -> UserOut | None:
        rps: UserResponse = await db.auth.update_user(UserUpdate)
        if rps.user:
            return UserOut(**rps.user.model_dump())
        else:
            logging.error(f"update failed: {rps}")
            return None

    async def authenticate(self, db: AsyncClient, *, email: str, password: str) -> UserOut | None:
        rep: AuthResponse = await db.auth.sign_in_with_password(email=email, password=password)
        if rep.user:
            return UserOut.from_auth_rsp(rep)
        else:
            logging.error(f"authenticate failed: {rep}")
            return None


user = CRUDUser()
