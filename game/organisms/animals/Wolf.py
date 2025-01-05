from organisms.Animal import Animal
from OrganismType import OrganismType
import OrganismStrength as s

class Wolf (Animal):
    def __init__(self, world, yy, xx, stre=s.wolf):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.type = OrganismType.WOLF.value
        self.state = True
        self.strength = stre
        self.initiative = 5
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Wolf(world, yy, xx)
