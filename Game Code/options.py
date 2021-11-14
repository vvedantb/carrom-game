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


def resolution_settings(screen):
    run = True

    res1_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="1280x720"
        )

    res2_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="1600x900"
        )        

    res3_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="1920x1080"
        )    

    res4_button = Button(
            color=WHITE,
            x=30,
            y=770,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Apply Fullscreen"
        )       

    back_button = Button(
            color=BLACK,
            x=100,
            y=970,
            width=500,
            height=50,
            text_color=WHITE,
            text_size=30,
            outline=CRIMSON,             
            text="Back"
        )             

    while run:
        screen.fill(BROWN)
        mouse_click = False


        res1_button.draw(screen)
        res2_button.draw(screen)
        res3_button.draw(screen)
        res4_button.draw(screen)
        back_button.draw(screen)

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
        
        # if res1_button.mouse_collide() and mouse_click == True:
        #     WIDTH, HEIGHT = 1280, 720             
        #     screen = p.display.set_mode((WIDTH, HEIGHT))

        # if res2_button.mouse_collide() and mouse_click == True:
        #     WIDTH, HEIGHT = 1600, 900
        #     screen = p.display.set_mode((WIDTH, HEIGHT))

        # if res3_button.mouse_collide() and mouse_click == True:
        #     WIDTH, HEIGHT = 1920, 1080
        #     screen = p.display.set_mode((WIDTH, HEIGHT))

        # if res4_button.mouse_collide() and mouse_click == True:
        #     pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # if back_button.mouse_collide() and mouse_click == True:
        #     run = False





def options(screen):
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

    test_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Select Striker Colour"
        )        

    test2_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500, 
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Select Pieces Colour"
        )

    resolution_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500, 
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Change resolution"
        )        

    while run:
        screen.fill(BROWN)
        mouse_click = False
        drawText('Options', font, WHITE, screen, 20, 20)
        

        return_button.draw(screen)
        test_button.draw(screen)
        test2_button.draw(screen)
        resolution_button.draw(screen)


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


        if test_button.mouse_collide() and mouse_click == True:
            print("It works!")
            # TODO: Put striker colour as whatever specificed
    
        if test2_button.mouse_collide() and mouse_click == True:
            print("This also works!")
            # TODO: Put pieces colour as whatever specified

        if return_button.mouse_collide() and mouse_click == True:
            run = False

        if resolution_button.mouse_collide() and mouse_click == True:
            resolution_settings(screen)
            break

        p.display.update()
        clock.tick(FPS)



