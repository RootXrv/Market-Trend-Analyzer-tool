"""
Constants used throughout the program
"""

# Timeframes
TIMEFRAMES = {
    '1m': '1 minute',
    '5m': '5 minutes',
    '15m': '15 minutes',
    '1h': '1 hour',
    '4h': '4 hours',
    '1d': '1 day'
}

# Signal strengths
SIGNALS = {
    'STRONG_BUY': {'emoji': '🚀', 'color': 'green', 'min_score': 70},
    'BUY': {'emoji': '📈', 'color': 'green', 'min_score': 60},
    'WAIT': {'emoji': '➡️', 'color': 'yellow', 'min_score': 40},
    'SELL': {'emoji': '📉', 'color': 'red', 'min_score': 30},
    'STRONG_SELL': {'emoji': '💀', 'color': 'red', 'min_score': 0}
}

# API endpoints
BINANCE_API = "https://api.binance.com/api/v3"
BYBIT_API = "https://api.bybit.com/v5/market"
