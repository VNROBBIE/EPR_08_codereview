from Plant import Plant

class Moss(Plant):
    """Mosses do not occupy space in the habitat and can only grow, not reproduce."""

    def __init__(self, name, age, size, min_size, size_growth_speed):
        """Initializes an instance of moss."""
        super().__init__(
            name=name,
            reproduction_rate=0,
            age=age,
            size=size,
            min_size=min_size,
            max_size=float("inf"),
            size_growth_speed=size_growth_speed)
