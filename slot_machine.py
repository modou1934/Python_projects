import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit() and int(amount) > 0:
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    return amount
def get_number_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("lines must be greater than 0")
        else:
            print("Invalid number of lines. Please enter a number between 1 and " + str(MAX_LINES) + ".")
    return lines
def get_bet():
    while True:
        amount = input("Enter the amount to bet: $")
        if amount.isdigit() and int(amount) > 0:
            amount= int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else:
                print("amount must be betwen $" + str(MIN_BET) + " and $" + str(MAX_BET) + ".")
        else:
            print("Invalid bet amount. Please enter a positive number.")
    return amount

def main():
    balance = deposit()
    lines= get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break
    print(f"You have deposited: ${balance}. You are betting {bet} on {lines}. Total bet = ${total_bet}")

if __name__ == "__main__":
    main()