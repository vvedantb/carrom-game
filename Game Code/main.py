import pygame as p # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed
import math # For collision function
from pygame.locals import * # Imports constants that are used by the Pygame module
from striker import Striker
from piece import Piece
from button import Button
import math

#from start_menu import *

clock = p.time.Clock() # Creates a clock object that is used to track amount of time
p.init() # Initialises all imported Pygame modules 

p.display.set_caption("Carrom Game") # Sets program caption 
icon = p.image.load("Game Code/icon.png") # Loads the icon image
p.display.set_icon(icon) # Sets the icon image


# p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1


BROWN = (138, 87, 0)
BLACK = (0,0,0)
CRIMSON = (220,20,60)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREY = (125, 125, 125)
LIGHT_BROWN = (191, 134, 0)

Board = p.image.load("Game Code/board.png")

WIDTH, HEIGHT = 1600, 900
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE) # Sets the display resolution
screen.fill(BROWN)


p.font.init()
font = p.font.SysFont('Arial Bold', 40) # Sets the font used within the program

BLACK_PIECE = p.image.load("Game Code/Assets/black-piece.png")
#BROWN_PIECE = 
PLAYER_STRIKER = p.draw.circle(screen, BLUE, (0,0), 2)
ENEMY_STRIKER = p.draw.circle(screen, RED, (0,0), 2)

FPS = 60 # Sets the refresh rate, i.e. 60 times a second

mouse_click = False # If a click has been made by the mouse




def event_manager():
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


def drawText(text, font, color, surface, x, y): # Writes text onto the screen of the program
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


def draw_board():
    pass



def mainMenu(screen):
    while True:
        screen.fill(BROWN)
        mouse_click = False
        
        drawText("Main Menu", font, WHITE, screen, 20, 20)

        game_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="Play Game"
        )
        game_button.draw(screen, BLACK, 30, CRIMSON)


        options_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text="Options"
        )
        options_button.draw(screen, BLACK, 30, CRIMSON)

        settings_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500,
            height=50,
            text="Settings"
        )
        settings_button.draw(screen, BLACK, 30, CRIMSON)

        quit_button = Button(
            color=WHITE,
            x=630,
            y=170,
            width=500,
            height=50,
            text="Quit Game"
        )
        quit_button.draw(screen, BLACK, 30, CRIMSON)

        play_music_button = Button(
            color=WHITE,
            x=630,
            y=370,
            width=500,
            height=50,
            text="Play music"
        )
        play_music_button.draw(screen, BLACK, 30, CRIMSON)

        events = p.event.get()
        for event in events:
            if event.type == QUIT: # Checks if the cross (top right button) has been pressed
                p.quit() # Program ends
                sys.exit()
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True    


        if game_button.mouse_collide() and mouse_click == True:
            game()

        if options_button.mouse_collide() and mouse_click == True:
            options(screen)

        if settings_button.mouse_collide() and mouse_click == True:
            settings()

        if quit_button.mouse_collide() and mouse_click == True:
            quit_game()

        if play_music_button.mouse_collide() and mouse_click == True:
            play_music()

        p.display.flip() # Updates display
        clock.tick(FPS) 


# def draw_pieces():
#     board_pieces = []
    
#     pieces_height = 1 # in cm
#     pieces_radius = 2 # in cm

#     pieces_size = int((math.pi)*(pieces_radius^2))  # Height x Radius x Pi^2
#     pieces_mass = 5 # in grams
#     #piece = Piece(DARK_GREY, WIDTH/6, HEIGHT/2, pieces_size, pieces_mass)

#     piece_1 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_1)
    
#     piece_2 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_2)
    
#     piece_3 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_3)
    
#     piece_4 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_4)
    
#     piece_5 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_5)
    
#     piece_6 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_6)
    
#     piece_7 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_7)
    
#     piece_8 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_8)
    
#     piece_9 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_9)
    
#     piece_10 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
#     board_pieces.append(piece_10)

#     print(board_pieces)



