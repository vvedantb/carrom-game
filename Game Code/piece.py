import pygame as p #Allows p to be referred as "p" at any point in the program
p.font.init() #Initialises the font module

WIDTH, HEIGHT = 1600, 900 
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
clock = p.time.Clock()

class Piece:
    def __init__(self, x, y, size, mass, state, color=None):
    
        self.x, self.y = x, y
        self.size = size
        self.mass = mass
        self.state = state
        if self.state == "queen":
            self.color = (153, 0, 102)
        elif self.state == "brown":
            self.color = (101, 67, 33)
        elif self.state == "black":
            self.color = (0, 0, 0)
        self.color = color

        self.speed = 0
        self.angle = 0

    def draw(self):
        p.draw.circle(
            screen, 
            self.color, 
            int(self.x), int(self.y), 
            self.size
        )

    def show(self, x, y):
        pass

    def move(self):
        pass

    def bounce(self):
        pass
