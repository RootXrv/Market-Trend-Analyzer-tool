"""
Display results in terminal
"""

from colorama import Fore, Style
import os

def show_results(symbol, result):
    """Show analysis results"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(Fore.CYAN + "="*50)
    print(f"📊 ANALYSIS RESULTS: {symbol}")
    print("="*50 + Style.RESET_ALL)
    
    print(f"\nCurrent Price: ${result['current_price']:.2f}")
    print(f"RSI: {result['rsi']:.1f}")
    
    # Color code the signal
    if "BUY" in result['signal']:
        signal_color = Fore.GREEN
    elif "SELL" in result['signal']:
        signal_color = Fore.RED
    else:
        signal_color = Fore.YELLOW
    
    print(f"\n{signal_color}Signal: {result['signal']}{Style.RESET_ALL}")
    print(f"Confidence: {result['confidence']:.1f}%")
    print(f"\nAdvice: {result['advice']}")
    
    print(Fore.CYAN + "\n" + "="*50)
    print("Press Enter to continue...")
    input()
