from organisms.Animal import Animal
from OrganismType import OrganismType
import OrganismStrength as s

class Sheep (Animal):
    def __init__(self, world, yy, xx, stre=s.sheep):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.type = OrganismType.SHEEP.value
        self.state = True
        self.strength = stre
        self.initiative = 4
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Sheep(world, yy, xx)
