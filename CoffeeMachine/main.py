MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report_resources():
    """Report rest resources."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["water"]}ml')
    print(f'Coffee: {resources["water"]}g')
    print(f'Money: {profit}')


def is_enough_resources(choice):
    """Returns True when order can be made, False if ingredients are insufficient."""
    coffee = MENU[choice]['ingredients']
    for ingredient, amount in coffee.items():
        if resources[ingredient] < amount:
            print(f'Sorry, there is not enough {ingredient}.')
            return False
    
    return True
        

def insert_coin():
    """Return the total calculated from coins inserted."""
    print('Please insert coins.')
    wrong_input = True
    while wrong_input:
        try:
            quarters = int(input('How many quarter?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))
            wrong_input = False
        except ValueError:
            print('Type only integer.')
            continue
    
    total_coin = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    
    return total_coin


def is_enough_coins(payment, cost):
    """Return True when the inserted coin is enough, False when not enough."""
    if payment >= cost:
        changes = payment - cost
        print(f'Here is ${changes} dollars in change.')
        return True
    else:
        print('Sorry, that\'s not enough money. Money refunded.')
        return False


def update_resources(choice):
    """Deduct the required ingredients from the rosources."""
    coffee = MENU[choice]
    for ingredient in coffee['ingredients'].keys():
        resources[ingredient] -= coffee['ingredients'][ingredient]
    
    return resources


profit = 0
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if choice == 'report':
        report_resources()
        continue
    elif choice == 'off':
        print('Goodbye.')
        is_on = False
    elif choice not in ['espresso', 'latte', 'cappuccino']:
        print('Type correct menu.')
        continue
    else:
        resources_check = is_enough_resources(choice)
        if resources_check == False:
            is_on = False
        else:
            inserted_coin = insert_coin()
            
            is_enough_pay = is_enough_coins(inserted_coin, MENU[choice]['cost'])
            if is_enough_pay == True:
                resources = update_resources(choice)
                profit += MENU[choice]['cost']
                print(f'Here is your {choice}. Enjoy!')