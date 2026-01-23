import copy
import doctest
from LivingBeing import LivingBeing

class Plant(LivingBeing):
    """A plant occupying space in the habitat based on its size. Withers when size is below min size."""

    def __init__(self, name, reproduction_rate, age, size, min_size, max_size, size_growth_speed):
        """Initialize a plant."""
        super().__init__(name, reproduction_rate, age)
        self.size = size
        self.min_size = min_size
        self.max_size = max_size
        self.size_growth_speed = size_growth_speed

    def grow(self):
        """Plant grows based on its set growth speed."""
        self.new_size = self.size + self.size_growth_speed
        return self.new_size

    def reproduce(self, season):
        """
        Creates a copy of current plant, if reproduction progress reaches 1.

        >>> b = Plant("bush", 1, 20, 20, 5, 30, 2)
        >>> b.reproduction_progress = 1

        Plants do not reproduce in winter.

        >>> offspring = b.reproduce(3)
        >>> offspring is None
        True
        >>> offspring = b.reproduce(0)
        >>> offspring is not None
        True
        """
        #  Reproduction halts in winter.
        if season != 3:
            #  Offspring has default values and age is set to 0. Size is set to minimum.
            if self.reproduction_progress >= 1:
                self.offspring_number += 1
                #  Reset reproduction progress.
                self.reproduction_progress -= 1
                offspring = copy.deepcopy(self)
                #  Bears same name as its parent, but enumerated.
                offspring.name = str(self.name + " (" + str(self.offspring_number) + ")")
                offspring.offspring_number = 0
                offspring.status = set()
                offspring.age = 0
                offspring.size = self.min_size
                return offspring


if __name__ == "__main__":
    doctest.testmod()
