"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 07/01/2024
@Description  :
"""
from gotrue import AuthResponse
from supabase_py_async import AsyncClient

from .crud_item import item
from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
from app.core.security import get_password_hash, verify_password
from ..schemas.user import UserCreate, User, UserOut


async def create_user_by_email(*, session: AsyncClient, user_create: UserCreate) -> UserOut:

    rps: AuthResponse = await session.auth.sign_up(user_create.model_dump())
    # NOTE: failed what will happen?

    return UserOut(**rps.user.model_dump(), access_token=rps.session.access_token)




def authenticate(*, session: Session, email: str, password: str) -> User | None:

