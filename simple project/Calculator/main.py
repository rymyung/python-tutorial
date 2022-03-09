

from numpy import double


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    num1 = float(input('What\'s the first number?: '))
    for symbol in operations:
        print(symbol)
        
    is_continue = True
    while is_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))

        operation_func = operations[operation_symbol]
        answer = operation_func(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        
        check = input(f'Type \'y\' to continue calculating with {answer}, or type \'n\' to start a new calculation, or type \'x\' to exit.: ')
        if check == 'y':
            num1 = answer
        elif check == 'n':
            is_continue = False
            calculator()
        else:
            is_continue = False
            print('Goodbye.')


if __name__ == '__main__':
    
    logo = """
    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)
    
    operations = {
        '+': add,
        '-': substract,
        '*': multiply,
        '/': divide
    }   
    
    calculator()