import pygame as p # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed
import math # For collision function
from pygame.locals import * # Imports constants that are used by the Pygame module
from piece import Piece
from button import Button
import math
clock = p.time.Clock() # Creates a clock object that is used to track amount of time
FPS = 60 # Sets the refresh rate
mouse_click = False # If a click has been made


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


def play_music(screen):
    run = True

    return_button = Button(
            color=BLACK,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color=WHITE,
            text_size=30,
            outline=CRIMSON,             
            text="Return to main menu"
        )

    start_music_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Play music"
        )       

    stop_music_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Stop music"
        )         

    pause_music_button = Button(
            color=WHITE,
            x=630,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Pause music"
        )

    resume_music_button = Button(
            color=WHITE,
            x=630,
            y=370,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,             
            text="Resume music"
        )        


    while run:
        screen.fill(BROWN)
        mouse_click = False


        return_button.draw(screen)
        start_music_button.draw(screen)
        stop_music_button.draw(screen)
        pause_music_button.draw(screen)
        resume_music_button.draw(screen)


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


        if return_button.mouse_collide() and mouse_click == True:
            run = False

        if start_music_button.mouse_collide() and mouse_click == True:
            p.mixer.music.load("Game Code/music.wav") # Loads the music file
            p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1
            p.mixer.music.set_volume(0.25) # Sets the music volume

        if stop_music_button.mouse_collide() and mouse_click == True:
            p.mixer.music.stop()

        if pause_music_button.mouse_collide() and mouse_click == True:
            p.mixer.music.pause()

        if resume_music_button.mouse_collide() and mouse_click == True:
            p.mixer.music.unpause()

        p.display.update()
        clock.tick(FPS)
