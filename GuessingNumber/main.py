

from random import randint

def set_difficulty():
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
    
    if level == 'easy':
        return 10
    elif level == 'hard':
        return 5
    else:
        print('Type only \'easy\' or \'hard\'.')
        return set_difficulty()


def guess_number():
    try:
        guess = int(input('Make a guess: '))
    except ValueError:
        print('Type only integer.')
        guess = guess_number()
    return guess


def check_answer(guess, target, turns):
    """Checks answer against guess. Return the number of turns remaining."""
    if guess > target:
        print('Too high.')
        return turns - 1
    elif guess < target:
        print('Too low.')
        return turns - 1
    else:
        print(f'You win! The answer is {target}')
    
    
if __name__ == '__main__':
    print('Welcome to the Number Guessing Game!')
    print('I\'m thingking of a number between 1 and 100.')
    target = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != target:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = guess_number()    
        turns = check_answer(guess, target, turns)
        
        if turns == 0:
            print(f'You\'ve run out of guesses, you lose. The answer is {target}')
            break
        elif guess != target:
            print('Guess again.')
        