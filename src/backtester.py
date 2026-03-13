"""
Simple backtesting engine
"""

def backtest_strategy(data, strategy_func):
    """
    Test a strategy on historical data
    """
    if not data:
        return {"win_rate": 0, "total_trades": 0}
    
    wins = 0
    total = 0
    
    for i in range(20, len(data) - 1):
        # Get signal
        past_data = data[:i]
        signal = strategy_func(past_data)
        
        if signal in ["BUY", "SELL"]:
            total += 1
            # Check if price moved in right direction
            future_price = data[i+1]['close']
            current_price = data[i]['close']
            
            if signal == "BUY" and future_price > current_price:
                wins += 1
            elif signal == "SELL" and future_price < current_price:
                wins += 1
    
    win_rate = (wins / total * 100) if total > 0 else 0
    
    return {
        "win_rate": win_rate,
        "total_trades": total,
        "wins": wins
          }
