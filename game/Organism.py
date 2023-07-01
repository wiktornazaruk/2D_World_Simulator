from var import var
from random import randint
from OrganismType import OrganismType

class Organism:
    def __init__(self, world, yy, xx, stre):
        self.strength = stre
        self.initiative = 0
        self.y = yy
        self.x = xx
        self.type = OrganismType.EMPTY.value
        self.state = True

    def action(self, world, direction):
        pass
    def collision(self, world, o, cn):
        pass
    def birth(self, world, yy, xx):
        pass

    def S(self):
        return self.strength
    def I(self):
        return self.initiative
    def T(self):
        return self.type
    def Y(self):
        return self.y
    def X(self):
        return self.x
    def alive(self):
        return self.state
    def die(self):
        self.state = False
    def upgradeS(self):
        self.strength += 1

    def doCollide(self, o):
        if self != o and self.X() == o.X() and self.Y() == o.Y() and o.alive() and self.alive():
            return True
        else:
            return False

    def save(self):
        s = ""
        if self.state:
            s += str(self.type) + "\n"
            s += str(self.y) + "\n"
            s += str(self.x) + "\n"
            s += str(self.strength) + "\n"
            s += "-"
        return s

    def breed(self, world):
        if 0 <= self.y < var["height"] and 0 <= self.x < var["width"]:
            d = [False, False, False, False]
            kiddoY = self.y
            kiddoX = self.x

            if self.y - 1 >= 0:
                if world.map[self.y - 1][self.x] == OrganismType.EMPTY.value:
                    d[0] = True
            if self.y + 1 < var["height"]:
                if world.map[self.y + 1][self.x] == OrganismType.EMPTY.value:
                    d[1] = True
            if self.x + 1 < var["width"]:
                if world.map[self.y][self.x + 1] == OrganismType.EMPTY.value:
                    d[2] = True
            if self.x - 1 >= 0:
                if world.map[self.y][self.x - 1] == OrganismType.EMPTY.value:
                    d[3] = True

            if d[0] or d[1] or d[2] or d[3]:
                while True:
                    c = randint(0, 3)
                    if c == 0 and d[0]:
                        kiddoY -= 1
                        break
                    elif c == 1 and d[1]:
                        kiddoY += 1
                        break
                    elif c == 2 and d[2]:
                        kiddoX += 1
                        break
                    elif c == 3 and d[3]:
                        kiddoX -= 1
                        break
                return self.birth(world, kiddoY, kiddoX)
        return 0
