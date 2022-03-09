import arts
import game_data
import random
import os

def choose_target(history):
    
    is_duplicated = True
    while is_duplicated:
        target_index = random.randint(0, len(data))
        if target_index not in history:
            is_duplicated = False
        
    target = data[target_index]
    name = target['name']
    follower = target['follower_count']
    history.append(target_index)
    
    return name, follower, history


def guess_answer():
    answer = input(f'Chose more follower! \nA : {first_name}, B : {second_name}. Answer? ').upper()
    
    if answer not in ['A', 'B']:
        print('Type only \'A\' or \'B\'')
        answer = guess_answer()
    
    return answer


def check_answer(first_follower, second_follower, answer):
    
    if answer == 'A':
        if first_follower > second_follower:
            result = True
        else:
            result = False
    
    elif answer == 'B':
        if first_follower < second_follower:
            result = True
        else:
            result = False
    
    return result


if __name__ == '__main__':
    data = game_data.data
    logo = arts.logo
    vs = arts.vs

    print(logo)

    score = 0
    history = []
    result = True
    while result:
        if score == 0:
            first_name, first_follower, history = choose_target(history)
        else:
            first_name, first_follower = second_name, second_follower
        
        print(f'Your current score is {score}')
        
        print(f'\"{first_name}\" has {first_follower}')
        print(vs)

        second_name, second_follower, history = choose_target(history)
        
        answer = guess_answer()
        result = check_answer(first_follower, second_follower, answer)
        score += result
        
        os.system('clear')
        if not result:
            print(f'No...')
        else:
            print(f'Yes!')
        print(f'\"{first_name}\" : {first_follower} vs \"{second_name}\" : {second_follower}')
        print('='*60)
        
        # game data를 모두 다 썼을 때는 종료
        if len(history) == len(data):
            break
    
    print(f'Your final score is {score}')
    print('Goodbye')