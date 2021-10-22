import pygame # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed
from pygame.locals import * # Imports constants that are used by the Pygame module

clock = pygame.time.Clock() # Creates a clock object that is used to track amount of time
pygame.init() # Initialises all imported Pygame modules 
pygame.display.set_caption("Carrom Game") # Sets program caption 

WIDTH, HEIGHT = 1000, 1000

BROWN = (164,116,73)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Sets the display resolution
font = pygame.font.SysFont('Arial Bold', 40) # Sets the font used within the program

BLACK_PIECE = pygame.image.load(os.path.join('Game Code\Assets', 'black-piece.png'))
#BROWN_PIECE = 
PLAYER_STRIKER = pygame.draw.circle(screen, BLUE, (0,0), 2)
ENEMY_STRIKER = pygame.draw.circle(screen, RED, (0,0), 2)

FPS = 60 # Sets the refresh rate, i.e. 60 times a second

mouse_click = False # If a click has been made by the mouse

screen.fill(BROWN)


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

        mx, my = pygame.mouse.get_pos() # Retrieves the current position of where the mouse is

        button_height = screen.get_height()/20
        button_width = screen.get_width()/10

        game_button = pygame.Rect(button_width, button_height, 3*button_width, button_height)
        options_button = pygame.Rect(button_width, 3*button_height, 3*button_width, button_height)
        settings_button = pygame.Rect(button_width, 6*button_height, 3*button_width, button_height)
        quit_button = pygame.Rect(button_width, 9*button_height, 2*button_width, button_height)

        if game_button.collidepoint((mx,my)): # Checks if mouse location overlaps button 1 location
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
        
        pygame.draw.rect(screen, BLACK, game_button) # Draws a rectangle onto the screen in white colour for button 1
        pygame.draw.rect(screen, BLACK, options_button)
        pygame.draw.rect(screen, BLACK, settings_button)
        pygame.draw.rect(screen, BLACK, quit_button)

        text_width = screen.get_width()/10
        text_height = screen.get_height()/6

        drawText("Play Game", font, WHITE, screen, text_height, 1.25*text_width) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
        drawText("Options", font, WHITE, screen, text_height, 3.25*text_width)
        drawText("Settings", font, WHITE, screen, text_height, 6.25*text_width)
        drawText("Quit", font, WHITE, screen, text_height, 9.25*text_width)


        events = pygame.event.get()
        for event in events:
            if event.type == QUIT: # Checks if the cross (top right button) has been pressed
                pygame.quit() # Program ends
                sys.exit()
            if event.type == KEYDOWN: # Checks if a key has been pressed
                if event.key == K_ESCAPE: # Checks if escape key has been pressed
                    pygame.quit() # Programs ends
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True

        pygame.display.update() # Updates display
        clock.tick(FPS) 




































def game():    
    run = True

    while run:
        BG = pygame.transform.scale(pygame.image.load(os.path.join('Game Code\Assets', 'carrom-board.jpg')), (WIDTH, HEIGHT))
        screen.blit(BG, (0, 0))

        drawText("Play Game", font, BLACK, screen, ( screen.get_width()/20 ), ( screen.get_height()/10 )) # Writes text onto the screen 

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    striker_shot()
                    
        
        pygame.display.update()
        clock.tick(FPS)



def options():
    run = True
    while run:
        screen.fill(WHITE)
        drawText('Options', font, BLACK, screen, 20, 20)
        
        button_7 = pygame.Rect(20,60,300,50)
        #pygame.draw.rect(screen, WHITE, button_7)
        pygame.draw.rect(screen, BLACK, pygame.Rect(30, 30, 60, 60),  2, 0, 0, 3)
        pygame.draw.rect(screen, BLACK, button_7,  border_bottom_right_radius=5)
        drawText('Select Striker Colour', font, BLACK, screen, 20, 60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        pygame.display.update()
        clock.tick(FPS)


def settings():

    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Settings', font, WHITE, screen, 20, 20)

        drawText('X-Senstivity', font, WHITE, screen, 20, 60)
        drawText('Y-Senstivity', font, WHITE, screen, 20, 100)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        
        pygame.display.update()
        clock.tick(FPS)



def quit_game():
    run = True
    while run:
        screen.fill(BLACK)

        drawText('Quit?', font, BLACK, screen, 20, 20)
        drawText('Press Q to confirm', font, BLACK, screen, 20, 60)
        drawText('Press ESC to return', font, BLACK, screen, 20, 100)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
                    pygame.quit()
        
        pygame.display.update()
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
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

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
        self.font = pygame.font.SysFont("monospace", 80, bold=True)
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

    
    

