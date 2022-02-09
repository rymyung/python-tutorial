import arts
import game_data
import random

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
    answer = input(f'Does \"{second_name}\" has more follower than \"{first_name}\"? Choose higher or lower: ').lower()
    
    if answer not in ['higher', 'lower']:
        print('Type only \'higher\' or \'lower\'')
        answer = guess_answer()
    
    return answer


def check_answer(first_follower, second_follower, answer):
    
    if answer == 'higher':
        if first_follower < second_follower:
            result = True
        else:
            result = False
    elif answer == 'lower':
        if first_follower > second_follower:
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

        if not result:
            print(f'No...')
        else:
            print(f'Yes!')
        print(f'\"{first_name}\" : {first_follower} vs \"{second_name}\" : {second_follower}')
        print('='*50)
        
        # game data를 모두 다 썼을 때는 종료
        if len(history) == len(data):
            break
    
    print(f'Your final score is {score}')