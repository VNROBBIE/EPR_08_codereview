from Plant import Plant

class Flower(Plant):
    """Flowers have a high reproduction rate compared to other plants."""

    def __init__(self, name, age, life_expectancy, size, min_size, max_size, size_growth_speed):
        super().__init__(name, age, life_expectancy, size, min_size, max_size, size_growth_speed)
        self.reproduction_rate = 4
