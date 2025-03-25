import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much are you willing to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid input. Please enter number greater than 0.")
        else:
            print("Invalid input. Please enter a number.")

    return amount


def get_numbers_of_lines():
    while True:
        lines = input(
            "Enter the numbers of lines you want to bet on (1 -" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Invalid input. Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("Enter your bet (between $" + str(MIN_BET) +
                       " and $" + str(MAX_BET) + ")? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Invalid input. Please enter a bet between $" +
                      str(MIN_BET) + " and $" + str(MAX_BET) + ".")
        else:
            print("Invalid input. Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"Insufficient funds. Please deposit more.Your current balance is ${balance}.")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. You total bet is ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
 