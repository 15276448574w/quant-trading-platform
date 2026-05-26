"""数据源处理模块"""
import pandas as pd
from app.core.config import settings

class DataSource:
    """数据源基类"""
    
    def get_kline(self, code: str, start_date: str, end_date: str, freq: str = "D"):
        raise NotImplementedError
    
    def get_quote(self, code: str):
        raise NotImplementedError

class TushareDataSource(DataSource):
    """Tushare 数据源"""
    
    def __init__(self):
        try:
            import tushare as ts
            self.ts = ts
            self.pro = ts.pro_api(settings.TUSHARE_TOKEN)
        except ImportError:
            raise ImportError("Tushare not installed")
    
    def get_kline(self, code: str, start_date: str, end_date: str, freq: str = "D"):
        """获取K线数据"""
        try:
            df = self.pro.daily(
                ts_code=code,
                start_date=start_date.replace("-", ""),
                end_date=end_date.replace("-", "")
            )
            return df
        except Exception as e:
            print(f"Error fetching data from Tushare: {e}")
            return pd.DataFrame()
    
    def get_quote(self, code: str):
        """获取实时行情"""
        try:
            df = self.pro.daily(ts_code=code, start_date="20240101", end_date="20240101")
            if not df.empty:
                return df.iloc[0].to_dict()
            return {}
        except Exception as e:
            print(f"Error fetching quote: {e}")
            return {}

class AKShareDataSource(DataSource):
    """AKShare 数据源"""
    
    def __init__(self):
        try:
            import akshare as ak
            self.ak = ak
        except ImportError:
            raise ImportError("AKShare not installed")
    
    def get_kline(self, code: str, start_date: str, end_date: str, freq: str = "D"):
        """获取K线数据"""
        try:
            # AKShare example
            symbol = f"sz{code}" if not code.startswith(('sh', 'sz')) else code
            df = self.ak.stock_zh_a_hist(
                symbol=symbol,
                start_date=start_date,
                end_date=end_date,
                adjust="qfq"
            )
            return df
        except Exception as e:
            print(f"Error fetching data from AKShare: {e}")
            return pd.DataFrame()
