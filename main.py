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
    "Money": 0
}


def receive_money():
    print("Please enter coins.")
    quarter = int(input(print("How many quarter? "))) * 0.25
    dime = int(input(print("How many dime? "))) * 0.10
    nickel = int(input(print("How many nickel? "))) * 0.05
    penny = int(input(print("How many penny? "))) * 0.01
    return quarter + dime + nickel + penny


def check_transaction(r, o):
    if r < price:
        print("Not enough money. Money refunded")
        return False
    elif r > price:
        change = round(r - price, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {o} Enjoy!")
        return True


def update_resource(a):
    resources["water"] = resources["water"] - MENU[a]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[a]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - MENU[a]["ingredients"]["milk"]
    resources["Money"] = resources["Money"] + MENU[a]["cost"]


def sufficient_resource(b):
    if resources["water"]<MENU[b]["ingredients"]["water"] or resources["coffee"]<MENU[b]["ingredients"]["coffee"] or resources["milk"]<MENU[b]["ingredients"]["milk"]:
        return False
    else:
        return True


def process_order(ordName):
    global price
    if sufficient_resource(ordName):
        price = MENU[ordName]["cost"]
        received = receive_money()
        if check_transaction(received, ordName):
            update_resource(ordName)
    else:
        print("Sorry, not enough resources")


def coffe_machine():
    global price
    on = True
    while on:
        order = input(print("What would you like? (espresso/latte/cappuccino): ")).lower()
        if order == "off":
            on = False
        elif order == "report":
            for i in resources:
                print(f"{i} = {resources[i]}")
        else:
            process_order(order)


coffe_machine()
