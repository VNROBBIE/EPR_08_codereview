from abc import ABC
from LivingBeing import LivingBeing

class Plant(LivingBeing, ABC):
    "An animal that grows every round. Requires space to grow."

    def __init__(self, name, reproduction_rate, status, age, life_expectancy, size, min_size, max_size, size_growth_speed):
        super().__init__(name, reproduction_rate, status, age, life_expectancy)
        self.size = size
        self.min_size = min_size
        self.max_size = max_size
        self.size_growth_speed = size_growth_speed

    def grow(self):
        """Plant grows based on its set growth speed."""
        self.new_size = self.size + self.size_growth_speed
        return self.new_size
