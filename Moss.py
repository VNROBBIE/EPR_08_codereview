from Plant import Plant

class Moss(Plant):
    """Mosses do not occupy space in the habitat and can only grow, not reproduce."""

    def __init__(self, name, age, life_expectancy, size, min_size, size_growth_speed):
        super().__init__(name, age, life_expectancy, size, min_size, size_growth_speed)
        self.max_size = float("inf")
        self.reproduction_rate = 0