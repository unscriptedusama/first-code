# Corrected Currency Converter Tool

def convert_currency(amount, from_currency, to_currency):
    rates_in_pkr = {
        "PKR": 1.0,
        "USD": 277.0,
        "INR": 3.35,
        "EUR": 300.0
    }

    if from_currency not in rates_in_pkr or to_currency not in rates_in_pkr:
        return "Currency not supported."

    # Convert from source currency to PKR, then to target currency
    amount_in_pkr = amount * rates_in_pkr[from_currency]
    converted = amount_in_pkr / rates_in_pkr[to_currency]
    return round(converted, 2)


# 👇 User Interface
print("Welcome to Simple Currency Converter (PKR ⇄ USD, INR, EUR)")
amount = float(input("Enter amount: "))
from_currency = input("From Currency (PKR, USD, INR, EUR): ").upper()
to_currency = input("To Currency (PKR, USD, INR, EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(f"\n{amount} {from_currency} = {result} {to_currency}")
