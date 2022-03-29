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


def tutorial(screen):
    run = True

    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText("How to play..", font, WHITE, screen, x=WIDTH/4, y=HEIGHT/4)

        events = p.event.get()
        for event in events:
            if event.type == QUIT: # Checks if the cross (top right button) has been pressed
                p.quit() # Program ends
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True          


