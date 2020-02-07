"""Classes for melon orders."""

from random import randint
# Datetime has a datetime module within the class, "as dt" helps clarify which
# datetime you are using within the code
from datetime import datetime as dt


class AbstractMelonOrder():
    def __init__(self, species, qty):
        """Initializes an Abstract Melon Class."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0.00
        # Adds a timestamp attribute when you instantiate any melon
        self.timestamp = dt.now()

    def get_base_price(self):
        """Calculate splurge pricing."""

        base_price = randint(5, 9)

        # Rush hour: add $4 to any order made during 8-11 AM, M-F
        
        # # List of weekday mapped ints
        # weekday = []

        # for day in timestamp:
        #     if day == weekday:
        #         if (time > 8 AM) and (time < 11 AM):
        #             base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        # Christmas Melons are more x1.5 expensive than other melons
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    # implement TooManyMelonsError Exception (subclass to ValueError)
    # print "No more than 100 melons!" as optional msg arg

    def __repr__(self):
        return f"{self.timestamp}"


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

    # def __repr__(self):
    #     return f"{self.tax}"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Updating get_total to add a flat $3 fee to intl orders with < 10 melons"""

        total = super().get_total()
        if self.qty < 10:
            total += 3.00
        return total

    # def __repr__(self):
    #     return f"{self.species}\n{self.qty}\n{self.shipped}\n{self.tax}\n{self.order_type}\n{self.country_code}"


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order. Govt orders are tax-exempt."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Update a melon's inspection status with a Boolean."""

        self.passed_inspection = passed
