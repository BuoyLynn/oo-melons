"""Classes for melon orders."""


class AbstractMelonOrder():
    def __init__(self, species, qty):
        """Initializes an Abstract Melon Class."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0.00

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        # Christmas Melons are more x1.5 expensive than other melons
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


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
