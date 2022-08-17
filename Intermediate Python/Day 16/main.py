from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_handler import MoneyHandler


def get_coffee(menu: Menu, coffee_maker: CoffeeMaker, money_handler: MoneyHandler):
    menu_items = menu.get_items()
    print(f"Our coffees: {menu_items}")
    coffee = input("What would you like?: ").strip().lower()

    if coffee == "off":
        return False

    elif coffee == "report":
        coffee_maker.report()

    else:
        while coffee not in menu.menu_names():
            print(f"We do not have {coffee}.")
            coffee = input("What would you like?: ").strip().lower()

        coffee = menu.find_drink(coffee)

        if coffee_maker.have_enough_resources(coffee):
            print("Please insert coins.")
            cost = coffee._cost

            if money_handler.make_payment(cost):
                coffee_maker.make_coffee(coffee)

    return True


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker(300, 200, 100)
    money_handler = MoneyHandler()

    running = True
    while running:
        running = get_coffee(menu, coffee_maker, money_handler)

    print("Coffee Maker has been turned off.")


if __name__ == "__main__":
    main()
