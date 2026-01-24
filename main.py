__author__ = "8572770, Kesidis, 8724694, Tran"

from Habitat import Habitat
from Flower import Flower
from Tree import Tree
from Moss import Moss
from Herbivore import Herbivore
from Carnivore import Carnivore
from Omnivore import Omnivore
from Plant import Plant
from Animal import Animal


def read_int(prompt, min_value=0):
    """Read an integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def create_start_population(habitat):
    """Initial setup"""
    print("\n--- Initial population setup ---")

    flowers = read_int("Number of flowers: ", 0)
    trees = read_int("Number of trees: ", 0)
    moss = read_int("Number of mosses: ", 0)

    herbivores = read_int("Number of herbivores: ", 0)
    carnivores = read_int("Number of carnivores: ", 0)
    omnivores = read_int("Number of omnivores: ", 0)

    # Names for flowers
    for i in range(flowers):
        habitat.add_living_being(Flower(f"Flower{i}"))

    # Names for trees
    for i in range(trees):
        habitat.add_living_being(Tree(f"Tree{i}"))

    # Names for moss
    for i in range(moss):
        habitat.add_living_being(Moss(f"Moss{i}"))

    # Names for herbivores
    for i in range(herbivores):
        habitat.add_living_being(Herbivore(f"Herbivore{i}"))

    # Names for carnivores
    for i in range(carnivores):
        habitat.add_living_being(Carnivore(f"Carnivore{i}"))

    # Names for omnivores
    for i in range(omnivores):
        habitat.add_living_being(Omnivore(f"Omnivore{i}"))


def print_status(habitat):
    """Print an overview of the ecosystem state."""
    flowers = 0
    trees = 0
    mosses = 0
    herbivores = 0
    carnivores = 0
    omnivores = 0

    for creature in habitat.living_beings:
        if isinstance(creature, Flower):
            flowers += 1

        if isinstance(creature, Tree):
            trees += 1

        if isinstance(creature, Moss):
            mosses += 1

        if isinstance(creature, Herbivore):
            herbivores += 1

        if isinstance(creature, Carnivore):
            carnivores += 1

        if isinstance(creature, Omnivore):
            omnivores += 1

    print("\n--- Ecosystem status ---")
    print(f"Time passed: {habitat.time_passed}")
    print(f"Season: {habitat.season}")
    print(f"Flowers: {flowers}")
    print(f"Trees: {trees}")
    print(f"Mosses: {mosses}")
    print(f"Herbivores: {herbivores}")
    print(f"Carnivores: {carnivores}")
    print("------------------------")


def main_menu(habitat):
    """Main menu"""
    while True:
        print("\n[1] Simulate one round")
        print("[2] Simulate multiple rounds")
        print("[3] Show ecosystem status")
        print("[0] Exit")

        choice = input("Choice: ")

        if choice == "1":
            print()
            print("--- Simulation result ---")
            habitat.update_eco()
            print("\nOne round simulated.")

        elif choice == "2":
            rounds = read_int("How many rounds? ", 1)
            print()
            for _ in range(rounds):
                habitat.update_eco()
            print(f"\n{rounds} rounds simulated.")

        elif choice == "3":
            print_status(habitat)

        elif choice == "0":
            print("Simulation ended.")
            break

        else:
            print("Invalid input.")


def main():
    print("=== Ecosystem Simulation ===")
    size = read_int("Habitat size: ", 1)

    habitat = Habitat(size)
    create_start_population(habitat)
    main_menu(habitat)


if __name__ == "__main__":
    main()
