"""
Ashley Eidenberger
lab1.py
Problem: Create a program that allows the user to calculate the monthly interest on their credit card.
Certificate of Authenticity: I certify that this assignment is entirely my own work
"""

def monthly_interest():
    annual_interest = eval(input("What is the annual interest rate?: "))
    annual_interest_rate = annual_interest / 100
    monthly_rate = annual_interest_rate / 12

    days_billing_cycle = eval(input("How many days are in the billing cycle?: "))
    net_balance = eval(input("What was the net (previous) balance?: "))
    payment_amount = eval(input("How much was the amount paid?: "))
    day_payment_made = eval(input("On what day was the payment made?: "))

    avg_daily_balance_calc = (net_balance * days_billing_cycle) - (payment_amount * (days_billing_cycle - day_payment_made))
    avg_daily_balance = avg_daily_balance_calc / days_billing_cycle

    month_interest = avg_daily_balance * monthly_rate

    print("Your average monthly interest is:$ ", month_interest)


monthly_interest()
