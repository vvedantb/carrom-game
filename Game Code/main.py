import pygame # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed



PLAYER_STRIKER = 
ENEMY_STRIKER = 


clock = pygame.time.Clock() # Creates a clock object that is used to track amount of time

from pygame.locals import * # Imports constants that are used by the Pygame module

pygame.init() # Initialises all imported Pygame modules 

pygame.display.set_caption("Carrom Game") # Sets program caption 

#CARROM_PIECE = pygame.image.load(os.path.join('images', 'carrom-piece.png'))

SCREEN_SIZE = (1280, 720)

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE) # Sets the display resolution

font = pygame.font.SysFont('Arial Bold', 40) # Sets the font used within the program




def drawText(text, font, color, surface, x, y): # Writes text onto the screen of the program
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


mouse_click = False # If a click has been made by the mouse

FPS = 60 # Sets the refresh rate, i.e. 60 times a second

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


def mainMenu():     
    while True:
        screen.fill(WHITE) # Fills the screen in the desired colour
        drawText("Main Menu", font, WHITE, screen, 20, 20)

        mx, my = pygame.mouse.get_pos() # Retrieves the current position of where the mouse is

        button_1 = pygame.Rect(50,100,200,50)
        button_2 = pygame.Rect(50,200,200,50)
        button_3 = pygame.Rect(50,300,200,50)
        button_4 = pygame.Rect(50,400,200,50)        

        if button_1.collidepoint((mx,my)): # Checks if mouse location overlaps button 1 location
            if mouse_click: # Checks if button has been clicked
                game()
        if button_2.collidepoint((mx, my)):
            if mouse_click:
                options()
        if button_3.collidepoint((mx, my)): 
            if mouse_click:
                import settings
        if button_4.collidepoint((mx, my)): 
            if mouse_click:
                quit_game()
        
        pygame.draw.rect(screen, WHITE, button_1) # Draws a rectangle onto the screen in white colour for button 1
        drawText("Play Game", font, BLACK, screen, (screen.get_width()/10), (screen.get_height()/6)) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
        
        pygame.draw.rect(screen, WHITE, button_2)
        drawText("Options", font, BLACK, screen, (screen.get_width()/10), (screen.get_height()*2/6))
        
        pygame.draw.rect(screen, WHITE, button_3)
        drawText("Settings", font, BLACK, screen, (screen.get_width()/10), (screen.get_height()*3/6))

        pygame.draw.rect(screen, WHITE, button_4)
        drawText("Quit", font, BLACK, screen, (screen.get_width()/10), (screen.get_height()*4/6))

        mouse_click = False

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
        screen.fill(WHITE)

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

    
    

