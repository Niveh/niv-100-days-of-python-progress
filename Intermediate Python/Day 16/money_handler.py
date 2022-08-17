class MoneyHandler:
    CURRENCY = "$"
    COINS = {
        "quarter": 0.25,
        "dime": 0.1,
        "nickle": 0.05,
        "penny": 0.01
    }

    def __init__(self, profit=0) -> None:
        self._profit = profit
        self._money_received = 0

    def __process_coins(self):
        """Private function to process coins input and update total money received.
        """
        quarters = int(input("How many quarters?: ")) * self.COINS["quarter"]
        dimes = int(input("How many dimes?: ")) * self.COINS["dime"]
        nickles = int(input("How many nickles?: ")) * self.COINS["nickle"]
        pennies = int(input("How many pennies?: ")) * self.COINS["penny"]

        self._money_received = quarters + dimes + nickles + pennies

    def __validate_money(self, cost: float):
        """
        Private function to check if the machine received enough money for the current transaction.

        Args:
                cost (float): The cost of the item.

        Returns:
                bool: True if money is sufficient, False otherwise.
        """
        if self._money_received < cost:
            print("Sorry, that's not enough money. Money refunded.")
            self._money_received = 0
            return False
        return True

    def __handle_change(self, cost):
        """
        Private function to print out the returned change if needed.

        Args:
                cost (float): The cost of the item.
        """
        if self._money_received > cost:
            change = self._money_received - cost
            print(f"Here is {self.CURRENCY}{change:.2f} in change.")

    def make_payment(self, cost):
        """
        Makes a payment using the given item's price.

        Args:
            cost (float): The price of the item.

        Returns:
            bool: True when payment is accepted, False otherwise.
        """
        self.__process_coins()
        if self.__validate_money(cost):
            self.__handle_change(cost)
            self._profit += cost
            self._money_received = 0
            return True

        return False
