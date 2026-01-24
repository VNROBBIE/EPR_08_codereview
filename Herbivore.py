__author__ = "8572770, Kesidis, 8724694, Tran"
import doctest
from Animal import Animal


class Herbivore(Animal):
    """A herbivore, that eats plants to survive."""

    def __init__(self, name):
        """
        Initialize a Herbivore.
        They eat plants until their food-requirement is met.
        """
        super().__init__(name)

    def gather_food(self, plant):
        """
        Eats 20% of a plant and adds it to its food stock.

        >>> from Tree import Tree
        >>> g = Herbivore("giraffe")
        >>> t = Tree("tree")
        >>> g.gather_food(t)
        >>> g.food
        34.0
        >>> t.size
        16.0
        >>> g.gather_food(t)
        >>> t.size
        12.8
        >>> t.status
        {'withered'}
        """
        food_eaten = plant.size * 0.2
        self.food += food_eaten
        #  Reduce plant size.
        plant.size -= food_eaten
        if plant.size < plant.min_size:
            plant.status.add("withered")


if __name__ == "__main__":
    doctest.testmod()
