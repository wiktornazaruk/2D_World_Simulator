from organisms.Plant import Plant
from OrganismType import OrganismType
import OrganismStrength as s

class Belladonna(Plant):
    def __init__(self, world, yy, xx, stre=s.belladonna):
        super().__init__(world, yy, xx, stre)
        self.initiative = 0
        self.type = OrganismType.BELLADONNA.value
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Belladonna(world, yy, xx)

    def collision(self, world, o, cn):
        if self.strength > o.S():
            o.die()
        if not self.state:
            o.die()
            world.mapChange(self.y, self.x, OrganismType.EMPTY.value)
        else:
            world.mapChange(self.y, self.x, self.type)
        return 0
