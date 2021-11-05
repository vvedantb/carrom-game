import pygame

class Particle:
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