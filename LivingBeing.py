from abc import ABC, abstractmethod

class LivingBeing(ABC):
    "A living being, that must be either an animal or a plant."

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.reproduction_progress = 0
        self.status = []
        self.age = age
        self.life_expectancy = life_expectancy
        self.habitat = habitat
        self.offspring_number = 0

    def incr_age(self, speed):
        """Increment age by 1. May be sped up by a factor."""
        self.age += 1 * speed

    def reproduce(self):
        """Creates a copy of current living being, but with default values and age set to 0."""
        self.offspring_number *= 1
        self.reproduction_progress -= 1
        offspring = self
        offspring.name = self.name + " (" + self.offspring_number + " "
        offspring.offspring_number = 0
        offspring.status = []
        offspring.age = 0
        return offspring
