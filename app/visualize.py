"""
Visualization of Financial Data

Uses Matplotlib to create graphs for savings, investments, etc.
"""

import matplotlib.pyplot as plt

def plot_savings_trend(months, amounts):
    plt.plot(months, amounts, label="Savings")
    plt.title("Savings Over Time")
    plt.xlabel("Months")
    plt.ylabel("Amount Saved ($)")
    plt.legend()
    plt.show()

""" Example Usage:
    months = [1, 2, 3, 4, 5]
    amounts = [50, 100, 150, 200, 250]
    plot_savings_trend(months, amounts)
"""
