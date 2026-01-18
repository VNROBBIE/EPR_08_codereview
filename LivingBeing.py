from abc import ABC, abstractmethod

class LivingBeing(ABC):
    "A living being, that must be either an animal or a plant."

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.age = age
        self.life_expectancy = life_expectancy
        self.habitat = habitat

    def incr_age(self, speed):
        self.age += 1 * speed

    def get_habitat_size(self):
        return self.habitat.size