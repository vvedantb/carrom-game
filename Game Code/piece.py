import pygame as p

class Piece:
    def __init__(self, color, x, y, size, mass):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.mass = mass

    def move(self):
        pass

    def bounce(self):
        pass



    # def move(self):
    #     if self.state == 'up':
    #         self.posX += self.dx
    #     elif self.state == 'down':
    #         self.posY = self.dy