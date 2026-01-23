__author__ = "8572770, Kesidis, 8724694, Tran"
import random
import doctest
from Plant import Plant
from Carnivore import Carnivore
from Herbivore import Herbivore
from Flower import Flower
from Tree import Tree
from Moss import Moss


class Habitat:
    """A habitat containing an ecosystem of plants and animals."""

    def __init__(self, size):
        """Initialize new habitat."""
        if size < 0:
            raise TypeError("Habitat size must be a positive number.")
        try:
            self.size = int(size)
        except ValueError:
            print("Habitat size must be a positive number.")
        self.living_beings = []
        self.occupied_space = 0
        self.time_passed = 0
        self.season = 0

    def set_season(self, season):
        """
        Sets the habitat to a specified season.

        >>> h = Habitat(100)
        >>> h.set_season("spring")
        >>> h.season == 0
        True
        >>> h.set_season("autumn")
        >>> h.season == 2
        True

        Raises Valueerror if an invalid season name is entered.

        >>> h.set_season("hello")
        Traceback (most recent call last):
        ...
        ValueError: Please enter one of the four seasons.
        """
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
                raise ValueError("""Please enter one of the four seasons.""")
        self.season = season % 4

    def calc_occupied_space(self):
        """
        Calculates the current space occupied by plants.

        >>> h = Habitat(500)
        >>> t = Tree("tree")
        >>> h.add_living_being(t)
        >>> h.calc_occupied_space()
        >>> h.occupied_space
        20
        >>> f = Flower("flower")
        >>> h.add_living_being(f)
        >>> h.calc_occupied_space()
        >>> h.occupied_space
        25

        Mosses do not add to the occupied space.

        >>> m = Moss("moss")
        >>> h.add_living_being(m)
        >>> h.calc_occupied_space()
        >>> h.occupied_space
        25
        """
        self.occupied_space = 0
        for creature in self.living_beings:
            if isinstance(creature, Plant) and not isinstance(creature, Moss):
                self.occupied_space += creature.size

    def add_living_being(self, creature):
        """
        Adds a new living being to the habitat.

        >>> h = Habitat(500)
        >>> t = Tree("tree")
        >>> h.add_living_being(t)
        >>> t in h.living_beings
        True
        >>> f = Flower("flower")
        >>> h.add_living_being(f)
        >>> f in h.living_beings
        True
        >>> m = Moss("moss")
        >>> h.add_living_being(m)
        >>> m in h.living_beings
        True
        """
        self.living_beings.append(creature)
        self.calc_occupied_space()

    def update_eco(self):
        """
        Updates the ecosystem after every round.

        Doctests not possible due to complexity
        of an ecosystem and context-dependency.
        """
        if self.time_passed != 0:
            self.season += 1
        self.update_deaths()
        #  Generate random number for random events.
        rng_sickness = random.randint(1, 100)
        #   Update every living being.
        for creature in self.living_beings[:]:
            creature.incr_age()
            #  Small chance to get sick.
            if rng_sickness <= 1:
                creature.status.add("sick")
            # Check if living being reproduces.
            self.update_reproduction(creature)
            if isinstance(creature, Plant):
                self.update_plant(creature)
            if isinstance(creature, Carnivore) and self.season != 3:
                self.update_hunt(creature)
            if isinstance(creature, Herbivore):
                self.update_herbivores(creature)
                #  Consume food.
                creature.eat()
        self.time_passed += 1

    def update_deaths(self):
        """
        Removes all deceased beings from the habitat.

        >>> h = Habitat(500)
        >>> t = Tree("tree")
        >>> h.add_living_being(t)
        >>> t.status.add("withered")
        >>> h.update_deaths()
        tree has died.
        >>> t in h.living_beings
        False
        >>> b = Carnivore("bear")
        >>> h.add_living_being(b)
        >>> b.status.add("starved")
        >>> h.update_deaths()
        bear has starved.
        >>> b in h.living_beings
        False
        """
        deceased_living_beings = []
        #   Check for death triggers for every creature.
        for creature in self.living_beings:
            if self.living_being_death_chance(creature):
                deceased_living_beings.append(creature)
        #  Create new living beings list without deceased animals.
        self.living_beings = [creature for creature in self.living_beings
                              if creature not in deceased_living_beings]

    def update_reproduction(self, creature):
        """
        Update the reproduction progress for all living beings.

        >>> h = Habitat(500)
        >>> b = Carnivore("bear")
        >>> b.reproduction_rate = 0.6
        >>> h.add_living_being(b)
        >>> h.update_reproduction(b)
        >>> b.reproduction_progress
        0.6
        >>> t = Tree("tree")
        >>> h.add_living_being(t)
        >>> len(h.living_beings)
        2
        >>> h.update_reproduction(t)
        >>> len(h.living_beings)
        3
        """
        #  Increase reproduction progress.
        creature.reproduction_progress += creature.reproduction_rate
        while True:
            offspring = creature.reproduce(self.season)
            if offspring is None:
                break
            #  Add newborn creature to habitat.
            self.living_beings.append(offspring)

    def update_plant(self, plant):
        """
        Grow every plant.

        >>> h = Habitat(500)
        >>> t = Tree("tree")
        >>> h.add_living_being(t)
        >>> h.update_plant(t)
        >>> t.size
        22

        If no space is left, plants cannot grow further.

        >>> f = Flower("flower")
        >>> h.add_living_being(f)
        >>> f.size = 5
        >>> h.occupied_space = 500
        >>> h.update_plant(f)
        >>> f.size
        5

        Mosses do not take any space and can grow infinitely.

        >>> m = Moss("moss")
        >>> h.add_living_being(m)
        >>> m.size
        20
        >>> h.occupied_space = 500
        >>> h.update_plant(m)
        >>> m.size
        23
        """
        new_plant_size = plant.grow()
        #  Check if new size exceeds max size or available Habitat space.
        if (new_plant_size <= plant.max_size and
            new_plant_size - plant.size + self.occupied_space <= self.size)\
                or isinstance(plant, Moss):
            plant.size = new_plant_size
            self.calc_occupied_space()

    def update_hunt(self, predator):
        """
        Start a hunt for every carnivore.

        >>> h = Habitat(500)
        >>> b = Carnivore("bear")
        >>> h.add_living_being(b)
        >>> d = Herbivore("deer")
        >>> h.add_living_being(d)
        >>> random.seed(2)
        >>> h.update_hunt(b)
        deer has been fed to bear.
        >>> b.food
        45.08487199515892
        >>> random.seed(5)
        >>> h.update_hunt(b)
        bear has injured itself while on a hunt.
        """
        #   Create list of potential preys (herbivores).
        if any(isinstance(prey, Herbivore) for prey in self.living_beings):
            prey_list = [prey for prey in self.living_beings if
                         isinstance(prey, Herbivore) and prey is not predator]
        else:
            #  Will resort to hunting other carnivores if no herbivores exist.
            prey_list = list(self.living_beings)
        if len(prey_list) > 0:
            predator.gather_food(random.choice(prey_list))

    def update_herbivores(self, herbivore):
        """
        Make all Herbivores eat random plants until they are fully fed.

        >>> h = Habitat(500)
        >>> t = Tree("tree")
        >>> h.add_living_being(t)
        >>> d = Herbivore("deer")
        >>> h.add_living_being(d)
        >>> d.food = 5
        >>> h.update_herbivores(d)
        >>> d.food
        16.808
        >>> t.size
        8.192
        >>> t.status
        {'withered'}

        Tree can't be eaten if it has withered.

        >>> d.food = 8
        >>> h.update_herbivores(d)
        >>> d.food
        8
        """
        while herbivore.food < herbivore.food_requirement:
            plants_list = [plant for plant in self.living_beings
                           if isinstance(plant, Plant) and
                           "withered" not in plant.status]
            if len(plants_list) == 0:
                break
            #  Eat a random plant.
            herbivore.gather_food(random.choice(plants_list))

    def living_being_death_chance(self, creature):
        """
        Calculate whether a creature dies or not based on its status.

        >>> h = Habitat(500)
        >>> b = Carnivore("bear")
        >>> h.add_living_being(b)
        >>> b.status.add("starved")
        >>> h.living_being_death_chance(b)
        bear has starved.
        True
        >>> random.seed(1)
        >>> b.status = {"sick"}
        >>> h.living_being_death_chance(b)
        Sickness has consumed bear.
        True
        >>> random.seed(19)
        >>> h.living_being_death_chance(b)
        bear has recovered from its sickness.
        False
        >>> b.status
        set()
        """
        rng_death = random.randint(1, 100)
        #  Starved, wounded and withered are guaranteed death.
        if len(creature.status) != 0:
            if "starved" in creature.status:
                print(creature.name + " has starved.")
                return True
            if "devoured" in creature.status:
                return True
            if "wounded" in creature.status:
                print(creature.name + " has succumbed to its injuries.")
                return True
            if "withered" in creature.status:
                print(creature.name + " has died.")
                return True
            if "old" in creature.status:
                #   Death chance is 10% for every unit above life expectancy.
                death_chance = creature.age - creature.life_expectancy * 10
                if rng_death <= death_chance:
                    print(creature.name + " has passed away of old age.")
                    return True
            if "sick" in creature.status:
                #   High chance to die to sickness.
                if rng_death <= 30:
                    print("Sickness has consumed " + creature.name + ".")
                    return True
                #  Small chance to recover from sickness when it is not winter.
                if rng_death >= 85 and self.season != 3:
                    creature.status.remove("sick")
                    print(creature.name + " has recovered from its sickness.")
            if "injured" in creature.status:
                #   High chance to die to injury that decreases over time.
                death_chance = 50 - 20 * creature.injury_time
                if death_chance < 0:
                    #  Injury heals after three time units.
                    creature.status.remove("injured")
                    print(creature.name + " has recovered from its injuries.")
                if rng_death <= death_chance:
                    print(creature.name + " has succumbed to its injuries.")
                    return True
                #  Count duration of an injury.
                creature.injury_time += 1
        return False


if __name__ == "__main__":
    doctest.testmod()
