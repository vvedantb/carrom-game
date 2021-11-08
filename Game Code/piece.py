import pygame as p

class Piece:
    def __init__(self, color, x, y, size, mass):
        self.x,y = x,y
        self.color = color
        self.size = size
        self.mass = mass

        self.speed = 0
        self.angle = 0

    def show(self, x, y):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size)


    def move(self):
        pass

    def bounce(self):
        pass



    # def move(self):
    #     if self.state == 'up':
    #         self.posX += self.dx
    #     elif self.state == 'down':
    #         self.posY = self.dy