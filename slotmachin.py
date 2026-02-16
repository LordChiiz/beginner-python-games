import random



MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

symbol_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winnings(columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
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
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        



def deposit():
    while True:
        amount = input('How much would you like to deposit $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be more than zero')
        else:
            print('Please enter a valid amount of money')

    return amount

def get_no_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print('Lines must be more than zero and a maximum of three')
        else:
            print('Please enter a valid amount of lines')

    return lines

def get_bet():
    while True:
        amount = input('How much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} and ${MAX_BET}')
        else:
            print('Please enter a valid amount of money')

    return amount



def main():
    balance =  deposit()
    while True:
        lines = get_no_of_lines()
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            while True:
                answer = input(f'Your bet amount has exceeded you balance of ${balance} . Would you like to add more money to your balance? Yes/no ').lower()
                if answer == 'yes':
                    addbalan = deposit()
                    balance += addbalan
                    break
                else:
                    print('You cannot proceed without sufficient amount of money')
                    continue

        print (f'Your balance is ${balance} and you are betting ${bet} on {lines} line(s). Total bet is ${total_bet}')

        if input('Press enter to play (q to quit)') == 'q': quit()
        balance -= total_bet

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)    
        print_slot_machin(slots)
        won, win_line = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${won} after winning on lines: ", *win_line)
        balance += won
        print(f'Your current balance is ${balance}')
        again = input("Press enter to spin again (enter q to quit) ")
        
        if again == 'q':
            print(f'Thanks for playing. Your remaining balance is ${balance}')
            break
    


main()