from var import var
from OrganismType import OrganismType
import OrganismStrength as s
from organisms.animals.Human import Human
from organisms.animals.Sheep import Sheep
from organisms.animals.Wolf import Wolf
from organisms.animals.Fox import Fox
from organisms.animals.Turtle import Turtle
from organisms.animals.Antelope import Antelope
from organisms.animals.CyberSheep import CyberSheep
from organisms.plants.Grass import Grass
from organisms.plants.SowThistle import SowThistle
from organisms.plants.Guarana import Guarana
from organisms.plants.Belladonna import Belladonna
from organisms.plants.Hogweed import Hogweed
import pygame
from music import music
from os.path import exists

class World:
    def __init__(self):
        self.decision = 10
        self.selectedAnimal = OrganismType.EMPTY.value
        self.humanAlive = True
        self.organisms = []
        self.map = [
            [0 for y in range(var["height"])] for x in range(var["width"])
        ]
        self.organisms.append(Human(self, 1, 1))
        self.isMusicPlaying = False

    def addNotification(self, typ, happening):
        s = ""
        if typ == OrganismType.HUMAN.value:
            s += "Human "
        elif typ == OrganismType.SHEEP.value:
            s += "Sheep "
        elif typ == OrganismType.WOLF.value:
            s += "Wolf  "
        elif typ == OrganismType.ANTELOPE.value:
            s += "Antelope "
        elif typ == OrganismType.TURTLE.value:
            s += "Turtle "
        elif typ == OrganismType.FOX.value:
            s += "Fox "
        elif typ == OrganismType.CYBERSHEEP.value:
            s += "Cyber Sheep "
        elif typ == OrganismType.GRASS.value:
            s += "Grass "
        elif typ == OrganismType.SOWTHISTLE.value:
            s += "Sow Thistle "
        elif typ == OrganismType.GUARANA.value:
            s += "Guarana "
        elif typ == OrganismType.BELLADONNA.value:
            s += "Belladonna "
        elif typ == OrganismType.HOGWEED.value:
            s += "Sosnovskys Hogweed "
        else:
            s += "Organism"

        if happening:
            s += "died"
        elif typ <= OrganismType.CYBERSHEEP.value:
            s += "breeded"
        else:
            s += "sawed"

        print(s)

    def addBeing(self, o):
        if o != OrganismType.EMPTY.value:
            self.addNotification(o.T(), False)
            if len(self.organisms) == 0:
                self.organisms.append(o)
            else:
                for i in range(len(self.organisms)):
                    if self.organisms[i].I() < o.I():
                        self.organisms.insert(i, o)
                        break
                    elif i == len(self.organisms)-1:
                        self.organisms.append(o)

    def load(self, gui):
        # returning to starting conditions
        self.organisms.clear()
        for y in range(var["height"]):
            for x in range(var["width"]):
                self.map[y][x] = 0
        self.humanAlive = True
        # file reading and adding organisms
        if not exists("save.txt"):
            print("Can't load. File does not exists!")
            exit()
        file = open("save.txt", "r")
        yy = 0
        xx = 0
        stre = 0
        abi = 0
        cnt = 0
        while True:
            line = file.readline()
            line2 = ""
            for i in range(len(line)):
                if line[i] != '\n':
                    line2 += line[i]
            line = line2
            if line == "--":
                break
            elif line == "-":
                self.addByClick(gui, yy, xx, stre, True, abi)
                cnt = -1
            elif cnt == 0:
                self.selectedAnimal = int(line)
            elif cnt == 1:
                yy = int(line)
            elif cnt == 2:
                xx = int(line)
            elif cnt == 3:
                stre = int(line)
            elif cnt == 4:
                abi = int(line)
            cnt += 1
        file.close()
        # final touches
        self.decision = 10
        self.selectedAnimal = OrganismType.EMPTY.value

    def save(self):
        file = open("save.txt", "w")
        for i in range(len(self.organisms)):
            print(self.organisms[i].save(), file=file)
        print("--", file=file)
        file.close()

    def mainLoop(self, gui):
        while self.humanAlive:
            i = 0
            while i < len(self.organisms):
                # human actions
                if self.organisms[i].T() == OrganismType.HUMAN.value:
                    # setting variables
                    self.decision = 10
                    self.humanAlive = self.organisms[i].humanAlive()
                    gui.display(self)
                    # decisions
                    while self.decision > 4:
                        gui.root.update()
                        if self.decision == 5:
                            self.save()
                            self.decision = 10
                        # exiting or loading
                        elif self.decision == 7 or self.decision == 6:
                            break
                        # music
                        elif self.decision == 8:
                            if not self.isMusicPlaying:
                                self.play_music()
                                self.isMusicPlaying = True
                            else:
                                self.stop_music()
                                self.isMusicPlaying = False
                            self.decision = 10
                    # exiting or loading
                    if self.decision == 7 or self.decision == 6:
                        break
                    else:
                        self.organisms[i].action(self, self.decision)
                # organsims actions
                elif self.organisms[i].alive():
                    if self.organisms[i].T() == OrganismType.SOWTHISTLE.value:
                        for k in [1, 2, 3]:
                            self.addBeing(self.organisms[i].action(self, 0))
                    else:
                        self.addBeing(self.organisms[i].action(self, 0))
                # collisions
                for j in range(len(self.organisms)):
                    if self.organisms[i].doCollide(self.organisms[j]):
                        self.addBeing(self.organisms[i].collision(self, self.organisms[j], True))
                # loop movement
                i += 1
            # remove dead organisms
            for i in sorted(range(len(self.organisms)), reverse=True):
                if self.organisms[i].T() != OrganismType.HUMAN.value and not self.organisms[i].alive():
                    self.addNotification(self.organisms[i].T(), True)
                    self.organisms.remove(self.organisms[i])
            # loading
            if self.decision == 6:
                self.load(gui)
            # exiting
            elif self.decision == 7:
                break
        print("Human died. Game over.")

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(music["death"])
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def decisionChange(self, d):
        self.decision = d

    def selectedAnimalChange(self, d):
        self.selectedAnimal = d

    def addByClick(self, gui,  yy, xx, stre=0, save=False, abi=0):
        if not self.selectedAnimal == OrganismType.EMPTY.value:
            if self.selectedAnimal == OrganismType.HUMAN.value:
                if not save:
                    stre = s.human
                self.addBeing(Human(self, yy, xx, stre, abi))
            elif self.selectedAnimal == OrganismType.SHEEP.value:
                if not save:
                    stre = s.sheep
                self.addBeing(Sheep(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.WOLF.value:
                if not save:
                    stre = s.wolf
                self.addBeing(Wolf(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.ANTELOPE.value:
                if not save:
                    stre = s.antelope
                self.addBeing(Antelope(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.TURTLE.value:
                if not save:
                    stre = s.turtle
                self.addBeing(Turtle(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.FOX.value:
                if not save:
                    stre = s.fox
                self.addBeing(Fox(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.CYBERSHEEP.value:
                if not save:
                    stre = s.cybersheep
                self.addBeing(CyberSheep(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.GRASS.value:
                if not save:
                    stre = 0
                self.addBeing(Grass(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.SOWTHISTLE.value:
                if not save:
                    stre = 0
                self.addBeing(SowThistle(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.GUARANA.value:
                if not save:
                    stre = 0
                self.addBeing(Guarana(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.BELLADONNA.value:
                if not save:
                    stre = s.belladonna
                self.addBeing(Belladonna(self, yy, xx, stre))
            elif self.selectedAnimal == OrganismType.HOGWEED.value:
                if not save:
                    stre = s.hogweed
                self.addBeing(Hogweed(self, yy, xx, stre))
            gui.display(self)
            

    def mapChange(self, yy, xx, c):
        if 0 <= yy < var["height"] and 0 <= xx < var["width"]:
            self.map[yy][xx] = c
