from Animal import Animal

class Herbivore(Animal):
    """An animal, that requires food to survive."""

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat, food_requirement):
        super().__init__(name, reproduction_rate, age, life_expectancy, habitat, food_requirement)
        self.food_requirement = food_requirement
        self.food = food_requirement * 2
        self.injury_time = 0

    def gather_food(self, plant):
        food_eaten = plant.size * 0.2
        plant.size -= food_eaten
        if plant.size < plant.min_size:
            plant.status.add("withered")

