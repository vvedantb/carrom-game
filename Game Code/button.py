import pygame as p #Allows p to be referred as "p" at any point in the program
p.font.init() #Initialises the font module

WIDTH, HEIGHT = 1600, 900 
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
clock = p.time.Clock()


#Some help from TechWithTim: https://www.youtube.com/watch?v=4_9twnEduFA
class Button:
    def __init__(self, color, x, y, width, height, text_color, text_size, outline=None, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.text_size = text_size
        self.outline = outline
        self.text = text

    def draw(self, screen, outline=None):
        if self.outline:
            p.draw.rect(screen, self.outline, ( self.x-2, self.y-2, self.width+4, self.height+4 ), 0, 10)
        p.draw.rect(screen, self.color, ( self.x, self.y, self.width, self.height ), 0, 10)

        if self.text != "":
            font = p.font.SysFont("Arial", self.text_size)
            text = font.render(self.text, 1, self.text_color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse_collide(self):
     
        mx, my = p.mouse.get_pos() 

        if mx > self.x and mx < self.x + self.width:
            if my > self.y and my < self.y + self.height:
                return True
        return False

    def change_color(self):
        pass # TODO: Add code to change color when the button has been pressed for the play music function