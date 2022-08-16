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

COINS = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01
}

UNITS = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g"
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

income = 0


def show_resources():
    for r in resources:
        print(f"{r.capitalize()}: {resources[r]}{UNITS[r]}")

    print(f"Money: ${income}")


def have_enough_resources(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for i in ingredients:
        required = ingredients[i]
        if resources[i] - required < 0:
            print(f"Sorry, there is not enough {i}")
            return False

    return True


def have_enough_money(money, coffee_cost):
    if money < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    return True


def handle_change(money, coffee_cost):
    global income
    if money > coffee_cost:
        change = money - coffee_cost
        print(f"Here is ${change:.2f} in change.")

    income += coffee_cost


def make_coffee(coffee):
    global resources
    ingredients = MENU[coffee]["ingredients"]
    for i in ingredients:
        required = ingredients[i]
        resources[i] -= required

    print(f"Here is your {coffee}. Enjoy!")


def get_coffee(coffee_list):
    print(f"Our coffees: {'/'.join(coffee_list)}")
    coffee = input("What would you like?: ").strip().lower()

    if coffee == "off":
        return False

    elif coffee == "report":
        show_resources()

    else:
        while coffee not in coffee_list:
            print(f"We do not have {coffee}.")
            coffee = input("What would you like?: ").strip().lower()

        if have_enough_resources(coffee):
            print("Please insert coins.")
            money = get_money()
            coffee_cost = MENU[coffee]["cost"]

            if have_enough_money(money, coffee_cost):
                handle_change(money, coffee_cost)
                make_coffee(coffee)

    return True


def get_money():
    quarters = int(input("How many quarters?: ")) * COINS["quarter"]
    dimes = int(input("How many dimes?: ")) * COINS["dime"]
    nickles = int(input("How many nickles?: ")) * COINS["nickle"]
    pennies = int(input("How many pennies?: ")) * COINS["penny"]

    return quarters + dimes + nickles + pennies


def main():
    machine_working = True
    while machine_working:
        coffee_list = list(MENU.keys())
        machine_working = get_coffee(coffee_list)

    print("Coffee Maker has been turned off.")


if __name__ == "__main__":
    main()
