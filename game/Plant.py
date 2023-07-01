from Organism import Organism
from random import randint


class Plant(Organism):
    def __init__(self, world, yy, xx, stre):
        super().__init__(world, yy, xx, stre)

    def action(self, world, direction):
        c = randint(0, 9)
        if c == 0:
            return self.breed(world)
        return 0

    def collision(self, world, o, cn):
        if self.strength > o.S():
            o.die()
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
