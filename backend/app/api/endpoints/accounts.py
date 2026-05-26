from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_db
from app.models.account import Account
from app.schemas.account import AccountResponse, AccountCreate, AccountUpdate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[AccountResponse])
async def get_accounts(db: AsyncSession = Depends(get_db)):
    """获取所有账户"""
    result = await db.execute(select(Account))
    accounts = result.scalars().all()
    return accounts

@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(account_id: int, db: AsyncSession = Depends(get_db)):
    """获取单个账户"""
    result = await db.execute(select(Account).where(Account.id == account_id))
    account = result.scalar_one_or_none()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.post("/", response_model=AccountResponse)
async def create_account(account: AccountCreate, db: AsyncSession = Depends(get_db)):
    """创建账户"""
    db_account = Account(**account.dict())
    db.add(db_account)
    await db.commit()
    await db.refresh(db_account)
    return db_account

@router.put("/{account_id}", response_model=AccountResponse)
async def update_account(account_id: int, account: AccountUpdate, db: AsyncSession = Depends(get_db)):
    """更新账户"""
    result = await db.execute(select(Account).where(Account.id == account_id))
    db_account = result.scalar_one_or_none()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    for key, value in account.dict(exclude_unset=True).items():
        setattr(db_account, key, value)
    
    await db.commit()
    await db.refresh(db_account)
    return db_account

@router.get("/{account_id}/summary")
async def get_account_summary(account_id: int, db: AsyncSession = Depends(get_db)):
    """获取账户概览"""
    result = await db.execute(select(Account).where(Account.id == account_id))
    account = result.scalar_one_or_none()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return {
        "total_asset": account.total_asset,
        "available_cash": account.available_cash,
        "holding_value": account.holding_value,
        "total_profit": account.total_profit,
        "profit_rate": account.profit_rate,
        "account_type": account.account_type
    }
