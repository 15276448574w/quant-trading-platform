from fastapi import APIRouter
from .endpoints import accounts, strategies, backtests, trades, markets

router = APIRouter(prefix="/api/v1")

# Include routers
router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
router.include_router(strategies.router, prefix="/strategies", tags=["strategies"])
router.include_router(backtests.router, prefix="/backtests", tags=["backtests"])
router.include_router(trades.router, prefix="/trades", tags=["trades"])
router.include_router(markets.router, prefix="/markets", tags=["markets"])
