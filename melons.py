"""Classes for melon orders."""


class AbstractMelonOrder():
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0.00

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
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

    # def __repr__(self):
    #     return f"{self.species}\n{self.qty}\n{self.shipped}\n{self.tax}\n{self.order_type}\n{self.country_code}"
