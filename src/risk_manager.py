"""
Risk management calculations
"""

def calculate_position_size(account_balance, risk_percent, stop_loss_percent):
    """
    Calculate safe position size
    """
    risk_amount = account_balance * (risk_percent / 100)
    position_size = risk_amount / (stop_loss_percent / 100)
    
    return position_size

def should_trade(signal_confidence, min_confidence=60):
    """
    Check if confidence is high enough to trade
    """
    return signal_confidence >= min_confidence
