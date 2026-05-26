from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_db
from app.models.backtest import Backtest
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class BacktestCreate(BaseModel):
    strategy_id: int
    backtest_name: str
    start_date: datetime
    end_date: datetime
    initial_capital: float = 100000.0

@router.get("/")
async def get_backtests(db: AsyncSession = Depends(get_db)):
    """获取所有回测"""
    result = await db.execute(select(Backtest))
    backtests = result.scalars().all()
    return backtests

@router.get("/{backtest_id}")
async def get_backtest(backtest_id: int, db: AsyncSession = Depends(get_db)):
    """获取单个回测"""
    result = await db.execute(select(Backtest).where(Backtest.id == backtest_id))
    backtest = result.scalar_one_or_none()
    if not backtest:
        raise HTTPException(status_code=404, detail="Backtest not found")
    return backtest

@router.post("/")
async def create_backtest(backtest: BacktestCreate, db: AsyncSession = Depends(get_db)):
    """创建回测"""
    db_backtest = Backtest(**backtest.dict())
    db.add(db_backtest)
    await db.commit()
    await db.refresh(db_backtest)
    return {"message": "Backtest started", "id": db_backtest.id}

@router.delete("/{backtest_id}")
async def delete_backtest(backtest_id: int, db: AsyncSession = Depends(get_db)):
    """删除回测"""
    result = await db.execute(select(Backtest).where(Backtest.id == backtest_id))
    db_backtest = result.scalar_one_or_none()
    if not db_backtest:
        raise HTTPException(status_code=404, detail="Backtest not found")
    
    await db.delete(db_backtest)
    await db.commit()
    return {"message": "Backtest deleted"}
