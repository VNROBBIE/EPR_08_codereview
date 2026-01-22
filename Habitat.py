import random
from Plant import Plant
from Animal import Animal
from Carnivore import Carnivore
from Herbivore import Herbivore
from Moss import Moss

class Habitat:
    """A habitat containing an ecosystem of plants and animals."""

    def __init__(self, size):
        """Initialize new habitat."""
        if isinstance(size, int) or size < 0:
            raise TypeError("Habitat size must be a positive whole number.")
        self.size = size
        self.living_beings = []
        self.occupied_space = 0
        self.time_passed = 0
        self.season = 0


    def set_season(self, season):
        match season:
            case "spring":
                season = 0
            case "summer":
                season = 1
            case "fall" | "autumn":
                season = 2
            case "winter":
                season = 3
            case _:
                raise ValueError("Invalid: Please enter one of the four seasons.")
        self.season = (season % 4) - 1


    def calc_occupied_space(self):
        """Calculates the current space occupied by plants."""
        self.occupied_space = 0
        for creature in self.living_beings:
            if isinstance(creature, Plant) and not isinstance(creature, Moss):
                self.occupied_space += creature.size


    def add_living_being(self, creature):
        """Adds a new living being to the habitat."""
        self.living_beings.append(creature)
        self.calc_occupied_space()


    def update_eco(self):
        """Updates the ecosystem after every round."""
        #  Generate random number for random events.
        RNG_sickness = random.randint(1, 100)
        self.update_deaths()
        #   Update every living being.
        for creature in self.living_beings:
            creature.incr_age()
            self.update_herbivores()
            #  Small chance to get sick.
            if RNG_sickness <= 10:
                creature.status.add("sick")
            # Check if living being reproduces.
            self.update_reproduction()
            if isinstance(creature, Plant):
                self.update_plant()
            if self.season != 3 and isinstance(creature, Animal):
                self.update_hunt(creature)
                self.update_herbivores(creature)
                #  Consume food.
                creature.eat()


    def update_deaths(self):
        """Removes all deaceased beings from the habitat."""
        deceased_living_beings = []
        #   Check for death triggers for every creature.
        for creature in self.living_beings:
            if self.living_being_death_chance(self, creature):
                deceased_living_beings.append(creature)
        #  Create new living beings list without deceased animals.
        self.living_beings = [creature for creature in self.living_beings if creature not in deceased_living_beings]


    def update_reproduction(self, creature):
        """Update the reproduction progress for all living beings."""
        while True:
            offspring = creature.reproduce()
            if offspring is None:
                break
            #  Add newborn creature to habitat.
            self.living_beings.append(creature.reproduce())


    def update_plant(self, plant):
        """Grow every plant."""
        new_plant_size = plant.grow()
        #  Check if new size exceeds max size or available Habitat space.
        if (new_plant_size <= plant.max_size and new_plant_size + self.occupied_space <= self.size)\
                or isinstance(plant, Moss):
            plant.size = new_plant_size
            self.calc_occupied_space()


    def update_hunt(self, predator):
        """Start a hunt for every carnivore."""
        if isinstance(predator, Carnivore):
            #   Create list of potential preys (herbivores).
            if any(isinstance(prey, Herbivore) for prey in self.living_beings):
                prey_list = [prey for prey in self.living_beings if isinstance(prey, Herbivore) and prey is not predator]
            else:
                #  Will resort to hunting other carnivores if no herbivores available.
                prey_list = [prey for prey in self.living_beings]
            if len(prey_list) > 0:
                predator.gather_food(random.choice(self.prey_list))


    def update_herbivores(self, herbivore):
        """Make all Herbivores eat a random plant until they are fully fed."""
        plants_list = [plant for plant in self.living_beings if isinstance(plant, Plant)]
        while len(plants_list) > 0 and herbivore.food < herbivore.food_requirement:
            #  Eat a random plant.
            herbivore.gather_food(random.choice(plants_list))
            herbivore.


    def living_being_death_chance(self, creature):
        """Calculate whether a creature dies or not based on its status."""
        RNG_death = random.randint(1, 100)
        #  Starved, wounded and withered are guaranteed death.
        if len(creature.status) != 0:
            if "starved" in creature:
                print(self.name + " starved.")
                return True
            if "wounded" in creature:
                print(creature.name + " has succumbed to its injuries.")
                return True
            if "withered" in creature:
                print(creature.name + " has died.")
                return True
            if "old" in creature.status:
                #   Death chance is 10% for every unit above life expectancy.
                death_chance = creature.age - creature.life_expectancy * 10
                if RNG_death <= death_chance:
                    print(creature.name + " has passed away of old age.")
                    return True
            if "sick" in creature.status:
                #   High chance to die to sickness.
                if RNG_death <= 30:
                    print("Sickness has consumed " + creature.name + ".")
                    return True
                elif RNG_death >= 85 and self.season != 3:
                    #  Small chance to recover from sickness.
                    creature.status.remove("sick")
                    print(creature.name + " has recovered from its sickness.")
            if "injured" in creature.status:
                #   High chance to die to injury that decreases over time.
                death_chance = 50 - 20 * creature.injury_time
                if death_chance < 0:
                    #  Injury heals after three time units.
                    creature.status.remove("injured")
                    print(creature.name + " has recovered from its injuries.")
                if RNG_death <= death_chance:
                    print(creature.name + " has succumbed to its injuries.")
                    return True
                else:
                    #  Count duration of an injury.
                    creature.injury_time += 1
        return False


