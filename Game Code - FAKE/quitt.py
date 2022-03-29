import pygame as p # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed
import math # For collision function

from pygame.locals import * # Imports constants that are used by the Pygame module
#from striker import Striker

from piece import Piece
from button import Button

from draw_text import drawText

clock = p.time.Clock() # Creates a clock object that is used to track amount of time
p.init() # Initialises all imported Pygame modules 

p.display.set_caption("Carrom Game") # Sets program caption 
icon = p.image.load("Game Code/icon.png") # Loads the icon image
p.display.set_icon(icon) # Sets the icon image


# p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1

# COLOURS
YELLOW = (240,230,140)
BROWN = (138, 87, 0)
BLACK = (0,0,0)
CRIMSON = (220,20,60)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREY = (125, 125, 125)
LIGHT_BROWN = (191, 134, 0)


FPS = 60 # Sets the refresh rate
mouse_click = False # If a click has been made 

Board = p.image.load("Game Code/board.png")

WIDTH, HEIGHT = 1600, 900
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
screen.fill(BROWN)


p.font.init()
font = p.font.SysFont('Arial Bold', 40) # Sets the font used within the program

BLACK_PIECE = p.image.load("Game Code/Assets/black-piece.png")
#BROWN_PIECE = 



def quit_game(screen):
    run = True

    return_button = Button(
            color=BLACK,
            x=30,
            y=70,
            width=500,
            height=50,
            text_color=WHITE,
            text_size=30,
            outline=CRIMSON,                        
            text="Return to main menu"
        )

    confirm_quit_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,                        
            text="Click to quit"
        )        

    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText('Are you sure you would like to quit?', font, WHITE, screen, 20, 220)
      
        return_button.draw(screen)
        confirm_quit_button.draw(screen)

        
        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        if return_button.mouse_collide() and mouse_click == True:
            run = False

        if confirm_quit_button.mouse_collide() and mouse_click == True:
            run = False
            p.quit()

        p.display.update()
        clock.tick(FPS)
