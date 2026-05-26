from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_db
from app.models.trade import Trade
from typing import List
from pydantic import BaseModel

router = APIRouter()

class TradeCreate(BaseModel):
    account_id: int
    code: str
    direction: str  # 'buy' or 'sell'
    price: float
    quantity: int
    commission: float = 0.0

@router.get("/")
async def get_trades(db: AsyncSession = Depends(get_db)):
    """获取所有交易"""
    result = await db.execute(select(Trade))
    trades = result.scalars().all()
    return trades

@router.get("/account/{account_id}")
async def get_account_trades(account_id: int, db: AsyncSession = Depends(get_db)):
    """获取账户的交易记录"""
    result = await db.execute(select(Trade).where(Trade.account_id == account_id))
    trades = result.scalars().all()
    return trades

@router.post("/")
async def create_trade(trade: TradeCreate, db: AsyncSession = Depends(get_db)):
    """创建交易"""
    trade_dict = trade.dict()
    trade_dict['amount'] = trade.price * trade.quantity
    db_trade = Trade(**trade_dict)
    db.add(db_trade)
    await db.commit()
    await db.refresh(db_trade)
    return db_trade
