"""
Savings Simulation Module

Simulates "pay yourself" subscriptions for savings.
"""

class SavingsSubscription:
    def __init__(self, name, amount, frequency):
        self.name = name
        self.amount = amount
        self.frequency = frequency
        self.total_saved = 0

    def save(self, periods):
        self.total_saved += self.amount * periods
        return self.total_saved

""" Example Usage:
    subscription = SavingsSubscription("Emergency Fund", 50, "monthly")
    print(subscription.save(6))  # Save for 6 months
"""
