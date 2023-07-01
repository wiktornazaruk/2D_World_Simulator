import tkinter
from PIL import ImageTk, Image
from World import World
from var import var
from colors import colors

class GUI:
    def __init__(self):
        # window initialisation
        self.root = tkinter.Tk()
        self.root.geometry('418x456')
        self.root.resizable(width=False, height=False)
        # loading icons
        self.icon = [
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Empty.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Human.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Sheep.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Wolf.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Antelope.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Turtle.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Fox.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Cybersheep.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Grass.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/SowThistle.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Guarana.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Belladonna.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open('C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Hogweed.png').resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS))
        ]
        # placing cells
        self.box = [
            [
                tkinter.Button(self.root, height=var["tile_size"], width=var["tile_size"], background=colors["green"], image=self.icon[0])
                for y in range(var["height"])
            ] for x in range(var["width"])
        ]
        for y in range(var["height"]):
            for x in range(var["width"]):
                self.box[y][x].configure(command=(lambda a=y, b=x: self.world.addByClick(self, a, b)))
        self.boxmen = [
            tkinter.Button(self.root, height=var["tile_size"], width=var["tile_size"], background=colors["magenta_dye"], image=self.icon[i+2])
            for i in range(11)
        ]
        for i in range(11):
            self.boxmen[i].configure(command=(lambda a=i: self.world.selectedAnimalChange(a+2)))
        # looping
        self.root.bind_all('<Key>', self.key)
        self.world = World()
        self.root.title('2D World Simulator Wiktor Nazaruk s190454')
        self.root.iconphoto(False, ImageTk.PhotoImage(file='C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/python/icons/Earth.png'))
        self.world.mainLoop(self)

    # display function
    def display(self, world):
        for y in range(var["height"]):
            for x in range(var["width"]):
                self.box[y][x].configure(image=self.icon[self.world.map[y][x]])
                self.box[y][x].grid(row=y, column=x)
        for i in range(11):
            self.boxmen[i].place(y=418, x=i*1.189*var["tile_size"])
        self.root.update()

    # key events
    def key(self, event):
        if event.keysym == 'Escape':
            self.root.destroy()
            self.world.decisionChange(7)
        if event.keysym == 'Home':
            self.world.decisionChange(5)
        if event.keysym == 'Insert':
            self.world.decisionChange(6)
        if event.keysym == 'End':
            self.world.decisionChange(4)
        if event.keysym == 'Up':
            self.world.decisionChange(0)
        if event.keysym == 'Down':
            self.world.decisionChange(1)
        if event.keysym == 'Right':
            self.world.decisionChange(2)
        if event.keysym == 'Left':
            self.world.decisionChange(3)
        if event.char.lower() == 'm':
            self.world.decisionChange(8)