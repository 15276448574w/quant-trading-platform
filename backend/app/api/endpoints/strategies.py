from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_db
from app.models.strategy import Strategy
from app.schemas.strategy import StrategyResponse, StrategyCreate, StrategyUpdate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[StrategyResponse])
async def get_strategies(db: AsyncSession = Depends(get_db)):
    """获取所有策略"""
    result = await db.execute(select(Strategy))
    strategies = result.scalars().all()
    return strategies

@router.get("/{strategy_id}", response_model=StrategyResponse)
async def get_strategy(strategy_id: int, db: AsyncSession = Depends(get_db)):
    """获取单个策略"""
    result = await db.execute(select(Strategy).where(Strategy.id == strategy_id))
    strategy = result.scalar_one_or_none()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

@router.post("/", response_model=StrategyResponse)
async def create_strategy(strategy: StrategyCreate, db: AsyncSession = Depends(get_db)):
    """创建策略"""
    db_strategy = Strategy(**strategy.dict())
    db.add(db_strategy)
    await db.commit()
    await db.refresh(db_strategy)
    return db_strategy

@router.put("/{strategy_id}", response_model=StrategyResponse)
async def update_strategy(strategy_id: int, strategy: StrategyUpdate, db: AsyncSession = Depends(get_db)):
    """更新策略"""
    result = await db.execute(select(Strategy).where(Strategy.id == strategy_id))
    db_strategy = result.scalar_one_or_none()
    if not db_strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    for key, value in strategy.dict(exclude_unset=True).items():
        setattr(db_strategy, key, value)
    
    await db.commit()
    await db.refresh(db_strategy)
    return db_strategy

@router.delete("/{strategy_id}")
async def delete_strategy(strategy_id: int, db: AsyncSession = Depends(get_db)):
    """删除策略"""
    result = await db.execute(select(Strategy).where(Strategy.id == strategy_id))
    db_strategy = result.scalar_one_or_none()
    if not db_strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    await db.delete(db_strategy)
    await db.commit()
    return {"message": "Strategy deleted"}
