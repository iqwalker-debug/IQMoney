"""
Budget Management Module

Handles income, expense logging, and remaining budget calculation.
"""

class Budget:
    def __init__(self, income):
        self.income = income
        self.expenses = []

    def add_expense(self, name, amount):
        self.expenses.append((name, amount))

    def remaining_budget(self):
        spent = sum(amount for _, amount in self.expenses)
        return self.income - spent

""" Example Usage:
    budget = Budget(1000)
    budget.add_expense("Rent", 500)
    budget.add_expense("Food", 200)
    print(budget.remaining_budget())
"""
