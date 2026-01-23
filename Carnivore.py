import random

from Animal import Animal

class Carnivore(Animal):
    """A carnivore, that hunts to acquire food."""

    def __init__(self, name, reproduction_rate, age, food_requirement):
        """Initializes new Carnivore."""
        super().__init__(name, reproduction_rate, age, food_requirement)

    def gather_food(self, prey):
        """Hunts and potentially kills a herbivore."""
        RNG_food = random.randint(1, 100)
        injury_percentage = 10
        #  Hunt has a 50% chance for success.
        if RNG_food <= 50:
            self.food += (random.random()) + 0.75 * self.food_requirement
            print(prey + " has been fed to " + self.name + ".")
            #  50/50 chance to catch a prey's disease.
            if "sick" in prey.status and RNG_food <= 25:
                self.status.add("sick")
                print("Its infection has spreaded to " + self.name)
        #  Small chance for hunt to critically fail and injure the predator.
        #  Chance is increased if prey is carnivorous.
        elif (isinstance(prey, Carnivore) and RNG_food >= 100 - injury_percentage - 20)\
                or RNG_food >= 100 - injury_percentage:
            #  Predator dies if already injured.
            if "injured" in self.status:
                self.status.add("wounded")
                print(self.name + " has been critically injured on a hunt.")
            else:
                #  Predator gets injured in case of a critical failure.
                self.status.add("injured")
                print(self.name + " has injured itself on a hunt.")

