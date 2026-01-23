from Plant import Plant

class Flower(Plant):
    """Flowers have a high reproduction rate compared to other plants."""

    def __init__(self, name, age, size, min_size, max_size, size_growth_speed):
        """Initializes a flower."""
        super().__init__(name=name,
                         reproduction_rate=4,
                         age=age,
                         size=size,
                         min_size=min_size,
                         max_size=max_size,
                         size_growth_speed=size_growth_speed)

if __name__ == "__main__":
    f = Flower("flower", 4, 2, 0, 5, 1)
    print(f.name)