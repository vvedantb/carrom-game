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


def draw_pieces():
    
    # Inner layer

    queen_piece = Piece( # Middle piece
        x=WIDTH/2, 
        y=HEIGHT/2, 
        size=15, 
        mass=1, 
        state="queen"
    )
    queen_piece.draw()

    brown_piece1 = Piece( # Top left piece
        x=(WIDTH/2)-30, 
        y=(HEIGHT/2)-15, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece1.draw()

    brown_piece2 = Piece( # Botton piece
        x=(WIDTH/2), 
        y=(HEIGHT/2)+30, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece2.draw()  

    brown_piece3 = Piece( # Top right piece
        x=(WIDTH/2)+30, 
        y=(HEIGHT/2)-15, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece3.draw()  

    # BROWN OUTER LAYER

    brown_piece4 = Piece( # Left piece
        x=(WIDTH/2)-60, 
        y=(HEIGHT/2), 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece4.draw()  


    brown_piece5 = Piece( # Right piece
        x=(WIDTH/2)+60, 
        y=(HEIGHT/2), 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece5.draw()  
    
    brown_piece6 = Piece( # Top left piece
        x=(WIDTH/2)-30, 
        y=(HEIGHT/2)-45, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece6.draw()   

    brown_piece7 = Piece( # Top right piece
        x=(WIDTH/2)+30, 
        y=(HEIGHT/2)-45, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece7.draw()   

    brown_piece8 = Piece( # Bottom left piece
        x=(WIDTH/2)-30, 
        y=(HEIGHT/2)+45, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece8.draw()    

    brown_piece9 = Piece( # Bottom right piece
        x=(WIDTH/2)+30, 
        y=(HEIGHT/2)+45, 
        size=15, 
        mass=1, 
        state="brown"
    )
    brown_piece9.draw()               

    # BLACK INNER LAYER

    black_piece1 = Piece( #Top piece
        x=(WIDTH/2), 
        y=(HEIGHT/2)-30, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece1.draw()   

    black_piece2 = Piece( #Bottom right piece
        x=(WIDTH/2)+30, 
        y=(HEIGHT/2)+15, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece2.draw()         

    black_piece3 = Piece( #Bottom left piece
        x=(WIDTH/2)-30, 
        y=(HEIGHT/2)+15, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece3.draw()  

    # BLACK OUTER LAYER 

    black_piece4 = Piece( # Top middle piece
        x=(WIDTH/2), 
        y=(HEIGHT/2)-60, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece4.draw()      

    black_piece5 = Piece( # Top left piece
        x=(WIDTH/2)-60, 
        y=(HEIGHT/2)-30, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece5.draw()    

    black_piece6 = Piece( # Top right piece
        x=(WIDTH/2)+60, 
        y=(HEIGHT/2)-30, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece6.draw()    

    black_piece7 = Piece( # Bottom left piece
        x=(WIDTH/2)-60, 
        y=(HEIGHT/2)+30, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece7.draw()       

    black_piece8 = Piece( # Bottom right piece
        x=(WIDTH/2)+60, 
        y=(HEIGHT/2)+30, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece8.draw()         

    black_piece9 = Piece( # Bottom middle piece
        x=(WIDTH/2), 
        y=(HEIGHT/2)+60, 
        size=15, 
        mass=1, 
        state="black"
    )
    black_piece9.draw()      


def draw_striker():
    striker = Piece(
        x=(WIDTH/2), 
        y=(8*HEIGHT/10), 
        size=20, 
        mass=1, 
        state="striker"
    )
    striker.draw()

def game(screen):    

    return_button = Button(
            color=BLACK,
            x=30,
            y=70,
            width=200,
            height=50,
            text_color=WHITE,
            text_size=30,
            outline=CRIMSON,                        
            text="Return"
        )    

    run = True
    while run:
        screen.fill(BROWN)
        mouse_click = False
        BOARD_WIDTH, BOARD_HEIGHT = 900, 900
        BG = p.transform.scale(p.image.load("Game Code/board.png"), ((int(screen.get_width()*0.5625)), screen.get_height())) # TODO: Change this line
        screen.blit(BG, (int(screen.get_width()/2 - (BOARD_WIDTH/2)), 0)) # Puts board in the middle

        drawText("Play Game", font, BLACK, screen, 20, 20) # Writes text onto the screen 

        return_button.draw(screen)

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
            # if event.type == KEYDOWN:
            #     if event.key == K_SPACE:
            #         striker_shot()


        if return_button.mouse_collide() and mouse_click == True:
            run = False        
        
        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()

        draw_pieces()
        draw_striker()

        p.display.update()
        clock.tick(FPS)