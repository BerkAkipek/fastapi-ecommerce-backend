from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings
from typing import AsyncGenerator

engine = create_async_engine(settings.DATABASE_URL, echo=False)
async_session_local = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_local() as session:
        yield session
