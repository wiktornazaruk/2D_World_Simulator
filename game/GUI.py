import tkinter
from PIL import ImageTk, Image
from World import World
from var import var
from colors import colors
import os

class GUI:
    def __init__(self):
        # window initialisation
        self.root = tkinter.Tk()
        self.root.geometry('418x456')
        self.root.resizable(width=False, height=False)
        # dirs
        self.base_dir = os.path.dirname(__file__)
        self.icons_dir = os.path.join(self.base_dir, 'icons')
        # loading icons
        self.icon = []
        self.add_icons(['Empty', 'Human', 'Sheep', 'Wolf', 'Fox', 'Turtle', 
                        'Antelope', 'Cybersheep', 'Grass', 'SowThistle', 
                        'Guarana', 'Belladonna', 'Hogweed'])
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
        self.root.iconphoto(False, ImageTk.PhotoImage(file=os.path.join(self.icons_dir, "Earth.png")))
        self.world.mainLoop(self)
    
    # adds icons to self.icon based on a list of character names.
    def add_icons(self, character_names):
        for character in character_names:
            image_path = os.path.join(self.icons_dir, f"{character}.png")
            if os.path.exists(image_path):
                self.icon.append(ImageTk.PhotoImage(Image.open(image_path).resize((var["tile_size"], var["tile_size"]), Image.ANTIALIAS)),)
            else:
                print(f"Warning: Image '{image_path}' not found.")

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
        # exit the game
        if event.keysym == 'Escape': 
            self.root.destroy()
            self.world.decisionChange(7)
        # save the game
        if event.keysym == 'Home':
            self.world.decisionChange(5)
        # load a game
        if event.keysym == 'Insert':
            self.world.decisionChange(6)
        # special ability (immortality) and automatically next turn
        if event.keysym == 'End':
            self.world.decisionChange(4)
        # arrows - human movement and automatically next turn
        if event.keysym == 'Up':
            self.world.decisionChange(0)
        if event.keysym == 'Down':
            self.world.decisionChange(1)
        if event.keysym == 'Right':
            self.world.decisionChange(2)
        if event.keysym == 'Left':
            self.world.decisionChange(3)
        # play music
        if event.char.lower() == 'm':
            self.world.decisionChange(8)
