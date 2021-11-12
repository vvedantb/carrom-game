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


# p.mixer.music.load("Game Code/music.wav") # Loads the music file
# p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1
# p.mixer.music.set_volume(0.25) # Sets the music volume

WIDTH, HEIGHT = 1600, 900

BROWN = (138, 87, 0)
BLACK = (0,0,0)
CRIMSON = (220,20,60)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
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


def draw_board():
    pass



def mainMenu():
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
            if event.type == KEYDOWN: # Checks if a key has been pressed
                if event.key == K_ESCAPE: # Checks if escape key has been pressed
                    p.quit() # Programs ends
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True

        if game_button.mouse_collide() and mouse_click == True:
            game()

        if options_button.mouse_collide() and mouse_click == True:
            options()

        if quit_button.mouse_collide() and mouse_click == True:
            quit_game()

        if play_music_button.mouse_collide() and mouse_click == True:
            play_music()

        p.display.flip() # Updates display
        clock.tick(FPS) 



# def mainMenu():     
#     while True:
#         screen.fill(BROWN)
#         mouse_click = False # If a click has been made by the mouse

#         drawText("Main Menu", font, WHITE, screen, 20, 20)

#         button_height = screen.get_height()/20
#         button_width = screen.get_width()/10

#         game_button = p.Rect(button_width-20, (WIDTH/10)+5, button_width, button_height)
#         options_button = p.Rect(button_width-20, (2*WIDTH/10)+5, button_width, button_height)
#         settings_button = p.Rect(button_width-20, (3*WIDTH/10)+5, button_width, button_height)
#         quit_button = p.Rect(button_width-20, (4*WIDTH/10)+5, button_width/2, button_height)
#         music_button = p.Rect(button_width-20, (5*WIDTH/10)+5, button_width, button_height)

      
#         p.draw.rect(screen, BLACK, game_button) # Draws a rectangle onto the screen in white colour for button 1
#         p.draw.rect(screen, BLACK, options_button)
#         p.draw.rect(screen, BLACK, settings_button)
#         p.draw.rect(screen, BLACK, quit_button)
#         p.draw.rect(screen, BLACK, music_button)

#         text_width = screen.get_width()/10
#         text_height = screen.get_height()/6

#         drawText("Play Game", font, WHITE, screen, text_height, 1.1*text_width) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
#         drawText("Options", font, WHITE, screen, text_height, 2.1*text_width)
#         drawText("Settings", font, WHITE, screen, text_height, 3.1*text_width)
#         drawText("Quit", font, WHITE, screen, text_height, 4.1*text_width)
#         drawText("Music", font, WHITE, screen, text_height, 5.1*text_width)

#         events = p.event.get()
#         for event in events:
#             if event.type == QUIT: # Checks if the cross (top right button) has been pressed
#                 p.quit() # Program ends
#                 sys.exit()
#             if event.type == KEYDOWN: # Checks if a key has been pressed
#                 if event.key == K_ESCAPE: # Checks if escape key has been pressed
#                     p.quit() # Programs ends
#                     sys.exit()
#             if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
#                 if event.button == 1: # Checks if button has been clicked
#                     mouse_click = True

#         mx, my = p.mouse.get_pos() # Retrieves the current position of where the mouse is

#         if game_button.collidepoint((mx, my)): # Checks if mouse location overlaps button 1 location
#             if mouse_click: # Checks if button has been clicked
#                 game()
#         if options_button.collidepoint((mx, my)):
#             if mouse_click:
#                 options()
#         if settings_button.collidepoint((mx, my)): 
#             if mouse_click:
#                 settings()
#         if quit_button.collidepoint((mx, my)): 
#             if mouse_click:
#                 quit_game()
#         if music_button.collidepoint((mx, my)):
#             if mouse_click:
#                 play_music(button_width, button_height, text_height, text_width)

#         p.display.flip() # Updates display
#         clock.tick(FPS) 


def draw_pieces():
    board_pieces = []
    
    pieces_height = 1 # in cm
    pieces_radius = 2 # in cm

    pieces_size = int((math.pi)*(pieces_radius^2))  # Height x Radius x Pi^2
    pieces_mass = 5 # in grams
    #piece = Piece(DARK_GREY, WIDTH/6, HEIGHT/2, pieces_size, pieces_mass)


    
    piece_1 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_1)
    
    piece_2 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_2)
    
    piece_3 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_3)
    
    piece_4 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_4)
    
    piece_5 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_5)
    
    piece_6 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_6)
    
    piece_7 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_7)
    
    piece_8 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_8)
    
    piece_9 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_9)
    
    piece_10 = Piece(DARK_GREY, WIDTH/10, HEIGHT/10, pieces_size, pieces_mass)
    board_pieces.append(piece_10)

    print(board_pieces)





