from Plant import Plant
from OrganismType import OrganismType

class SowThistle(Plant):
    def __init__(self, world, yy, xx, stre=0):
        super().__init__(world, yy, xx, stre)
        self.initiative = 0
        self.type = OrganismType.SOWTHISTLE.value
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return SowThistle(world, yy, xx)
