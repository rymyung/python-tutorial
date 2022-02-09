
import random
import os
import collections

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawed_card = random.choice(cards)
    
    return drawed_card

def calculate_score(deck):
    score = sum(deck)
    if score > 21 and 11 in deck:
        return score - 10
    else:
        return score

def compare(my_score, dealer_score):
    if my_score > 21 and dealer_score > 21:
        result = 'Draw, Both score above 21!'
    elif my_score > 21:
        result = 'Lose, Your score is above 21!'
    elif dealer_score > 21:
        result = 'Win, Dealer score is above 21!'
    elif my_score == dealer_score:
        result = 'Draw, Same score.'
    elif my_score > dealer_score:
        result = 'Win!'
    elif my_score < dealer_score:
        result = 'Lose!'
    
    return result


def play_blackjack():
    my_deck = [draw_card() for _ in range(2)]
    dealer_deck = [draw_card() for _ in range(2)]

    continue_draw = True
    while continue_draw:
        os.system('clear')
        
        # 점수 계산
        my_score = calculate_score(my_deck)
        dealer_score = calculate_score(dealer_deck)
        
        print(f'Dealer\'s first card is : {dealer_deck[0]}')
        print(f'Your deck is : {my_deck}, current score is {my_score}')
        
        # 둘 중 하나가 21점 이상이면 카드뽑기 중단
        if my_score >= 21 or dealer_score >= 21:
            break
        
        # 딜러는 16점 이하일 경우 무조건 카드 뽑기
        if dealer_score < 17:
            dealer_deck.append(draw_card())

        # 플레이어 카드 뽑기 여부 결정
        add_card = input('Type \'y\' to get another card, type \'n\' to pass: ')
        if add_card == 'y':
            my_deck.append(draw_card())

        elif add_card == 'n':
            continue_draw = False
            dealer_score = calculate_score(dealer_deck)
            os.system('clear')
            print('Draw phase is done. Let\'s check it out!')
            
    
    result = compare(my_score, dealer_score)

    print(f'Your deck : {my_deck}, Dealer\'s deck : {dealer_deck}')
    print(f'Your score : {my_score}, Dealer\'s score : {dealer_score}')
    print(f'You {result}!')


def simul_compare(my_score, dealer_score):
    if my_score > 21 and dealer_score > 21:
        result = 0
    elif my_score > 21:
        result = -1
    elif dealer_score > 21:
        result = 1
    elif my_score == dealer_score:
        result = 0
    elif my_score < dealer_score:
        result = -1
    elif my_score > dealer_score:
        result = 1
    
    return result

def simul_blackjack(base_score):
    my_deck = [draw_card() for _ in range(2)]
    dealer_deck = [draw_card() for _ in range(2)]

    continue_draw = True
    while continue_draw:
        
        # 점수 계산
        my_score = calculate_score(my_deck)
        dealer_score = calculate_score(dealer_deck)
        
        # 둘 중 하나가 21점 이상이면 카드뽑기 중단
        if my_score >= 21 or dealer_score >= 21:
            break
        
        # 딜러는 16점 이하일 경우 무조건 카드 뽑기
        if dealer_score < 17:
            dealer_deck.append(draw_card())

        # 플레이어 카드 뽑기 여부 결정
        if my_score <= base_score:
            my_deck.append(draw_card())

        else:
            continue_draw = False
            dealer_score = calculate_score(dealer_deck)
    
    result = simul_compare(my_score, dealer_score)
    
    return result
    
    
'''
if __name__ == '__main__':

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    print(logo)

    continue_game = True
    while continue_game:
        check = input('Type \'y\' to start new game, or type \'n\' to exit: ')
        if check == 'y':
            os.system('clear')
            play_blackjack()
        elif check == 'n':
            print('Goodbye.')
            continue_game = False
        else:
            print('Type only \'y\' or \'n\'.')
'''

if __name__ == '__main__':
    # base_score 이하일 때 카드 뽑기를 할 경우 승률 시뮬레이션
    simul_result = {}
    simul_times = 1000
    for base_score in range(1, 21):
        simul_list = [simul_blackjack(base_score) for _ in range(simul_times)]
        simul_result[base_score] = simul_list
    
    simul_rates = {}
    for k, v in simul_result.items():
        rates = collections.Counter(simul_result[k])
        simul_rates[k] = [rates[1]/simul_times, rates[0]/simul_times, rates[-1]/simul_times]
    
    for base_score, rate in simul_rates.items():
        print(f'Base score : {base_score}, Winning rate : {rate[0]}, Draw rate : {rate[1]}, Lose rate : {rate[2]}')
    
    