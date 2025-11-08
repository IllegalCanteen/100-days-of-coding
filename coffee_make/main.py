import time
from art import title


menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":200,
            "milk":100,
            "coffee":24
        },
        "cost":3.0,
    }

}
def coffee_machine():
    on=True
    water = 300.0
    milk = 200.0
    coffee = 100.0
    money = 0.0
    while on:
        selection = input("Would you like to order a coffee(c), turn the machine off(o) or check the machines report(r): ").lower()
        if selection == "o":
            print("Turning machine off")
            time.sleep(1)
            print("Machine off")
            return
        elif selection == "c":
            picking = True
            while picking:
                choice = input("What would you like: an espresso, latte or cappuccino ☕: ").lower()
                try:
                    if water < menu[choice]["ingredients"].get("water", 0.0):
                        print("Not enough water to make coffee😭")
                        print("Turning machine off to refill ingredients")
                        return
                    elif milk < menu[choice]["ingredients"].get("milk", 0):
                        print("Not enough milk to make coffee😭")
                        print("Turning machine off to refill ingredients")
                        return
                    elif coffee < menu[choice]["ingredients"].get("coffee", 0):
                        print("Not enough coffee powder to make coffee😭")
                        print("Turning machine off to refill ingredients")
                        return
                    else:
                        cost = menu[choice]["cost"]
                        print(f"Amount to pay: ${cost}  ")
                        quarters = int(input("How many quarters?: "))
                        dimes = int(input("How many dimes?: "))
                        nickels = int(input("How many nickles?: "))
                        pennies = int(input("How many pennies?: "))
                        total_paid = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

                        if total_paid == cost:
                            print("Your coffee is paid")
                            print(f"Making {choice}")
                            time.sleep(2)
                            print(f"Here is your {choice} ☕")
                            water -= menu[choice]["ingredients"].get("water", 0.0)
                            milk -= menu[choice]["ingredients"].get("milk", 0.0)
                            coffee -= menu[choice]["ingredients"].get("coffee", 0.0)
                            money += menu[choice]["cost"]
                        elif total_paid > cost:
                            change=total_paid-cost
                            print(f"Paid extra paying you back change of ${change} ")
                            print(f"Making {choice}")
                            time.sleep(2)
                            print(f"Here is your {choice} ☕")
                            water -= menu[choice]["ingredients"].get("water", 0.0)
                            milk -= menu[choice]["ingredients"].get("milk", 0.0)
                            coffee -= menu[choice]["ingredients"].get("coffee", 0.0)
                            money += menu[choice]["cost"]
                        elif total_paid < cost:
                            print(f"Money not sufficient repaying you back ${total_paid} you paid 😊")


                        break
                except KeyError:
                    print("Not a valid choice enter espresso, latte or cappuccino 😊")
        elif selection == "r":
            print(f"Water : {water} ml")
            print(f"Milk : {milk} ml")
            print(f"Coffee powder : {coffee}g")
            print(f"Money : ${money}")
        else:
            print("Invalid input try again")
print(title)
coffee_machine()