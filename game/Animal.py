from var import var
from Organism import Organism
from random import randint
from OrganismType import OrganismType

class Animal(Organism):
    def __init__(self, world, yy, xx, stre):
        super().__init__(world, yy, xx, stre)
        self.py = self.y
        self.px = self.x

    def action(self, world, direction):
        self.py = self.y
        self.px = self.x
        while True:
            c = randint(0, 3)
            # up
            if c == 0 and self.y-1 >= 0:
                self.y -= 1
                break
            # down
            if c == 1 and self.y+1 < var["height"]:
                self.y += 1
                break
            # right
            if c == 2 and self.x+1 < var["width"]:
                self.x += 1
                break
            # left
            if c == 3 and self.x-1 >= 0:
                self.x -= 1
                break
        world.mapChange(self.py, self.px, OrganismType.EMPTY.value)
        world.mapChange(self.y, self.x, self.type)
        return 0

    def moveBack(self, world):
        world.mapChange(self.py, self.px, self.type)
        self.x = self.px
        self.y = self.py

    def collision(self, world, o, cn):
        if self.type == o.T():
            self.moveBack(world)
            return self.breed(world)
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(world, self, False)
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
