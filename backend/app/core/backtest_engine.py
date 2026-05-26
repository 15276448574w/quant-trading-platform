"""回测引擎"""
from datetime import datetime
from typing import List, Dict
import pandas as pd

class BacktestEngine:
    """回测引擎核心类"""
    
    def __init__(self, strategy, initial_capital: float = 100000.0):
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.portfolio = {}
        self.trades = []
        self.equity_curve = []
    
    def run(self, kline_data: pd.DataFrame, start_date: datetime, end_date: datetime):
        """
        运行回测
        
        Args:
            kline_data: K线数据
            start_date: 开始日期
            end_date: 结束日期
        """
        print(f"[Backtest] Starting backtest from {start_date} to {end_date}")
        print(f"[Backtest] Initial capital: {self.initial_capital}")
        
        # 遍历K线数据
        for idx, row in kline_data.iterrows():
            # 调用策略生成信号
            signal = self.strategy.on_bar(row)
            
            if signal:
                self.execute_trade(signal, row)
        
        return self.get_results()
    
    def execute_trade(self, signal: Dict, row: pd.Series):
        """执行交易"""
        print(f"[Trade] Signal: {signal}")
        self.trades.append(signal)
    
    def get_results(self) -> Dict:
        """获取回测结果"""
        total_return = (self.current_capital - self.initial_capital) / self.initial_capital * 100
        
        return {
            "initial_capital": self.initial_capital,
            "final_capital": self.current_capital,
            "total_return": total_return,
            "trades": len(self.trades),
            "trades_detail": self.trades
        }
