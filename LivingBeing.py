from abc import ABC, abstractmethod

class LivingBeing(ABC):
    "A living being, that must be either an animal or a plant."

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.reproduction_progress = 0
        self.status = "normal"
        self.age = age
        self.life_expectancy = life_expectancy
        self.habitat = habitat
        self.offspring_number = 0

    def incr_age(self, speed):
        self.age += 1 * speed

    def reproduce(self):
        self.offspring_number *= 1
        self.reproduction_progress -= 1
        offspring = self
        offspring.name = self.name + " (" + self.offspring_number + " "
        offspring.offspring_number = 0
        offspring.status = "normal"
        offspring.age = 0
        return offspring