"""
Test indicator calculations
"""

from src.indicators import calculate_rsi, calculate_moving_average

def test_rsi():
    prices = [100, 102, 101, 103, 105, 104, 106, 108, 107, 109]
    rsi = calculate_rsi(prices)
    assert 0 <= rsi <= 100
    print("✅ RSI test passed")

def test_ma():
    prices = [100, 102, 101, 103, 105]
    ma = calculate_moving_average(prices, 3)
    assert ma > 0
    print("✅ Moving average test passed")

if __name__ == "__main__":
    test_rsi()
    test_ma()
