"""
Generate signals for Quotex trading
"""

def get_quotex_signal(data):
    """
    Generate binary options signal
    Suitable for 1-5 minute trades
    """
    if not data or len(data) < 10:
        return {"signal": "WAIT", "expiry": "5min"}
    
    closes = [c['close'] for c in data]
    
    # Simple logic for binary options
    last_3 = closes[-3:]
    
    if last_3[0] < last_3[1] < last_3[2]:  # 3 up candles
        return {
            "signal": "CALL (UP)",
            "expiry": "5min",
            "confidence": 70
        }
    elif last_3[0] > last_3[1] > last_3[2]:  # 3 down candles
        return {
            "signal": "PUT (DOWN)",
            "expiry": "5min",
            "confidence": 70
        }
    else:
        return {
            "signal": "WAIT",
            "expiry": "5min",
            "confidence": 50
        }