def draw_pieces():
    piece1 = Piece(DARK_GREY, ( WIDTH/2 ), ( HEIGHT/2 ), )
    piece2 = Piece()



def game():    
    run = True
    while run:
        screen.fill(BROWN)
        BOARD_WIDTH, BOARD_HEIGHT = 900, 900
        BG = p.transform.scale(p.image.load("Game Code/board.png"), ((int(screen.get_width()*0.5625)), screen.get_height())) # TODO: Change this line
        screen.blit(BG, (int(screen.get_width()/2 - (BOARD_WIDTH/2)), 0)) # Puts board in the middle

        drawText("Play Game", font, BLACK, screen, 20, 20) # Writes text onto the screen 

        # player_striker = Striker.draw_circle(screen, RED, (BOARD_WIDTH/2, BOARD_HEIGHT/2), 15)
        # enemy_striker = Striker.draw_circle(screen, BLUE, (BOARD_WIDTH/2 + 15, BOARD_HEIGHT/2), 15)

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

        # draw_pieces()


        # p.draw.circle(screen, RED, (2*WIDTH/6, 2*HEIGHT/8), 15) 
        # p.draw.circle(screen, RED, (2*WIDTH/6, 6*HEIGHT/8), 15) 

        # p.draw.circle(screen, RED, (4*WIDTH/6, 2*HEIGHT/8), 15) 
        # p.draw.circle(screen, RED, (4*WIDTH/6, 6*HEIGHT/8), 15)

        # p.draw.circle(screen, RED, (4*WIDTH/6 - 30, 6*HEIGHT/8 + 50), 15) 
        # p.draw.circle(screen, RED, (2*WIDTH/6 + 30, 6*HEIGHT/8 + 50), 15) 

        # p.draw.circle(screen, RED, (4*WIDTH/6 - 30, 2*HEIGHT/8 - 50), 15) 
        # p.draw.circle(screen, RED, (2*WIDTH/6 + 30, 2*HEIGHT/8 - 50), 15) # Striker boundaries

        # p.draw.circle(screen, RED, (WIDTH/2, HEIGHT/2), 20) # Center circle

        # p.draw.circle(screen, DARK_GREY, (WIDTH/4 + 30, HEIGHT/8 - 30), 30) # Top left
        # p.draw.circle(screen, DARK_GREY, (WIDTH/4 + 30, 7*HEIGHT/8 + 30), 30) # Bottom left
        # p.draw.circle(screen, DARK_GREY, (3*WIDTH/4 - 30, HEIGHT/8 - 30), 30) # Top right
        # p.draw.circle(screen, DARK_GREY, (3*WIDTH/4 - 30, 7*HEIGHT/8 + 30), 30) # Bottom right corner holes

        for i in range(20):
            p.draw.circle(screen, DARK_GREY, (i* WIDTH/100, HEIGHT/2), 10)
                    
        for i in range(4):
            p.draw.rect(screen, (0,0,0), ((WIDTH/4)+i,(HEIGHT)+i,155,155), 2)

        p.display.update()
        clock.tick(FPS)


def play_music():
    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False

        return_button = Button(
            color=BLACK,
            x=30,
            y=170,
            width=500,
            height=50,
            text="Return to main menu"
        )
        return_button.draw(screen, WHITE, 30, CRIMSON)

        start_music_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text="Play music"
        )
        start_music_button.draw(screen, BLACK, 30, CRIMSON)

        stop_music_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500,
            height=50,
            text="Stop music"
        )
        stop_music_button.draw(screen, BLACK, 30, CRIMSON)

        pause_music_button = Button(
            color=WHITE,
            x=630,
            y=170,
            width=500,
            height=50,
            text="Pause music"
        )
        pause_music_button.draw(screen, BLACK, 30, CRIMSON)


        resume_music_button = Button(
            color=WHITE,
            x=630,
            y=370,
            width=500,
            height=50,
            text="Resume music"
        )
        resume_music_button.draw(screen, BLACK, 30, CRIMSON)

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




