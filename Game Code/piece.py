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
        self.state = state
        self.color = color

        self.speed = 0
        self.angle = 0

    def draw(self):
        outline = 2
        if self.state == "queen":
            self.color = (153, 0, 102)
        elif self.state == "brown":
            self.color = (173, 94, 46)
        elif self.state == "black":
            self.color = (72, 73, 76)
        
        p.draw.circle(screen, (255,255,255), (int(self.x), int(self.y)), 12, 0)
        
        p.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def get_width(self):
        pass

    def get_height(self):
        pass

    def show(self, x, y):
        pass

    def move(self):
        pass

    def bounce(self):
        pass
