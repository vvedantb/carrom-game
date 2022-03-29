from time import sleep 
import math
import pygame as p #Allows p to be referred as "p" at any point in the program
p.font.init() #Initialises the font module

WIDTH, HEIGHT = 1600, 900 
WHITE = (255, 255, 255)
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
        self.power = 0

    def draw(self):
        outline = 2
        if self.state == "queen":
            self.color = (153, 0, 102)
        elif self.state == "brown":
            self.color = (173, 94, 46)
        elif self.state == "black":
            self.color = (72, 73, 76)
        elif self.state == "striker":
            self.color = (153,153,0)
        
        p.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

        p.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size-2, 2)

    def new_xy_pos(self):
        new_x = self.x + (self)

    def shot(self):
        if self.state == "striker":
            for i in range(0, self.power*5):
                sleep(0.1)
                self.y -= 1