# Simple Currency Converter Tool

def convert_currency(amount, from_currency, to_currency):
    rates = {
        "PKR": 1.0,
        "USD": 277.0,
        "INR": 3.35,
        "EUR": 300.0
    }

    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported."

    converted = (amount / rates[from_currency]) * rates[to_currency]
    return round(converted, 2)


# 👇 User Interface
print("Welcome to Simple Currency Converter (PKR ⇄ USD, INR, EUR)")
amount = float(input("Enter amount: "))
from_currency = input("From Currency (PKR, USD, INR, EUR): ").upper()
to_currency = input("To Currency (PKR, USD, INR, EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(f"\n{amount} {from_currency} = {result} {to_currency}")