def game():    
    run = True
    while run:
        screen.fill(BROWN)
        BOARD_WIDTH, BOARD_HEIGHT = 900, 900
        BG = p.transform.rotate(p.transform.scale(p.image.load(os.path.join('Game Code\Assets', 'carrom-board.jpg')), ((int(screen.get_width()*0.5625)), screen.get_height())), 89.5) # TODO: Change this line
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

        draw_pieces()


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
        screen.fill(BROWN)
        mouse_click = False

        return_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="Click to return to main menu"
        )
        return_button.draw(screen, BLACK, 30, CRIMSON)

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


# def play_music(button_width, button_height, text_height, text_width):
#     run = True
#     while run:
#         drawText('Press "ESC" to exit music', font, BLACK, screen, 500, 400)
#         drawText('Press "Y" to start music', font, BLACK, screen, 500, 500)
#         drawText('Press "N" to stop music', font, BLACK, screen, 500, 600)
#         drawText('Press "P" to pause music', font, BLACK, screen, 500, 700)
#         drawText('Press "O" to resume music', font, BLACK, screen, 500, 800)

#         music_button = p.Rect(button_width-20, (5*WIDTH/10)+5, button_width+50, button_height)
        
#         events = p.event.get()
#         for event in events:
#             if event.type == QUIT:
#                 p.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     run = False
#                 if event.key == K_y:
#                     p.mixer.music.load("Game Code/music.wav") # Loads the music file
#                     p.mixer.music.play(-1) # Plays the music, and sets it to loop through the argument -1
#                     p.mixer.music.set_volume(0.25) # Sets the music volume
                    
#                     p.draw.rect(screen, GREEN, music_button)
#                     drawText("Playing Music", font, WHITE, screen, text_height, 5.1*text_width)
#                 if event.key == K_n:
#                     p.mixer.music.stop()
#                     p.draw.rect(screen, RED, music_button)
#                     drawText("Stopped", font, WHITE, screen, text_height, 5.1*text_width)
#                 if event.key == K_p:
#                     p.mixer.music.pause()
#                     p.draw.rect(screen, BLUE, music_button)
#                     drawText("Paused", font, WHITE, screen, text_height, 5.1*text_width)
#                 if event.key == K_o:
#                     p.mixer.music.unpause()
#                     p.draw.rect(screen, GREEN, music_button)
#                     drawText("Playing Music", font, WHITE, screen, text_height, 5.1*text_width)

#         p.display.update()
#         clock.tick(FPS)    


def options():
    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False
        drawText('Options', font, WHITE, screen, 20, 20)
        
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
            WHITE,
            30,
            370,
            500, 
            50,
            "Select Pieces Colour"
        )

        test2_button.draw(screen, BLACK, 30, CRIMSON)

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

        if test_button.mouse_collide() and mouse_click == True:
            print("It works!")
            # TODO: Put striker colour as whatever specificed
    
        if test2_button.mouse_collide() and mouse_click == True:
            print("This also works!")
            # TODO: Put pieces colour as whatever specified

        p.display.update()
        clock.tick(FPS)


def settings():

    run = True
    
    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText('Settings', font, WHITE, screen, 20, 20)

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
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True
        
        if x_sensitivity_button.mouse_collide() and mouse_click == True:
            print("Omg! It works!")
            # TODO: Change x-sensitivity

        if y_sensitivity_button.mouse_collide() and mouse_click == True:
            print("Omgggg! It works!")
            # TODO: Change x-sensitivity

        p.display.update()
        clock.tick(FPS)



def quit_game():
    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText('Are you sure you would like to quit?', font, WHITE, screen, 20, 220)

        confirm_quit_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text="Click to quit"
        )
        confirm_quit_button.draw(screen, BLACK, 30, CRIMSON)

        return_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text="Click to return to main menu"
        )
        return_button.draw(screen, BLACK, 30, CRIMSON)

        
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

        if confirm_quit_button.mouse_collide() and mouse_click == True:
            run = False
            p.quit()
        
        if return_button.mouse_collide() and mouse_click == True:
            run = False

        p.display.update()
        clock.tick(FPS)


mainMenu()


        





    
    

