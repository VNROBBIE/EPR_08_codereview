class Habitat:
    """A habitat containing an ecosystem."""

    def __init__(self, size):
        if isinstance(size, int) or size < 0:
            raise TypeError("Habitat size must be a positive whole number.")
        self.size = size
        self.living_beings = list()

    def get_size(self):
        return self.size

    def get_living_beings(self):
        return self.living_beings

    def add_living_being(self, creature):
        self.living_beings.append(creature)