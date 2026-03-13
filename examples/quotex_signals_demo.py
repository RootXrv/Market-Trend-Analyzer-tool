"""
Example of getting Quotex signals
"""

from src.data_fetcher import get_market_data
from src.quotex_signals import get_quotex_signal

# Get EUR/USD data for Quotex
data = get_market_data("EURUSDT", "5m", 20)

if data:
    signal = get_quotex_signal(data)
    print(f"Quotex Signal: {signal['signal']}")
    print(f"Expiry: {signal['expiry']}")
    print(f"Confidence: {signal['confidence']}%")
