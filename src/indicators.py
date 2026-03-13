"""
Technical Indicators for Market Analysis
"""

def calculate_rsi(prices, period=14):
    """Calculate RSI"""
    if len(prices) < period + 1:
        return 50
    
    # Calculate gains and losses
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])
    
    gains = []
    losses = []
    for change in changes[-period:]:
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))
    
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    
    if avg_loss == 0:
        return 100
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_moving_average(prices, period):
    """Simple Moving Average"""
    if len(prices) < period:
        return prices[-1]
    return sum(prices[-period:]) / period

def analyze_trend(data):
    """
    Analyze market trend and return signal
    """
    if not data or len(data) < 20:
        return {"signal": "WAIT", "confidence": 0, "message": "Not enough data"}
    
    # Get prices
    closes = [c['close'] for c in data]
    current_price = closes[-1]
    
    # RSI Analysis
    rsi = calculate_rsi(closes)
    
    if rsi < 30:
        rsi_score = 0.8
        rsi_msg = "Oversold - Good to buy"
    elif rsi > 70:
        rsi_score = 0.2
        rsi_msg = "Overbought - Better to sell"
    else:
        rsi_score = 0.5
        rsi_msg = "Neutral"
    
    # Moving Average Analysis
    ma_short = calculate_moving_average(closes, 10)
    ma_long = calculate_moving_average(closes, 30)
    
    if current_price > ma_short > ma_long:
        ma_score = 0.8
        ma_msg = "Strong uptrend"
    elif current_price < ma_short < ma_long:
        ma_score = 0.2
        ma_msg = "Strong downtrend"
    else:
        ma_score = 0.5
        ma_msg = "Mixed signals"
    
    # Calculate final score
    total_score = (rsi_score * 0.5) + (ma_score * 0.5)
    confidence = total_score * 100
    
    # Determine signal
    if confidence >= 70:
        signal = "STRONG BUY 🚀"
        advice = "Good time to buy!"
    elif confidence >= 60:
        signal = "BUY 📈"
        advice = "Slightly bullish"
    elif confidence >= 40:
        signal = "WAIT ➡️"
        advice = "Wait for clearer signal"
    elif confidence >= 30:
        signal = "SELL 📉"
        advice = "Consider selling"
    else:
        signal = "STRONG SELL 💀"
        advice = "Better to stay out"
    
    return {
        "signal": signal,
        "confidence": confidence,
        "advice": advice,
        "rsi": rsi,
        "current_price": current_price,
        "ma_short": ma_short,
        "ma_long": ma_long,
        "details": {
            "rsi": rsi_msg,
            "ma": ma_msg
        }
    }
