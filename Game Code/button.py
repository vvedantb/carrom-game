import pygame as p #Allows pygame to be referred as "p" at any point in the program
p.font.init() #Initialises the font module

WIDTH, HEIGHT = 1600, 900 
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
clock = p.time.Clock()
#font = p.font.SysFont("Calibri", 20)



class Button:
    def __init__(self, bg_color, text_color, text, font, pos, size):
        self.bg_color = bg_color
        self.text_color = text_color
        if self.text == "":
            self.text = "Test"
        else:
            self.text = text
        self.font = font
        self.x, self.y = pos
        self.width, self.height = size

    def show(self):   
        screen.blit(self.surface, (self.x, self.y))

    def draw_text(self):
        textobj = self.font.render(self.text, 1, self.text_color)
        textrect = textobj.get_rect()
        textrect.topleft = (self.x, self.y)
        surface.blit(textobj, textrect)

    # def draw_text(text, font, color, surface, x, y):
    #     textobj = font.render(text, 1, color)
    #     textrect = textobj.get_rect()
    #     textrect.topleft = (x,y)
    #     surface.blit(textobj, textrect)

#    def change_text(self):
