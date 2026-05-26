from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings
from typing import AsyncGenerator

# Create base class for models
Base = declarative_base()

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
)

# Create async session factory
async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """获取数据库会话"""
    async with async_session() as session:
        yield session

async def init_db():
    """初始化数据库"""
    async with engine.begin() as conn:
        # 创建所有表
        from app.models.user import User
        from app.models.account import Account
        from app.models.strategy import Strategy
        from app.models.backtest import Backtest
        from app.models.trade import Trade
        
        await conn.run_sync(Base.metadata.create_all)
        print("✅ 数据库表已创建")
