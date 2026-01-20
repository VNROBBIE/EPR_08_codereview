import random
from Plant import Plant
from Animal import Animal
from Carnivore import Carnivore
from Herbivore import Herbivore

class Habitat:
    """A habitat containing an ecosystem."""

    def __init__(self, size):
        if isinstance(size, int) or size < 0:
            raise TypeError("Habitat size must be a positive whole number.")
        self.size = size
        self.living_beings = []
        self.occupied_space = self.calc_occupied_space()

    def calc_occupied_space(self):
        """Calculates the current space occupied by plants."""
        for creature in self.living_beings:
            if isinstance(creature, Plant):
                self.occupied_space += creature.size

    def add_living_being(self, creature):
        """Adds a new living being to the habitat."""
        self.living_beings.append(creature)
        self.calc_occupied_space()

    def update_eco(self):
        """Updates the ecosystem after every round."""
        deceased_living_beings = []
        RNG = random.randint(1, 100)
        #   Update every living being.
        for creature in self.living_beings:
            #   Check for death triggers for every creature.
            if self.living_being_death_chance(self, creature, RNG) or "starved" in creature.status:
                deceased_living_beings.append(creature)
                continue
            else:
                # Check if living being reproduces.
                while True:
                    offspring = creature.reproduce()
                    if offspring is None:
                        break
                    self.living_beings.append(creature.reproduce())
                if isinstance(creature, Plant):
                    new_plant_size = creature.grow()
                    if new_plant_size <= creature.max_size and new_plant_size + self.occupied_space <= self.size:
                        creature.size = new_plant_size
                        self.calc_occupied_space()
                if isinstance(creature, Animal):
                    if isinstance(creature, Carnivore):
                        prey_list = [prey for prey in self.living_beings if isinstance(prey, Herbivore)]
                        if len(prey_list) > 0:
                            creature.gather_food(random.choice(self.living_beings), RNG)
                    creature.eat()
        self.living_beings = [creature for creature in self.living_beings if creature not in deceased_living_beings]


    def living_being_death_chance(self, creature, RNG):
        """Calculate whether a creature dies or not based on its status."""
        if len(creature.status) != 0:
            if "starved" in creature:
                print(self.name + " starved.")
                return True
            if "wounded" in creature:
                print(creature.name + " succumbed to its injuries.")
                return True
            if "withered" in creature:
                print(creature.name + " has died.")
                return True
            if "old" in creature.status:
                #   Death chance is 10% for every unit above life expectancy.
                death_chance = creature.age - creature.life_expectancy * 10
                if RNG <= death_chance:
                    print(creature.name + " passed away of old age.")
                    return True
            if "sick" in creature.status:
                #   High chance to die to sickness.
                if RNG <= 30:
                    print("Sickness consumed " + creature.name + ".")
                    return True
                elif RNG >= 85:
                    #  Small chance to recover from sickness.
                    creature.status.remove("sick")
                    print(creature.name + " recovered from its sickness.")
            if "injured" in creature.status:
                #   High chance to die to injury that decreases over time.
                death_chance = 50 - 20 * creature.injury_time
                if death_chance < 0:
                    creature.status.remove("injured")
                    print(creature.name + " recovered from its injuries.")
                if RNG <= death_chance:
                    print(creature.name + " succumbed to its injuries.")
                    return True
                else:
                    creature.injury_time += 1
        return False


