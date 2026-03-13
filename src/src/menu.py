"""
Menu system for the application
"""

from colorama import Fore
import sys

def show_main_menu():
    """Display main menu"""
    print(Fore.CYAN + "\nMAIN MENU")
    print("1. Analyze Crypto")
    print("2. Analyze Forex")
    print("3. Settings")
    print("4. Exit" + Fore.RESET)
    
    choice = input("\nChoose: ")
    return choice

def show_settings():
    """Display settings menu"""
    print(Fore.YELLOW + "\nSETTINGS")
    print("1. Change default symbol")
    print("2. Change timeframe")
    print("3. Back to main menu" + Fore.RESET)
    
    choice = input("\nChoose: ")
    return choice
