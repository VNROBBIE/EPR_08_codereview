from LivingBeing import LivingBeing

class Plant(LivingBeing):
    """A plant occupying space in the habitat based on its size. Withers when size is below min size."""

    def __init__(self, name, reproduction_rate, age, life_expectancy, size, min_size, max_size, size_growth_speed):
        super().__init__(name, reproduction_rate, age, life_expectancy)
        self.size = size
        self.min_size = min_size
        self.max_size = max_size
        self.size_growth_speed = size_growth_speed

    def grow(self):
        """Plant grows based on its set growth speed."""
        self.new_size = self.size + self.size_growth_speed
        return self.new_size

    def reproduce(self, season):
        """Creates a copy of current plant, if reproduction progress reaches 1."""
        #  Reproduction halts in winter.
        if season != 3:
            #  Offspring has default values and age is set to 0. Size is set to minimum.
            if self.reproduction_progress >= 1:
                self.offspring_number += 1
                #  Reset reproduction progress.
                self.reproduction_progress -= 1
                offspring = self
                #  Bears same name as its parent, but enumerated.
                offspring.name = str(self.name + " (" + self.offspring_number + ")")
                offspring.offspring_number = 0
                offspring.status = set()
                offspring.age = 0
                offspring.size = self.min_size
                return offspring
            else:
                #  Increase reproduction progress.
                self.reproduction_progress += self.reproduction_rate
                return None
