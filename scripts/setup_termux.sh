#!/data/data/com.termux/files/usr/bin/bash
echo "Setting up for Termux..."
pkg install python
pkg install git
pip install -r requirements.txt
echo "Setup complete! Run: python src/market_analyzer.py"
