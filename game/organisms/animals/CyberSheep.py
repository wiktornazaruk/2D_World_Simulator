from organisms.Animal import Animal
from var import var
from random import randint
from OrganismType import OrganismType
import OrganismStrength as s

class CyberSheep (Animal):
    def __init__(self, world, yy, xx, stre=s.cybersheep):
        self.strength = stre
        self.initiative = 4
        self.y = yy
        self.x = xx
        self.type = OrganismType.CYBERSHEEP.value
        self.state = True
        self.py = self.y
        self.px = self.x
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return CyberSheep(world, yy, xx)

    def action(self, world, direction):
        self.py = self.y
        self.px = self.x
        a = 0
        b = 0
        cur = var["shpsw"]
        min = var["shpsw"]
        my = 0
        mx = 0
        # searching for the closest hogweed
        for i in range(var["height"]):
            for j in range(var["width"]):
                if world.map[i][j] == OrganismType.HOGWEED.value:
                    a = i - self.y
                    b = j - self.x
                    cur = (a * a) + (b * b)
                    if cur < min:
                        min = cur
                        my = i
                        mx = j
        if min != var["shpsw"]:
            #--------------------
            a = my - (self.py-1)
            b = mx - self.px
            cur = (a * a) + (b * b)
            if cur < min:
                self.y = self.py
                self.x = self.px
                self.y -= 1
                min = cur
            # --------------------
            a = my - (self.py+1)
            cur = (a * a) + (b * b)
            if cur < min:
                self.y = self.py
                self.x = self.px
                self.y += 1
                min = cur
            # --------------------
            a = my - self.py
            b = mx - (self.px+1)
            cur = (a * a) + (b * b)
            if cur < min:
                self.y = self.py
                self.x = self.px
                self.x += 1
                min = cur
            # --------------------
            b = mx - (self.px-1)
            cur = (a * a) + (b * b)
            if cur < min:
                self.y = self.py
                self.x = self.px
                self.x -= 1
                min = cur
        else:
            while True:
                c = randint(0, 3)
                if c == 0 and self.y-1 >= 0:
                    self.y -= 1
                    break
                if c == 1 and self.y+1 < var["height"]:
                    self.y += 1
                    break
                if c == 2 and self.x+1 < var["width"]:
                    self.x += 1
                    break
                if c == 3 and self.x-1 >= 0:
                    self.x -= 1
                    break
        world.mapChange(self.py, self.px, OrganismType.EMPTY.value)
        world.mapChange(self.y, self.x, self.type)
        return 0

    def collision(self, world, o, cn):
        if self.type == o.T():
            self.moveBack(world)
            return self.breed(world)
        elif o.T() == OrganismType.HOGWEED.value:
            o.die()
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(world, self, False)
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
