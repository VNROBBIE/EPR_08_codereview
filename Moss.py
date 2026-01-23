__author__ = "8572770, Kesidis, 8724694, Tran"
from Plant import Plant


class Moss(Plant):
    """Mosses do not occupy space in the habitat and can not reproduce."""

    def __init__(self, name):
        """Initializes an instance of moss."""
        super().__init__(name)
        self.age = 0
        self.size = 20
        self.min_size = 10
        self.max_size = float("inf")
        self.size_growth_speed = 3
