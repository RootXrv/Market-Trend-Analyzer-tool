"""
Binance specific functions
"""

def format_binance_symbol(symbol):
    """Format symbol for Binance"""
    return symbol.upper().replace("/", "")

def get_binance_intervals():
    """Get available intervals"""
    return [
        "1m", "3m", "5m", "15m", "30m",
        "1h", "2h", "4h", "6h", "8h",
        "12h", "1d", "3d", "1w", "1M"
    ]
