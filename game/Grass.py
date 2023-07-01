from Plant import Plant
from OrganismType import OrganismType

class Grass(Plant):
    def __init__(self, world, yy, xx, stre=0):
        super().__init__(world, yy, xx, stre)
        self.initiative = 0
        self.type = OrganismType.GRASS.value
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Grass(world, yy, xx)
