from abc import ABC, abstractmethod
from LivingBeing import LivingBeing

class Plant(LivingBeing, ABC):
    "An animal that grows every round. Requires space to grow."

    def __init__(self, name, reproduction_rate, status, age, life_expectancy, habitat, size, min_size, max_size, size_growth_speed):
        super().__init__(name, reproduction_rate, status, age, life_expectancy, habitat)
        self.size = size
        self.min_size = min_size
        self.max_size = max_size
        self.size_growth_speed = size_growth_speed

    def grow(self):
        """Plant grows based on growth speed."""
        self.new_size = self.size + self.size_growth_speed
        if self.new_size <= self.max_size and self.new_size + self.habitat.occupied_space <= self.habitat:
            self.size += self.size_growth_speed
