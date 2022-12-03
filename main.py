from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep
my_coffemaker=CoffeeMaker()
my_moneymachine=MoneyMachine()
my_menu=Menu()
is_on=True
while is_on:
    opcoes=my_menu.get_items()
    my_choice=input(f"what would you like to drink?: {opcoes}\n")
    drink=my_menu.find_drink(my_choice)
    if drink is None and my_choice!='report':
        print("please enter a valid option")
        sleep(2)
        for i in range(10):
            print("\n")
        continue
    elif my_choice=='report':
        my_coffemaker.report()
        my_moneymachine.report()
        continue
    if not my_coffemaker.is_resource_sufficient(drink):
        print("Sorry, we can't make your drink")
        for i in range(20):
            print("\n")
            continue
    if my_moneymachine.make_payment(drink.cost)==False:
        print("insufficient money, poor bastard bitch")
        for i in range(30):
            print("\n")
        continue
    else:
        my_coffemaker.make_coffee(drink)







