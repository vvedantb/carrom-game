import pygame as p #Allows p to be referred as "p" at any point in the program
p.font.init() #Initialises the font module

WIDTH, HEIGHT = 1600, 900 
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
clock = p.time.Clock()
#font = p.font.SysFont("Calibri", 20)


#Some help from TechWithTim: https://www.youtube.com/watch?v=4_9twnEduFA
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self. y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, text_size, outline=None):
        if outline:
            p.draw.rect(screen, outline, ( self.x-2, self.y-2, self.width+4, self.height+4 ), 0)
        p.draw.rect(screen, self.color, ( self.x, self.y, self.width, self.height ), 0)

        if self.text != "":
            font = p.font.SysFont("Arial", text_size)
            text = font.render(self.text, 1, ( 0, 0, 0 ))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse_collide(self):
        mx, my = p.mouse.get_pos() 
        if button.collidepoint((mx, my)): 
            if mouse_click: 
                return True