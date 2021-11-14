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

from music import play_music
from options import options
from quitt import quit_game
from settings import settings
from game import game
from tutorial import tutorial
from instructions import instructions

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







def mainMenu(screen):

    game_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color = BLACK,
            text_size = 30,
            outline=CRIMSON,
            text="Play Game"
        )

    options_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,
            text="Options"
        )        


    settings_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,
            text="Settings"
        )     

    quit_button = Button(
            color=WHITE,
            x=630,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,
            text="Quit Game"
        )

    music_button = Button(
            color=WHITE,
            x=630,
            y=370,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,            
            text="Play music"
        )       

    tutorial_button = Button(
            color=WHITE,
            x=630,
            y=570,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,            
            text="How to play"        
    )    

    instructions_button = Button(
            color=WHITE,
            x=630,
            y=770,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,            
            text="Instructions"        
    )    


    while True:
        screen.fill(BROWN)
        mouse_click = False
        
        drawText("Main Menu", font, WHITE, screen, 20, 20)

        game_button.draw(screen)
        options_button.draw(screen)
        settings_button.draw(screen)
        quit_button.draw(screen)
        music_button.draw(screen)
        tutorial_button.draw(screen)
        instructions_button.draw(screen)

        events = p.event.get()
        for event in events:
            if event.type == QUIT: # Checks if the cross (top right button) has been pressed
                p.quit() # Program ends
                sys.exit()
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True    
            if event.type == MOUSEMOTION:
                if game_button.mouse_collide():
                    game_button.color = RED
                else:
                    game_button.color = WHITE
                
                if options_button.mouse_collide():
                    options_button.color = RED
                else:
                    options_button.color = WHITE

                if settings_button.mouse_collide():
                    settings_button.color = RED
                else:
                    settings_button.color = WHITE  

                if quit_button.mouse_collide():
                    quit_button.color = RED
                else:
                    quit_button.color = WHITE                                      
                if music_button.mouse_collide():
                    music_button.color = RED
                else:
                    music_button.color = WHITE

                if tutorial_button.mouse_collide():
                    tutorial_button.color = RED
                else:
                    tutorial_button.color = WHITE

                if instructions_button.mouse_collide():
                    instructions_button.color = RED
                else:
                    instructions_button.color = WHITE

                



        if game_button.mouse_collide() and mouse_click == True:
            game(screen)            

        if options_button.mouse_collide() and mouse_click == True:
            options(screen)

        if settings_button.mouse_collide() and mouse_click == True:
            settings(screen)

        if quit_button.mouse_collide() and mouse_click == True:
            quit_game(screen)

        if music_button.mouse_collide() and mouse_click == True:
            play_music(screen)

        if tutorial_button.mouse_collide() and mouse_click == True:
            tutorial(screen)

        if instructions_button.mouse_collide() and mouse_click == True:
            instructions(screen)            
        

        p.display.flip() # Updates display
        clock.tick(FPS) 






mainMenu(screen)


        





    
    

