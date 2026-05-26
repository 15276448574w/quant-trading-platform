from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base

class Trade(Base):
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    strategy_id = Column(Integer, ForeignKey("strategies.id"))
    code = Column(String(20), nullable=False)  # 股票代码
    direction = Column(String(10), nullable=False)  # 'buy' or 'sell'
    price = Column(Float, nullable=False)  # 成交价格
    quantity = Column(Integer, nullable=False)  # 成交数量
    amount = Column(Float, nullable=False)  # 成交金额
    commission = Column(Float, default=0.0)  # 手续费
    profit = Column(Float, default=0.0)  # 盈亏
    status = Column(String(50), default="completed")  # pending, completed, cancelled
    trade_time = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<Trade {self.code} {self.direction} {self.quantity}>"
