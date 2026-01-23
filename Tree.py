__author__ = "8572770, Kesidis, 8724694, Tran"
import copy
import doctest
from Plant import Plant


class Tree(Plant):
    """Trees have a very high life expectancy compared to other plants."""

    def __init__(self, name):
        """Initilizes a tree."""
        super().__init__(name)
        self.size = 20
        self.min_size = 15
        self.max_size = 50
        self.size_growth_speed = 2

    def reproduce(self, season):
        """
        Creates a copy of current tree. Trees can also reproduce during winter.

        >>> t = Tree("tree")
        >>> t.reproduction_progress = 2

        Plants do not reproduce in winter.

        >>> offspring = t.reproduce(3)
        >>> offspring is not None
        True
        >>> offspring = t.reproduce(0)
        >>> offspring is not None
        True
        """
        #  Offspring has default values and age is set to 0.
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
            #  Offspring has minimum possible size.
            offspring.size = self.min_size
            return offspring
        return None


if __name__ == "__main__":
    doctest.testmod()