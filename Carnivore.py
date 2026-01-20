from Animal import Animal

class Carnivore(Animal):
    """An animal, that requires food to survive."""

    def __init__(self, name, reproduction_rate, age, life_expectancy, habitat, food_requirement):
        super().__init__(name, reproduction_rate, age, life_expectancy, habitat, food_requirement)
        self.food_requirement = food_requirement
        self.food = food_requirement * 2
        self.injury_time = 0

    def gather_food(self, prey, RNG):
        if RNG <= 50:
            self.food += 1.5 * self.food_requirement
            print(prey + " has been fed to " + self.name + ".")
            if "sick" in prey.status and RNG <= 25:
                self.status.add("sick")
                print("Its infection has spreaded to " + self.name)
        elif RNG >= 90:
            if "wounded" in self.status:
                print(self.name + " has been critically injured on a hunt.")

            else:
                self.status.add("injured")
                print(self.name + " has injured itself on a hunt.")

