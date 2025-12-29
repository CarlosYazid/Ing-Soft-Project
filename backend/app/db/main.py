from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from core import SETTINGS


ENGINE = create_async_engine(
    SETTINGS.db_url,
    echo=True,  # logging SQL (opcional)
)


AsyncSessionLocal = sessionmaker(
    bind=ENGINE,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def init_db():
    async with ENGINE.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
            
