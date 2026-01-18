from abc import ABC, abstractmethod
from LivingBeing import LivingBeing

class Animal(LivingBeing, ABC):
    "An animal, that requires food to survive."

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat, food_requirement):
        super().__init__(name, reproduction_rate, age, life_expectancy, habitat)
        self.food_requirement = food_requirement
        self.food = food_requirement * 2
        self.injury_time = 0

    def eat(self):
        self.food -= self.food_requirement