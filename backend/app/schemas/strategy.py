from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class StrategyBase(BaseModel):
    name: str
    description: Optional[str] = None
    code: str
    parameters: Optional[Dict[str, Any]] = None

class StrategyCreate(StrategyBase):
    user_id: int

class StrategyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None
    status: Optional[str] = None

class StrategyResponse(StrategyBase):
    id: int
    user_id: int
    is_active: bool
    status: str
    win_rate: float
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    created_at: datetime
    
    class Config:
        from_attributes = True
