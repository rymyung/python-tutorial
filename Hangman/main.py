
import os
import random
import words
import arts

logo = arts.logo
stages = arts.stages

print(logo)

word_list = words.word_list
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = len(stages)-1
is_game_end = False
while not is_game_end:
    guess = input('Guess a letter: ').lower()
    
    os.system('clear')
    
    if guess in display:
        print(f'A {guess} is already answered. \nPlease guess different letter.')
        continue
    
    else:
        if guess in chosen_word:
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display[i] = guess
        else:
            lives -= 1
    
        print(stages[lives])
        print(display)

        if '_' not in display:
            is_game_end = True
            print('You win.')
        
        elif lives == 0:
            is_game_end = True
            print('You lose.')
            print(f'The chosen word is {chosen_word}')
