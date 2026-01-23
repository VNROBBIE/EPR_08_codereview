__author__ = "8572770, Kesidis, 8724694, Tran"
import doctest
from Animal import Animal


class Herbivore(Animal):
    """A herbivore, that eats plants to survive."""

    def __init__(self, name, reproduction_rate, age, food_requirement):
        """
        Initialize an Herbivore.
        They eat plants until their food-requirement is met.
        """
        super().__init__(name, reproduction_rate, age, food_requirement)

    def gather_food(self, plant):
        """
        Eats 20% of a plant and adds it to its food stock.

        >>> from Tree import Tree
        >>> g = Herbivore("giraffe", 0.25, 20, 30)
        >>> t = Tree("tree", 0.5, 50, 14, 10, 100, 1)
        >>> g.gather_food(t)
        >>> g.food
        47.8
        >>> t.size
        11.2
        >>> g.gather_food(t)
        >>> t.size
        8.959999999999999
        >>> t.status
        {'withered'}
        """
        food_eaten = plant.size * 0.2
        self.food += food_eaten
        plant.size -= food_eaten
        if plant.size < plant.min_size:
            plant.status.add("withered")


if __name__ == "__main__":
    doctest.testmod()
