__author__ = "8572770, Kesidis, 8724694, Tran"
import doctest
from Animal import Animal
from Herbivore import Herbivore
from Carnivore import Carnivore


class Omnivore(Herbivore, Carnivore):
    """An omnivore, that will hunt, but will mainly eat plants."""

    def __init__(self, name):
        """
        Initialize a Herbivore.
        They eat plants until their food-requirement is met.
        """
        super().__init__(name)

    def gather_food(self, food):
        """
        Will hunt or eat plant depending on the current target.

        >>> import random
        >>> from Flower import Flower
        >>> f = Omnivore("fox")
        >>> f.food = 10
        >>> b = Herbivore("bunny")
        >>> random.seed(1)
        >>> f.gather_food(b)
        bunny has been fed to fox.
        >>> f.food
        25.569203874822215
        >>> p = Flower("poppy")
        >>> f.gather_food(p)
        >>> f.food
        26.569203874822215
        """
        if isinstance(food, Animal):
            Carnivore.gather_food(self, food)
        else:
            Herbivore.gather_food(self, food)

if __name__ == "__main__":
    doctest.testmod()
