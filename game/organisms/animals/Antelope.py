from organisms.Animal import Animal
from var import var
from random import randint
from OrganismType import OrganismType
import OrganismStrength as s

class Antelope (Animal):
    def __init__(self, world, yy, xx, stre=s.antelope):
        self.strength = stre
        self.initiative = 4
        self.y = yy
        self.x = xx
        self.type = OrganismType.ANTELOPE.value
        self.state = True
        self.py = self.y
        self.px = self.x
        self.escape = 0
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Antelope(world, yy, xx)

    def action_one(self, world, cameFrom):
        if cameFrom == 0:
            cameFrom = 1
        elif cameFrom == 1:
            cameFrom = 0
        elif cameFrom == 2:
            cameFrom = 3
        elif cameFrom == 3:
            cameFrom = 2
        while True:
            c = randint(0, 3)
            if c != cameFrom:
                if c == 0 and self.y-1 >= 0:
                    self.y -= 1
                    break
                elif c == 1 and self.y+1 < var["height"]:
                    self.y += 1
                    break
                elif c == 2 and self.x+1 < var["width"]:
                    self.x += 1
                    break
                elif c == 3 and self.x-1 >= 0:
                    self.x -= 1
                    break
        return c

    def action(self, world, direction):
        self.py = self.y
        self.px = self.x
        self.action_one(world, self.action_one(world, 4))
        world.mapChange(self.py, self.px, OrganismType.EMPTY.value)
        world.mapChange(self.y, self.x, self.type)
        return 0

    def collision(self, world, o, cn):
        # setting new escape route
        c = randint(0, 1)
        self.escape = 0
        if self.y - 1 >= 0 and world.map[self.y - 1][self.x] == OrganismType.EMPTY.value:
            self.escape = 1
        elif self.y + 1 < var["height"] and world.map[self.y + 1][self.x] == OrganismType.EMPTY.value:
            self.escape = 2
        elif self.x + 1 < var["width"] and world.map[self.y][self.x + 1] == OrganismType.EMPTY.value:
            self.escape = 3
        elif self.x - 1 >= 0 and world.map[self.y][self.x - 1] == OrganismType.EMPTY.value:
            self.escape = 4
        else:
            self.escape = 0
        # collision
        if self.type == o.T():
            self.moveBack(world)
            return self.breed(world)
        elif c > 0 and self.escape > 0:
            world.mapChange(self.y, self.x, o.T())
            if self.escape == 1:
                self.y -= 1
            elif self.escape == 2:
                self.y += 1
            elif self.escape == 3:
                self.x += 1
            elif self.escape == 4:
                self.x -= 1
            self.escape = 0
            self.state = True
            cn = False
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(world, self, False)
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
