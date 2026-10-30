"""Tiny shopping helpers used in the issue tracking lab."""

def total(prices):
    return sum(prices)

def apply_discount(total_price, percent):
    return total_price * ( 1 - percent / 100)

def add_tax(price, rate):
    return round(price * (1 + rate / 100), 2)


