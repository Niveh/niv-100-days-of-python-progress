class MenuItem:
    """
    Represents a Menu item.
    """

    def __init__(self, name, water, milk, coffee, cost) -> None:
        self._name = name
        self._cost = cost
        self._ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Represents the Menu.
    """

    def __init__(self) -> None:
        self._menu = [
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("cappuccino", 250, 100, 24, 3.0)
        ]

    def menu_names(self):
        return [i._name for i in self._menu]

    def get_items(self):
        return "/".join(self.menu_names())

    def find_drink(self, order_name: str):
        for item in self._menu:
            if order_name == item._name:
                return item
        print(f'Sorry, "{order_name}" is not available.')
