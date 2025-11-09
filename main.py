from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on=True
while on:
    option = input("Would you like to order a coffee(c), check money colle3cted (m), check ingredients left(i), or turn the machine off(o): ").lower()
    if option == "i":
        ingredient_report = coffee_maker.report()
    elif option == "m":
        money_report = money_machine.report()
    elif option == "c":
        picking =True
        while picking:
            question = menu.get_items()
            choice = input(f"Would you like a {question}: ")
            coffee = menu.find_drink(choice)
            if coffee is None:
                print("Invalid Drink try again")
            else:
                continues = coffee_maker.is_resource_sufficient(coffee)
                name = coffee.name
                cost = float(coffee.cost)
                ingredients = coffee.ingredients

                if continues:
                    print(f"Cost of {name} is {cost}")
                    paying=True
                    while paying:
                        try:
                            paid = money_machine.make_payment(coffee.cost)
                            if paid:
                                coffee_maker.make_coffee(coffee)
                                print(f"Your coffee has been paid for here is your {coffee.name}")
                                break
                        except ValueError:
                            print("Please enter a valid amount of money as a number")

                else:
                    print(f"Not enough ingredients to make {name} ")
                break


    elif option == "o":
        print("Thank you for using the coffee machine")
        print("Turning coffee machine off")
        time.sleep(2)
        print("Machine Off")
        break
    else:
        print("Invalid option enter 'c','m','i',or 'o'")

