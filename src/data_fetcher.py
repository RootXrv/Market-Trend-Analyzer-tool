"""
Fetches market data from Binance
"""

import requests
from datetime import datetime

def get_market_data(symbol="BTCUSDT", interval="1h", limit=50):
    """
    Get market data from Binance
    """
    try:
        url = "https://api.binance.com/api/v3/klines"
        params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print("❌ Error: Could not get data")
            return None
        
        data = response.json()
        
        # Organize the data
        market_data = []
        for candle in data:
            market_data.append({
                'time': datetime.fromtimestamp(candle[0]/1000),
                'open': float(candle[1]),
                'high': float(candle[2]),
                'low': float(candle[3]),
                'close': float(candle[4]),
                'volume': float(candle[5])
            })
        
        return market_data
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
