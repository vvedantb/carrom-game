import pygame as p

class Striker:
    
    def __init__(self, screen, color, position, radius):
        self.screen = screen
        self.color = color
        self.position = position
        self.radius = radius
    
    def draw_circle(screen, color, position, radius):
        p.draw.circle(screen, color, position, radius)
    
    def shoot_striker(self, color):
        keys = p.key.get_pressed()
        if keys[p.K_SPACE]:
            p.draw.rect(screen, color, (x, y, width, height))
            p.display.update() 

    
    def return_to_base(self):
        pass