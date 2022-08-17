from menu import MenuItem


class CoffeeMaker:
    """
    Represents a Coffee Maker
    """
    UNITS = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g"
    }

    def __init__(self, water=0, milk=0, coffee=0) -> None:
        self._resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    def report(self):
        """
        Prints out a report of all resources.
        """
        for r in self._resources:
            print(f"{r.capitalize()}: {self._resources[r]}{self.UNITS[r]}")

    def have_enough_resources(self, drink: MenuItem):
        """Checks if we have enough resources to make the order.

        Args:
            drink (MenuItem): The drink to make.

        Returns:
            bool: True if we can make the order, False otherwise.
        """
        ingredients = drink._ingredients
        for i in ingredients:
            if ingredients[i] > self._resources[i]:
                print(f"Sorry, there is not enough {i}.")
                return False
        return True

    def make_coffee(self, order: MenuItem):
        """Make the coffee and update the resources data.

        Args:
            order (MenuItem): The order to make.
        """
        ingredients = order._ingredients
        for i in ingredients:
            self._resources[i] -= ingredients[i]

        print(f"Here is your {order._name} ☕️. Enjoy!")
