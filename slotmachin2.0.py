import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

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


def print_slot_machin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_char = " | " if i != len(columns) - 1 else "\n"
            print(column[row], end=end_char)


def deposit():
    while True:
        amount = input('How much would you like to deposit $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            print('Amount must be more than zero')
        else:
            print('Please enter a valid amount of money')


def get_no_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            print('Lines must be more than zero and a maximum of three')
        else:
            print('Please enter a valid amount of lines')


def get_bet():
    while True:
        amount = input('How much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            print(f'Amount must be between ${MIN_BET} and 4{MAX_BET}')
        else:
            print('Please enter a valid amount of money')


def main():
    balance = deposit()

    while True:
        lines = get_no_of_lines()
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            answer = input(
                f'Your bet amount has exceeded your balance of ${balance}. '
                'Would you like to add more money? Yes/no: '
            ).lower()
            if answer == 'yes':
                balance += deposit()
            else:
                print('You cannot proceed without sufficient amount of money')
                break

        print(f'Your balance is ${balance} and you are betting ${bet} on {lines} line(s). Total bet is ${total_bet}')
        if input('Press enter to play (q to quit): ') == 'q':
            break

        balance -= total_bet
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machin(slots)

        won, win_line = check_winnings(slots, lines, bet, symbol_value)
        if won > 0:
            print(f"You won ${won} on lines:", *win_line)
        else:
            print("No wins this round.")

        balance += won
        print(f'Your current balance is ${balance}')

        again = input("Press enter to spin again (enter q to quit): ")
        if again == 'q':
            print(f'Thanks for playing. Your remaining balance is ${balance}')
            break


main()
