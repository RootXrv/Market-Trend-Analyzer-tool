"""
Simple alert system
"""

import time

class AlertSystem:
    def __init__(self):
        self.alerts = []
    
    def add_alert(self, symbol, condition, message):
        """Add a new alert"""
        self.alerts.append({
            'symbol': symbol,
            'condition': condition,
            'message': message,
            'triggered': False
        })
    
    def check_alerts(self, current_data):
        """Check if any alerts should trigger"""
        triggered = []
        for alert in self.alerts:
            if not alert['triggered']:
                # Simple price check
                if alert['condition'] == 'above' and current_data > alert['price']:
                    alert['triggered'] = True
                    triggered.append(alert['message'])
        
        return triggered