def resolution_settings(screen):
    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False

        res1_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="1280x720"
        )
        res1_button.draw(screen, WHITE, 30, CRIMSON)

        res2_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text="1600x900"
        )
        res2_button.draw(screen, WHITE, 30, CRIMSON)     

        res3_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500,
            height=50,
            text="1920x1080"
        )
        res3_button.draw(screen, WHITE, 30, CRIMSON)  

        res4_button = Button(
            color=WHITE,
            x=30,
            y=770,
            width=500,
            height=50,
            text="Apply Fullscreen"
        )
        res4_button.draw(screen, WHITE, 30, CRIMSON)                           

        back_button = Button(
            color=BLACK,
            x=30,
            y=970,
            width=500,
            height=50,
            text="Back"
        )
        back_button.draw(screen, WHITE, 30, CRIMSON)   

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
        
        if res1_button.mouse_collide() and mouse_click == True:
            WIDTH, HEIGHT = 1280, 720             
            screen = p.display.set_mode((WIDTH, HEIGHT))

        if res2_button.mouse_collide() and mouse_click == True:
            WIDTH, HEIGHT = 1600, 900
            screen = p.display.set_mode((WIDTH, HEIGHT))

        if res3_button.mouse_collide() and mouse_click == True:
            WIDTH, HEIGHT = 1920, 1080
            screen = p.display.set_mode((WIDTH, HEIGHT))

        if res4_button.mouse_collide() and mouse_click == True:
            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        if back_button.mouse_collide() and mouse_click == True:
            run = False





def options(screen):
    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False
        drawText('Options', font, WHITE, screen, 20, 20)
        
        return_button = Button(
            color=BLACK,
            x=30,
            y=70,
            width=500,
            height=50,
            text="Return to main menu"
        )
        return_button.draw(screen, WHITE, 30, CRIMSON)

        test_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="Select Striker Colour"
        )
        test_button.draw(screen, BLACK, 30, CRIMSON)

        test2_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500, 
            height=50,
            text="Select Pieces Colour"
        )
        test2_button.draw(screen, BLACK, 30, CRIMSON)

        resolution_button = Button(
            color=WHITE,
            x=30,
            y=570,
            width=500, 
            height=50,
            text="Change resolution"
        )
        resolution_button.draw(screen, BLACK, 30, CRIMSON)

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
            mainMenu(screen)

        if resolution_button.mouse_collide() and mouse_click == True:
            resolution_settings(screen)
            break

        p.display.update()
        clock.tick(FPS)





def settings():

    run = True
    
    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText('Settings', font, WHITE, screen, 20, 20)

        return_button = Button(
            color=BLACK,
            x=30,
            y=70,
            width=500,
            height=50,
            text="Return to main menu"
        )

        return_button.draw(screen, WHITE, 30, CRIMSON)

        x_sensitivity_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="X-Sensitivity"
        )
        x_sensitivity_button.draw(screen, text_color=BLACK, text_size=30, outline=CRIMSON)
      
        y_sensitivity_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text="Y-Sensitivity"
        )
        y_sensitivity_button.draw(screen, text_color=BLACK, text_size=30, outline=CRIMSON)

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

        
        if x_sensitivity_button.mouse_collide() and mouse_click == True:
            print("Omg! It works!")
            # TODO: Change x-sensitivity

        if y_sensitivity_button.mouse_collide() and mouse_click == True:
            print("Omgggg! It works!")
            # TODO: Change x-sensitivity

        if return_button.mouse_collide() and mouse_click == True:
            mainMenu()        
        
        p.display.update()
        clock.tick(FPS)






def quit_game():
    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText('Are you sure you would like to quit?', font, WHITE, screen, 20, 220)
      

        return_button = Button(
            color=BLACK,
            x=30,
            y=70,
            width=500,
            height=50,
            text="Return to main menu"
        )
        return_button.draw(screen, WHITE, 30, CRIMSON)

        confirm_quit_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="Click to quit"
        )
        confirm_quit_button.draw(screen, BLACK, 30, CRIMSON)



        
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


mainMenu(screen)


        





    
    

