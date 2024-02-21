MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


machine = True
continu = True
Money = 0


def report():
    for i in resources:
        print(f"{i} = {resources[i]}")
    print(f"Money= {Money}€")


def refill():
    global resources
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def process(type, cost):
    global resources
    global Money
    for i in type["ingredients"]:
        resources[i] -= type["ingredients"][i]
    Money += cost


def payment(cost):
    ten = int(input("How many 10 cents coins:"))
    twenty = int(input("How many 20 cents coins:"))
    fifty = int(input("How many 50 cents coins:"))
    total = round((ten/10 + twenty/5 + fifty/2), 2)
    if total > cost:
        change = round((total - cost), 2)
        print(f"Transaction successfully completed!\nHere is your change of:{change}€")
        return True
    elif total == cost:
        print("Transaction successfully completed!")
        return True
    else:
        print("Sorry that's not enough money")
        return False


def check_resource (type):
    if resources["water"] < type["ingredients"]["water"]:
        print(f"Sorry, not enough water")
        return False

    if resources["milk"] < type["ingredients"]["milk"]:
        print(f"Sorry, not enough milk")
        return False

    if resources["coffee"] < type["ingredients"]["coffee"]:
        print(f"Sorry, not enough coffee")
        return False

    else:
        return True


def checking(type):
    if check_resource(type=type) == False:
        return False
    else:
        if payment(cost=type["cost"]) == False:
            return False
        else:
            return True


def step_a(choice):
    global continu
    while continu:
            if choice == "espresso":
                if checking(type=MENU[choice]) == False:
                    continu = False
                else:
                    process(type=MENU[choice] , cost=MENU[choice]["cost"])
                    print (f"Enjoy your {choice}!")
                    continu = False

            elif choice == "latte":
                if checking(type=MENU[choice]) == False:
                    continu = False
                else:
                    process(type=MENU[choice], cost=MENU[choice]["cost"])
                    print(f"Enjoy your {choice}!")
                    continu = False

            elif choice == "cappuccino":
                if checking(type=MENU[choice]) == False:
                    continu = False
                else:
                    process(type=MENU[choice], cost=MENU[choice]["cost"])
                    print(f"Enjoy your {choice}!")
                    continu = False

            else:
                print("Didn't get what you mean, try again.")
                continu= False


while machine:
    continu = True
    choice = input("What would you like today?:\n1.Espresso 1,50€\n2.Latte 2,50€\n3.Cappuccino 3,00€\nEnter:").lower()
    if choice == "off":
        machine = False

    elif choice == "report":
        report()

    elif choice == "refill":
        refill()
        print ("Refilled!")

