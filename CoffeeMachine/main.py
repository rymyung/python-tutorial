from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_machine = CoffeeMaker()
my_coffee_menu = Menu()
my_money_machine = MoneyMachine()

is_on = True
while is_on:
    options = my_coffee_menu.get_items()
    choice = input(f'What would you like? {options}: ').lower()
    if choice == 'report':
        my_coffee_machine.report()
        my_money_machine.report()
    elif choice == 'off':
        print('Goodbye.')
        is_on = False
    else:
        ordered_drink = my_coffee_menu.find_drink(choice)
        if ordered_drink == None:
            continue
        else:
            is_enough_resource = my_coffee_machine.is_resource_sufficient(ordered_drink)
            if not is_enough_resource:
                break
            else:
                is_money_acceptable = my_money_machine.make_payment(ordered_drink.cost)
                if is_money_acceptable:
                    my_coffee_machine.make_coffee(ordered_drink)

