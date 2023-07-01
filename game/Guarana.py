from Plant import Plant
from OrganismType import OrganismType

class Guarana(Plant):
    def __init__(self, world, yy, xx, stre=0):
        super().__init__(world, yy, xx, stre)
        self.initiative = 0
        self.type = OrganismType.GUARANA.value
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Guarana(world, yy, xx)

    def collision(self, world, o, cn):
        if self.strength > o.S():
            o.die()
        if not self.state:
            o.upgradeS()
            o.upgradeS()
            o.upgradeS()
        else:
            world.mapChange(self.y, self.x, self.type)
        return 0
