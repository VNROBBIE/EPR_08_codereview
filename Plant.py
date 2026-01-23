__author__ = "8572770, Kesidis, 8724694, Tran"
import copy
import doctest
from abc import ABC
from LivingBeing import LivingBeing


class Plant(LivingBeing, ABC):
    """
    A plant occupying space in the habitat based on its size.
    Withers when size is below min size.
    """

    def __init__(self, name):
        """Initialize a plant."""
        super().__init__(name)

    def grow(self):
        """Plant grows based on its set growth speed."""
        self.new_size = self.size + self.size_growth_speed
        return self.new_size

    def reproduce(self, season):
        """
        Creates a copy of current plant, if reproduction progress reaches 1.
        >>> class TestPlant(Plant):
        ...    def __init__(self, name):
        ...        super().__init__(name)
        ...        self.min_size = 5
        >>> b = TestPlant("bush")
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
            """
            Offspring has default values and age is set to 0.
            Size is set to minimum.
            """
            if self.reproduction_progress >= 1:
                self.offspring_number += 1
                #  Reset reproduction progress.
                self.reproduction_progress -= 1
                offspring = copy.deepcopy(self)
                #  Bears same name as its parent, but enumerated.
                offspring.name = str(self.name +
                                     " (" + str(self.offspring_number) + ")")
                offspring.offspring_number = 0
                offspring.status = set()
                offspring.age = 0
                offspring.size = self.min_size
                return offspring
        return None


if __name__ == "__main__":
    doctest.testmod()
