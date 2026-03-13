"""
Utility functions
"""

import json
from datetime import datetime

def save_to_file(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, default=str)

def load_from_file(filename):
    """Load data from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return None

def format_time(timestamp):
    """Format timestamp"""
    return datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')
