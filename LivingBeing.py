from abc import ABC, abstractmethod

class LivingBeing(ABC):
    "A living being, that must be either an animal or a plant."

    def __init__(self, name, reproduction_rate, age, life_expectancy):
        """Initialize new living being."""
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.reproduction_progress = 0
        self.status = {}
        self.age = age
        self.life_expectancy = life_expectancy
        self.offspring_number = 0

    def incr_age(self, speed):
        """Increment age by 1. May be sped up by a factor."""
        self.age += 1 * speed

    def reproduce(self):
        """Creates a copy of current living being, if reproduction progess reaches 1."""
        #  Offspring has default values and age is set to 0.
        if self.reproduction_progress >= 1:
            self.offspring_number *= 1
            #  Reset reproduction progress.
            self.reproduction_progress -= 1
            offspring = self
            #  Bears same name as its parent, but enumerated.
            offspring.name = str(self.name + " (" + self.offspring_number + ")")
            offspring.offspring_number = 0
            offspring.status = []
            offspring.age = 0
            return offspring
        else:
            #  Increase reproduction progress.
            self.reproduction_progress += self.reproduction_rate
            return None
