import pygame # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed


clock = pygame.time.Clock() # Creates a clock object that is used to track amount of time
from pygame.locals import * # Imports constants that are used by the Pygame module
pygame.init() # Initialises all imported Pygame modules 
pygame.display.set_caption("Carrom Game") # Sets program caption 
screen = pygame.display.set_mode((500,700),0,32) # Sets the display resolution

font = pygame.font.SysFont('Arial Bold', 40) # Sets the font used within the program

def drawText(text, font, color, surface, x, y): # Writes text onto the screen of the program
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

mouse_click = False # If a click has been made by the mouse

# ---------
# CONSTANTS
# --------- 
FPS = 60 # Sets the refresh rate, i.e. 60 times a second


# ------
# COLORS
# ------
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


class Player:
    def __init__(self, player_turn, taken_pieces, remaining_pieces):
        self.player_turn = player_turn
        self.taken_pieces = taken_pieces
        self.remaining_pieces = remaining_pieces

    def user_stats(self):
        remaining_pieces = 9
        if piece_taken == True:
            remaining_pieces -= 1


def mainMenu():     

    while True:
        
        screen.fill(BLACK) # Fills the screen in the desired colour
        drawText("Main Menu", font, WHITE, screen, 20, 20)

        mx, my = pygame.mouse.get_pos() # Retrieves the current position of where the mouse is

        button_1 = pygame.Rect(50,100,200,50)
        button_2 = pygame.Rect(50,200,200,50)
        button_3 = pygame.Rect(50,300,200,50)
        button_4 = pygame.Rect(50,400,200,50)
        button_5 = pygame.Rect(50,500,200,50)
        button_6 = pygame.Rect(50,600,200,50)

        if button_1.collidepoint((mx,my)): # Checks if mouse location overlaps button 1 location
            if mouse_click: # Checks if button has been clicked
                game()
        if button_2.collidepoint((mx, my)):
            if mouse_click:
                options()
        if button_3.collidepoint((mx, my)):
            if mouse_click:
                gameMode1()
        if button_4.collidepoint((mx, my)): 
            if mouse_click:
                gameMode2()
        if button_5.collidepoint((mx, my)): 
            if mouse_click:
                settings()
        if button_6.collidepoint((mx, my)): 
            if mouse_click:
                quit_game()
        
        pygame.draw.rect(screen, WHITE, button_1) # Draws a rectangle onto the screen in white colour for button 1
        drawText("Main Game", font, BLACK, screen, 70, 110) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
        
        pygame.draw.rect(screen, WHITE, button_2)
        drawText("Options", font, BLACK, screen, 90, 210)
        
        pygame.draw.rect(screen, WHITE, button_3)
        drawText("Game Mode 1", font, BLACK, screen, 60, 310)
        
        pygame.draw.rect(screen, WHITE, button_4)
        drawText("Game Mode 2", font, BLACK, screen, 60, 410)

        pygame.draw.rect(screen, WHITE, button_5)
        drawText("Settings", font, BLACK, screen, 90, 510)

        pygame.draw.rect(screen, WHITE, button_6)
        drawText("Quit", font, BLACK, screen, 120, 610)

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
        clock.tick(FPS) # 

def game():
    
    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Main Game', font, WHITE, screen, 20, 20)
        
        player1 = Player(False, 0, 20)
        player2 = Player(False, 0, 20)


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


def options():
    
    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Options', font, WHITE, screen, 20, 20)
        
        button_7 = pygame.Rect(20,60,300,50)
        pygame.draw.rect(screen, WHITE, button_7)
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


def gameMode1():
    
    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Game Mode 1', font, WHITE, screen, 20, 20)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False # Returns to main menu
        
        pygame.display.update()
        clock.tick(FPS)

def gameMode2():

    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Game Mode 2', font, WHITE, screen, 20, 20)
        
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

        drawText('Quit?', font, WHITE, screen, 20, 20)
        drawText('Press Q to confirm', font, WHITE, screen, 20, 60)
        drawText('Press ESC to return', font, WHITE, screen, 20, 100)
        
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


        



