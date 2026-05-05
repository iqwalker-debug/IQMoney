"""
Investment Growth Calculator

Calculates compound interest to show the growth of investments.
"""

def calculate_compound_interest(principal, rate, periods):
    return principal * (1 + rate) ** periods

""" Example Usage:
    investment = calculate_compound_interest(1000, 0.05, 10)
    print(investment)  # Output: Amount after 10 periods
"""
