#!/usr/bin/env python3
"""
Market Trend Analyzer Tool- Main Program
"""

import json
import os
import sys
from colorama import init, Fore

# Import our modules
from src.data_fetcher import get_market_data
from src.indicators import analyze_trend
from src.display import show_results

# Initialize colors
init()

def load_config():
    """Load settings from config file"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except:
        return {"favorites": {"crypto": ["BTCUSDT"]}, "settings": {"default_timeframe": "1h"}}

def main():
    """Main program"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(Fore.CYAN + "="*50)
    print("🚀 MARKET TREND ANALYZER")
    print("="*50 + Fore.RESET)
    
    # Load config
    config = load_config()
    
    # Show menu
    print("\n1. Analyze Crypto")
    print("2. Analyze Forex")
    print("3. Settings")
    print("4. Exit")
    
    choice = input("\nChoose (1-4): ")
    
    if choice == "1":
        symbol = input("Enter crypto (BTCUSDT): ") or "BTCUSDT"
        data = get_market_data(symbol)
        if data:
            result = analyze_trend(data)
            show_results(symbol, result)
    
    elif choice == "4":
        print("Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
