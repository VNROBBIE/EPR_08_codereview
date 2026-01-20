from abc import ABC, abstractmethod
from LivingBeing import LivingBeing

class Animal(LivingBeing, ABC):
    """An animal, that requires food to survive."""

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat, food_requirement):
        super().__init__(name, reproduction_rate, age, life_expectancy, habitat)
        self.food_requirement = food_requirement
        self.food = food_requirement * 2
        self.injury_time = 0

    @abstractmethod
    def gather_food(self):
        pass

    def eat(self):
        """Consumes current food amount. Animal gets hungry and then starves if too low on food."""
        self.food -= self.food_requirement
        if self.food < 0:
            self.food = 0
            if "hungry" not in self.status:
                self.status.add("hungry")
                print(self.name + " did not find enough food and is hungry.")
            else:
                self.status.add("starved")
        elif "hungry" in self.status:
            self.status.remove("hungry")

