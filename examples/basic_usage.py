"""
Simple example of how to use the analyzer
"""

from src.data_fetcher import get_market_data
from src.indicators import analyze_trend

# Get Bitcoin data
print("Fetching Bitcoin data...")
data = get_market_data("BTCUSDT", "1h")

if data:
    # Analyze trend
    result = analyze_trend(data)
    
    # Print results
    print(f"\nSignal: {result['signal']}")
    print(f"Confidence: {result['confidence']:.1f}%")
    print(f"Advice: {result['advice']}")
