__author__ = "8572770, Kesidis, 8724694, Tran"
from Plant import Plant


class Flower(Plant):
    """Flowers have a high reproduction rate compared to other plants."""

    def __init__(self, name):
        """Initializes a flower."""
        super().__init__(name)
        self.reproduction_rate = 1.5
        self.size = 5
        self.min_size = 3
        self.max_size = 10
        self.size_growth_speed = 1
