from Animal import Animal

class Herbivore(Animal):
    """A herbivore, that eats plants to survive."""

    def __init__(self, name, reproduction_rate, age, food_requirement):
        """Initialize an Herbivore. They eat plants until their food-requirement is met."""
        super().__init__(name, reproduction_rate, age, food_requirement)

    def gather_food(self, plant):
        food_eaten = plant.size * 0.2
        self.food += food_eaten
        plant.size -= food_eaten
        if plant.size < plant.min_size:
            plant.status.add("withered")

