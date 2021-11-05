import pygame as p # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed
import math # For collision function
from pygame.locals import * # Imports constants that are used by the Pygame module
from striker import Striker

clock = p.time.Clock() # Creates a clock object that is used to track amount of time
p.init() # Initialises all imported Pygame modules 

p.display.set_caption("Carrom Game") # Sets program caption 
icon = p.image.load("Game Code/icon.png") # Loads the icon image
p.display.set_icon(icon) # Sets the icon image


# p.mixer.music.load("Game Code/wholeotherwave.wav") # Loads the music file
# p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1
# p.mixer.music.set_volume(0.25) # Sets the music volume

WIDTH, HEIGHT = 1600, 900

BROWN = (138, 87, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREY = (125, 125, 125)
LIGHT_BROWN = (191, 134, 0)

Board = p.image.load("Game Code/board.jpg")


screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
p.font.init()
font = p.font.SysFont('Arial Bold', 40) # Sets the font used within the program

BLACK_PIECE = p.image.load("Game Code/Assets/black-piece.png")
#BROWN_PIECE = 
PLAYER_STRIKER = p.draw.circle(screen, BLUE, (0,0), 2)
ENEMY_STRIKER = p.draw.circle(screen, RED, (0,0), 2)

FPS = 60 # Sets the refresh rate, i.e. 60 times a second

mouse_click = False # If a click has been made by the mouse

screen.fill(BROWN)




def collide(p1, p2):
    pass



def drawText(text, font, color, surface, x, y): # Writes text onto the screen of the program
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


def mainMenu():     
    while True:
        screen.fill(BROWN)
        mouse_click = False # If a click has been made by the mouse

        drawText("Main Menu", font, WHITE, screen, 20, 20)

        button_height = screen.get_height()/20
        button_width = screen.get_width()/10

        game_button = p.Rect(button_width-20, (WIDTH/10)+5, button_width, button_height)
        options_button = p.Rect(button_width-20, (2*WIDTH/10)+5, button_width, button_height)
        settings_button = p.Rect(button_width-20, (3*WIDTH/10)+5, button_width, button_height)
        quit_button = p.Rect(button_width-20, (4*WIDTH/10)+5, button_width/2, button_height)
        music_button = p.Rect(button_width-20, (6*WIDTH/10)+5, button_width, button_height)

      
        p.draw.rect(screen, BLACK, game_button) # Draws a rectangle onto the screen in white colour for button 1
        p.draw.rect(screen, BLACK, options_button)
        p.draw.rect(screen, BLACK, settings_button)
        p.draw.rect(screen, BLACK, quit_button)
        p.draw.rect(screen, BLACK, music_button)

        text_width = screen.get_width()/10
        text_height = screen.get_height()/6

        drawText("Play Game", font, WHITE, screen, text_height, 1.1*text_width) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
        drawText("Options", font, WHITE, screen, text_height, 2.1*text_width)
        drawText("Settings", font, WHITE, screen, text_height, 3.1*text_width)
        drawText("Quit", font, WHITE, screen, text_height, 4.1*text_width)
        drawText("Play Music?", font, WHITE, screen, text_height, 5.1*text_width)

        events = p.event.get()
        for event in events:
            if event.type == QUIT: # Checks if the cross (top right button) has been pressed
                p.quit() # Program ends
                sys.exit()
            if event.type == KEYDOWN: # Checks if a key has been pressed
                if event.key == K_ESCAPE: # Checks if escape key has been pressed
                    p.quit() # Programs ends
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True

        mx, my = p.mouse.get_pos() # Retrieves the current position of where the mouse is

        if game_button.collidepoint((mx, my)): # Checks if mouse location overlaps button 1 location
            if mouse_click: # Checks if button has been clicked
                game()
        if options_button.collidepoint((mx, my)):
            if mouse_click:
                options()
        if settings_button.collidepoint((mx, my)): 
            if mouse_click:
                settings()
        if quit_button.collidepoint((mx, my)): 
            if mouse_click:
                quit_game()
        if music_button.collidepoint((mx, my)):
            if mouse_click:
                play_music()

        p.display.update() # Updates display
        clock.tick(FPS) 




































def game():    
    run = True

    while run:
        screen.fill(BROWN)
        BOARD_WIDTH, BOARD_HEIGHT = 900, 900
        BG = p.transform.rotate(p.transform.scale(p.image.load(os.path.join('Game Code\Assets', 'carrom-board.jpg')), ((int(screen.get_width()*0.5625)), screen.get_height())), 89.5)
        screen.blit(BG, (int(screen.get_width()/2 - (BOARD_WIDTH/2)), 0)) # Puts board in the middle

        drawText("Play Game", font, BLACK, screen, 20, 20) # Writes text onto the screen 

        player_striker = Striker.draw_circle(screen, RED, (BOARD_WIDTH/2, BOARD_HEIGHT/2), 15)
        enemy_striker = Striker.draw_circle(screen, BLUE, (BOARD_WIDTH/2 + 15, BOARD_HEIGHT/2), 15)

        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    striker_shot()

        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()

        p.draw.circle(screen, RED, (2*WIDTH/6, 2*HEIGHT/8), 15) 
        p.draw.circle(screen, RED, (2*WIDTH/6, 6*HEIGHT/8), 15) 
        
        p.draw.circle(screen, RED, (4*WIDTH/6, 2*HEIGHT/8), 15) 
        p.draw.circle(screen, RED, (4*WIDTH/6, 6*HEIGHT/8), 15)

        p.draw.circle(screen, RED, (4*WIDTH/6 - 30, 6*HEIGHT/8 + 50), 15) 
        p.draw.circle(screen, RED, (2*WIDTH/6 + 30, 6*HEIGHT/8 + 50), 15) 
        
        p.draw.circle(screen, RED, (4*WIDTH/6 - 30, 2*HEIGHT/8 - 50), 15) 
        p.draw.circle(screen, RED, (2*WIDTH/6 + 30, 2*HEIGHT/8 - 50), 15) # Striker boundaries
        
        p.draw.circle(screen, RED, (WIDTH/2, HEIGHT/2), 20) # Center circle

        p.draw.circle(screen, DARK_GREY, (WIDTH/4 + 30, HEIGHT/8 - 30), 30) # Top left
        p.draw.circle(screen, DARK_GREY, (WIDTH/4 + 30, 7*HEIGHT/8 + 30), 30) # Bottom left
        p.draw.circle(screen, DARK_GREY, (3*WIDTH/4 - 30, HEIGHT/8 - 30), 30) # Top right
        p.draw.circle(screen, DARK_GREY, (3*WIDTH/4 - 30, 7*HEIGHT/8 + 30), 30) # Bottom right corner holes

        for i in range(20):
            p.draw.circle(screen, DARK_GREY, (i* WIDTH/100, HEIGHT/2), 10)
                    
        for i in range(4):
            p.draw.rect(screen, (0,0,0), ((WIDTH/4)+i,(HEIGHT)+i,155,155), 2)

        p.display.update()
        clock.tick(FPS)






def play_music():
    run = True
    while run:
        drawText('Press "Y" to start music', font, BLACK, screen, 20, 20)
        drawText('Press "N" to stop music', font, BLACK, screen, 60, 20)
        drawText('Press "P" to pause music', font, BLACK, screen, 100, 20)
        
        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                if event.key == K_y:
                    p.mixer.music.load("Game Code/wholeotherwave.wav") # Loads the music file
                    p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1
                    p.mixer.music.set_volume(0.25) # Sets the music volume
                if event.key == K_n:
                    pygame.mixer.music.stop()
                

        p.display.update()
        clock.tick(FPS)    




















































def options():
    run = True
    while run:
        screen.fill(BROWN)
        drawText('Options', font, BLACK, screen, 20, 20)
        
        button_7 = p.Rect(20,60,300,50)
        #p.draw.rect(screen, WHITE, button_7)
        p.draw.rect(screen, BLACK, p.Rect(30, 30, 60, 60),  2, 0, 0, 3)
        p.draw.rect(screen, BLACK, button_7,  border_bottom_right_radius=5)
        drawText('Select Striker Colour', font, BLACK, screen, 20, 60)

        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        p.display.update()
        clock.tick(FPS)


def settings():

    run = True
    
    while run:
        screen.fill(BROWN)

        drawText('Settings', font, WHITE, screen, 20, 20)

        drawText('X-Senstivity', font, WHITE, screen, 20, 60)
        drawText('Y-Senstivity', font, WHITE, screen, 20, 100)
        
        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        
        p.display.update()
        clock.tick(FPS)



def quit_game():
    run = True
    while run:
        screen.fill(BROWN)

        drawText('Quit?', font, BLACK, screen, 20, 20)
        drawText('Press Q to confirm', font, BLACK, screen, 20, 60)
        drawText('Press ESC to return', font, BLACK, screen, 20, 100)
        
        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
                    p.quit()
        
        p.display.update()
        clock.tick(FPS)


mainMenu()


        

class Piece():
    def __init__(self, screen, color, posX, posY, radius, width, height ):
        self.screen = screen 
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.width = width
        self.height = height
        self.state = 'stopped'

        # Ball Movement
        self.dx = 0
        self.dy = 0
        self.show()

    def show():
        p.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def move(self):
        if self.state == 'up':
            self.posX += self.dx
        elif self.state == 'down':
            self.posY = self.dy

class Score:
    def __init__(self, screen, points, posX, posY):
        self.screen = screen
        self.points = points
        self.posX = posX
        self.posY = posY
        self.font = p.font.SysFont("monospace", 80, bold=True)
        self.label = self.font.render(self.points, 0, WHITE)
        self.show()

    def show(self):
        self.screen.blit(self.label, (self.posX - self.label.get_rect().width//2, self.posY))

    def increase(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points, 0, WHITE)

class CollisionManager:
    pass

    
    

