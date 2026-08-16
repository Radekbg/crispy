from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()

coffe_machine.report()
money_machine.report()

menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? \n({options}): ".lower())
    drink = menu.find_drink(choice)
    if coffe_machine.is_resource_sufficient(drink):
        print("Resources are sufficient")
        print(drink.name)
        print(drink.cost)
        payment = float(input("Please proceed with payment.\n"))
        print(payment)
        if payment > drink.cost:
            change = payment - drink.cost
            print(f"Here is ${change:.2f} in change.")
            coffe_machine.make_coffee(drink)
        elif payment == drink.cost:
            print("Your drink is on the way.")
            coffe_machine.make_coffee(drink)
        else:
            print("Sorry, payment is not sufficient.")
    else:
        print("Sorry, coffee is not sufficient")