from requests import get
from pprint import PrettyPrinter
from dotenv import load_dotenv
import os

load_dotenv()  # Carica .env automaticamente

BASE_URL = f"https://v6.exchangerate-api.com/v6/{os.getenv('api_key_currency_converter')}/latest/USD"

printer = PrettyPrinter()
def get_currencies():
    response = get(BASE_URL)
    data = response.json()['conversion_rates']
    data = list(data.items())
    data.sort()
    return data

def print_currencies(currencies):
    for currency in currencies:
        id,value = currency
        print(f"{id} - {value}")
    
def exchange_rate(currency1, currency2):
    enpoint = f"https://v6.exchangerate-api.com/v6/{os.getenv('api_key_currency_converter')}/pair/{currency1}/{currency2}"
    data = get(enpoint).json()
    if data.get('result') == 'error':
        return f"Error: {data.get('error-type')}"
    else:
        rate = data['conversion_rate']
        print(f"Exchange rate from {currency1} --> {currency2}: {rate}")
        return rate

def convert(amount, currency1, currency2):
    rate = exchange_rate(currency1, currency2)
    if rate == "Error: malformed-request":
        return
    else:
        return f"{amount} {currency1} is equal to {amount * float(rate)} {currency2}"

    

def main():
    currencies = get_currencies()
    print("Welcome to the currency converter!!")
    print("Commands: ")
    print("1. List - lists the different currencies")
    print("2. Convert - converts between two currencies")
    print("3. Rate - gets the exchange rate between two currencies")
    print("4. Exit - exits the program")

    choice = input("Enter a number between 1 and 4: ")
    if choice == "1":
        print_currencies(currencies)
    elif choice == "2":
        currency1 = input("Enter the name of the first currency(only the abbreviation. ie: USD): ").title()
        currency2 = input("Enter the name of the second currency(only the abbreviation. ie: EUR): ").title()
        amount = float(input("Enter the amount: "))
        result = convert(amount, currency1, currency2)
        print(result)
    elif choice == "3":
        currency1 = input("Enter the name of the first currency(only the abbreviation. ie: USD): ").title()
        currency2 = input("Enter the name of the second currency(only the abbreviation. ie: EUR): ").title()
        rate = exchange_rate(currency1, currency2)
        print(rate)
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")
    
if __name__ == "__main__":
    main()




