import copy
from abc import ABC, abstractmethod
from LivingBeing import LivingBeing

class Animal(LivingBeing, ABC):
    """An animal, that requires food to survive."""

    def __init__(self, name, reproduction_rate, age, food_requirement):
        """Initialize new animal."""
        super().__init__(name, reproduction_rate, age)
        self.food_requirement = food_requirement
        self.food = food_requirement * 1.5
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

    def reproduce(self, season):
        """Creates a copy of current living being, if reproduction progress reaches 1."""
        #  Reproduction halts in winter.
        if season != 3:
            #  Offspring has default values and age is set to 0.
            if self.reproduction_progress >= 1:
                self.offspring_number += 1
                #  Reset reproduction progress.
                self.reproduction_progress -= 1
                offspring = copy.deepcopy(self)
                #  Bears same name as its parent, but enumerated.
                offspring.name = str(self.name + " (" + self.offspring_number + ")")
                offspring.offspring_number = 0
                offspring.status = set()
                offspring.age = 0
                offspring.food = offspring.food_requirement * 2
                return offspring