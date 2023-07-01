from Animal import Animal
from var import var
from OrganismType import OrganismType
import OrganismStrength as s


class Human(Animal):
    def __init__(self, world, yy, xx, stre=s.human, abi=0):
        self.strength = stre
        self.initiative = 4
        self.y = yy
        self.x = xx
        self.type = OrganismType.HUMAN.value
        self.state = True
        self.py = self.y
        self.px = self.x
        self.ability = abi
        self.escape = 0
        world.mapChange(self.y, self.x, self.type)

    def humanAlive(self):
        if self.state or self.ability > 0:
            return True
        else:
            return False

    def save(self):
        s = ""
        s += str(self.type) + "\n"
        s += str(self.y) + "\n"
        s += str(self.x) + "\n"
        s += str(self.strength) + "\n"
        s += str(self.ability) + "\n"
        s += "-"
        return s

    def action(self, world, direction):
        if self.ability > 0:
            self.state = True
        if self.state:
            self.py = self.y
            self.px = self.x
            # up
            if direction == 0 and self.y-1 >= 0:
                self.y -= 1
            # down
            if direction == 1 and self.y+1 < var["height"]:
                self.y += 1
            # right
            if direction == 2 and self.x+1 < var["width"]:
                self.x += 1
            # left
            if direction == 3 and self.x-1 >= 0:
                self.x -= 1
            # special ability
            if direction == 4:
                self.ability = 6
            # special ability decay
            if self.ability > 0:
                self.ability -= 1
            world.mapChange(self.py, self.px, OrganismType.EMPTY.value)
            world.mapChange(self.y, self.x, self.type)
        else:
            world.mapChange(self.y, self.x, OrganismType.EMPTY.value)
        return 0

    def collision(self, world, o, cn):
        # setting new escape route
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
        if self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        elif self.ability > 0 and self.escape > 0:
            # escaping
            world.mapChange(self.y, self.x, o.T())
            if self.escape == 1:
                self.y -= 1
            if self.escape == 2:
                self.y += 1
            if self.escape == 3:
                self.x += 1
            if self.escape == 4:
                self.x -= 1
            self.state = True
            cn = False
            world.mapChange(self.y, self.x, self.type)
        elif self.ability > 0 and self.escape == 0:
            self.state = True
            if cn:
                self.moveBack(world)
            else:
                o.moveBack(world)
                world.mapChange(self.y, self.x, self.type)
        if cn:
            o.collision(world, self, False)
        if self.state:
            world.mapChange(self.y, self.x, self.type)
        return 0
