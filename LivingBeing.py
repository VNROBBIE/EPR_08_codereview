from abc import ABC, abstractmethod

class LivingBeing(ABC):
    """A living being, that must be either an animal or a plant."""

    def __init__(self, name, reproduction_rate, age):
        """Initialize new living being."""
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.reproduction_progress = 0
        self.status = set()
        self.age = age
        self.life_expectancy = 40
        self.offspring_number = 0

    def incr_age(self):
        """Increment age by 1."""
        self.age += 1

    @abstractmethod
    def reproduce(self, season):
        """Creates a copy of current living being, if reproduction progress reaches 1."""
        pass
