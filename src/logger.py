"""
Simple logging system
"""

from datetime import datetime

class Logger:
    def __init__(self, log_file='app.log'):
        self.log_file = log_file
    
    def log(self, message, level='INFO'):
        """Write to log file"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {level}: {message}\n")
    
    def error(self, message):
        """Log error"""
        self.log(message, 'ERROR')
    
    def info(self, message):
        """Log info"""
        self.log(message, 'INFO')
