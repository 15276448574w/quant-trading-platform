from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_name = Column(String(100), nullable=False)
    account_type = Column(String(50), nullable=False)  # 'paper' or 'live'
    total_asset = Column(Float, default=0.0)  # 总资产
    available_cash = Column(Float, default=0.0)  # 可用资金
    holding_value = Column(Float, default=0.0)  # 持仓价值
    total_profit = Column(Float, default=0.0)  # 总盈亏
    profit_rate = Column(Float, default=0.0)  # 收益率
    initial_capital = Column(Float, default=0.0)  # 初始资金
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Account {self.account_name}>"
