from Animal import Animal
from var import var
from random import randint
from OrganismType import OrganismType
import OrganismStrength as s

class Fox (Animal):
    def __init__(self, world, yy, xx, stre=s.fox):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.type = OrganismType.FOX.value
        self.state = True
        self.strength = stre
        self.initiative = 7
        world.mapChange(self.y, self.x, self.type)

    def birth(self, world, yy, xx):
        return Fox(world, yy, xx)

    def type_to_strength(self, typ):
        if typ == OrganismType.HUMAN.value:
            return s.human
        elif typ == OrganismType.SHEEP.value: 
            return s.sheep
        elif typ == OrganismType.WOLF.value:
            return s.wolf
        elif typ == OrganismType.ANTELOPE.value:
            return s.antelope
        elif typ == OrganismType.TURTLE.value:
            return s.turtle
        elif typ == OrganismType.FOX.value:
            return s.fox
        elif typ == OrganismType.CYBERSHEEP.value:
            return s.cybersheep
        elif typ == OrganismType.HOGWEED.value:
            return s.hogweed
        elif typ == OrganismType.BELLADONNA.value:
            return s.belladonna
        else:
            return 0

    def action(self, world, direction):
        self.py = self.y
        self.px = self.x
        d = [False, False, False, False]

        if self.y - 1 > 0:
            if self.type_to_strength(world.map[self.y - 1][self.x]) <= self.strength:
                d[0] = True
        if self.y + 1 < var["height"]:
            if self.type_to_strength(world.map[self.y + 1][self.x]) <= self.strength:
                d[1] = True
        if self.x + 1 < var["width"]:
            if self.type_to_strength(world.map[self.y][self.x + 1]) <= self.strength:
                d[2] = True
        if self.x - 1 > 0:
            if self.type_to_strength(world.map[self.y][self.x - 1]) <= self.strength:
                d[3] = True

        if d[0] or d[1] or d[2] or d[3]:
            while True:
                c = randint(0, 3)
                if c == 0 and d[0]:
                    self.y -= 1
                    break
                elif c == 1 and d[1]:
                    self.y += 1
                    break
                elif c == 2 and d[2]:
                    self.x += 1
                    break
                elif c == 3 and d[3]:
                    self.x -= 1
                    break

        world.mapChange(self.py, self.px, OrganismType.EMPTY.value)
        world.mapChange(self.y, self.x, self.type)
        return 0
