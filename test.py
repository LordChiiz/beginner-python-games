symbols = [
    ['a', 'b', 'c'],
    ['w', 'y', 'z'],
    ['1', '2', '3']
]

# for r in range(len(symbols[0])):
#     for i, any in enumerate(symbols):
#         print (symbols[0][0])

for line in range(3):
    symbol = symbols[0][line]
    print(symbol)
    for column in symbols:
        print(column)
        symbol_to_check = column[line]
        print(f'symbol check {symbol_to_check}')
        
