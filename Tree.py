import copy
from Plant import Plant

class Tree(Plant):
    """Trees have a very high life expectancy compared to other plants."""

    def __init__(self, name, reproduction_rate, age ,size, min_size, max_size, size_growth_speed):
        """Initilizes a tree."""
        super().__init__(name, reproduction_rate, age, size, min_size, max_size, size_growth_speed)
        self.life_expectancy = 100


    def reproduce(self, season):
        """Creates a copy of current tree. Trees can also reproduce during winter."""
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
    t = Tree("tree", 1, 5, 10, 5, 50, 1)
    print(t.status)