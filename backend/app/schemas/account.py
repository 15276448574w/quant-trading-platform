from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AccountBase(BaseModel):
    account_name: str
    account_type: str  # 'paper' or 'live'
    initial_capital: float

class AccountCreate(AccountBase):
    user_id: int

class AccountUpdate(BaseModel):
    account_name: Optional[str] = None
    total_asset: Optional[float] = None
    available_cash: Optional[float] = None
    holding_value: Optional[float] = None

class AccountResponse(AccountBase):
    id: int
    user_id: int
    total_asset: float
    available_cash: float
    holding_value: float
    total_profit: float
    profit_rate: float
    created_at: datetime
    
    class Config:
        from_attributes = True
