from Plant import Plant
from OrganismType import OrganismType
import OrganismStrength as s

class Hogweed(Plant):
    def __init__(self, world, yy, xx, stre=s.hogweed):
        super().__init__(world, yy, xx, stre)
        self.initiative = 0
        self.type = OrganismType.HOGWEED.value
        world.mapChange(self.y, self.x, self.type)
        self.yyy = [self.y-1, self.y+1, self.y, self.y]
        self.xxx = [self.x, self.x, self.x+1, self.x-1]

    def birth(self, world, yy, xx):
        return Hogweed(world, yy, xx)

    def doCollide(self, o):
        if self != o and o.alive() and self.alive():
            yo = o.Y()
            xo = o.X()
            if yo == self.y and xo == self.x:
                return True
            elif yo == self.yyy[0] and xo == self.xxx[0]:
                return True
            elif yo == self.yyy[1] and xo == self.xxx[1]:
                return True
            elif yo == self.yyy[2] and xo == self.xxx[2]:
                return True
            elif yo == self.yyy[3] and xo == self.xxx[3]:
                return True
            else:
                return False
        else:
            return False

    def collision(self, world, o, cn):
        if o.T() < 7:
            o.die()
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
