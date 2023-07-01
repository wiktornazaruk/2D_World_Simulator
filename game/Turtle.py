from Animal import Animal
from var import var
from random import randint
from OrganismType import OrganismType
import OrganismStrength as s


class Turtle (Animal):
    def __init__(self, world, yy, xx, stre=s.turtle):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.type = OrganismType.TURTLE.value
        self.state = True
        self.strength = stre
        self.initiative = 1
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Turtle(world, yy, xx)

    def action(self, world, decision):
        c = randint(0, 3)
        if c == 0:
            self.py = self.y
            self.px = self.x
            while True:
                c = randint(0, 3)
                if c == 1 and self.y-1 >= 0:
                    self.y -= 1
                    break
                if c == 2 and self.y+1 < var["height"]:
                    self.y += 1
                    break
                if c == 3 and self.x+1 < var["width"]:
                    self.x += 1
                    break
                if c == 4 and self.x-1 >= 0:
                    self.x -= 1
                    break
            world.mapChange(self.py, self.px, OrganismType.EMPTY.value)
            world.mapChange(self.y, self.x, self.type)
        return 0

    def collision(self, world, o, cn):
        if o.T() <= 7:
            if self.type == o.T():
                self.moveBack(world)
                return self.breed(world)
            elif o.S() < 5 and not cn:
                self.state = True
                o.moveBack(world)
            elif self.strength > o.S() or (self.strength == o.S() and cn):
                o.die()
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(world, self, False)
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
