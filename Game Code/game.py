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




# Inner layer

queen_piece = Piece(x=WIDTH/2, y=HEIGHT/2, size=15, mass=1, state="queen")  # Middle piece

brown_piece1 = Piece(x=(WIDTH/2)-30, y=(HEIGHT/2)-15, size=15, mass=1, state="brown")  # Top left piece

brown_piece2 = Piece(x=(WIDTH/2), y=(HEIGHT/2)+30, size=15, mass=1, state="brown")  # Botton piece

brown_piece3 = Piece(x=(WIDTH/2)+30, y=(HEIGHT/2)-15, size=15, mass=1, state="brown")  # Top right piece

# BROWN OUTER LAYER

brown_piece4 = Piece(x=(WIDTH/2)-60, y=(HEIGHT/2), size=15, mass=1, state="brown") # Left piece

brown_piece5 = Piece(x=(WIDTH/2)+60, y=(HEIGHT/2), size=15, mass=1, state="brown") # Right piece
    
brown_piece6 = Piece(x=(WIDTH/2)-30, y=(HEIGHT/2)-45, size=15, mass=1, state="brown") # Top left piece  

brown_piece7 = Piece(x=(WIDTH/2)+30, y=(HEIGHT/2)-45, size=15, mass=1, state="brown") # Top right piece       

brown_piece8 = Piece(x=(WIDTH/2)-30, y=(HEIGHT/2)+45, size=15, mass=1, state="brown") # Bottom left piece

brown_piece9 = Piece(x=(WIDTH/2)+30, y=(HEIGHT/2)+45, size=15, mass=1, state="brown") # Bottom right piece

# BLACK INNER LAYER

black_piece1 = Piece(x=(WIDTH/2), y=(HEIGHT/2)-30, size=15, mass=1, state="black") #Top piece

black_piece2 = Piece(x=(WIDTH/2)+30, y=(HEIGHT/2)+15, size=15, mass=1, state="black") #Bottom right piece   

black_piece3 = Piece(x=(WIDTH/2)-30, y=(HEIGHT/2)+15, size=15, mass=1, state="black") #Bottom left piece

# BLACK OUTER LAYER 

black_piece4 = Piece(x=(WIDTH/2), y=(HEIGHT/2)-60, size=15, mass=1, state="black") # Top middle piece

black_piece5 = Piece(x=(WIDTH/2)-60, y=(HEIGHT/2)-30, size=15, mass=1, state="black") # Top left piece

black_piece6 = Piece(x=(WIDTH/2)+60, y=(HEIGHT/2)-30, size=15, mass=1, state="black")   # Top right piece

black_piece7 = Piece(x=(WIDTH/2)-60, y=(HEIGHT/2)+30, size=15, mass=1, state="black") # Bottom left piece

black_piece8 = Piece(x=(WIDTH/2)+60, y=(HEIGHT/2)+30, size=15, mass=1, state="black")  # Bottom right piece

black_piece9 = Piece(x=(WIDTH/2), y=(HEIGHT/2)+60, size=15, mass=1, state="black") # Bottom middle piece

striker = Piece(x=(WIDTH/2), y=(8*HEIGHT/10), size=20, mass=1, state="striker")


pieces = []

pieces.append(queen_piece)

pieces.append(brown_piece1)
pieces.append(brown_piece2)
pieces.append(brown_piece3)
pieces.append(brown_piece4)
pieces.append(brown_piece5)
pieces.append(brown_piece6)
pieces.append(brown_piece7)
pieces.append(brown_piece8)
pieces.append(brown_piece9)


pieces.append(black_piece1)
pieces.append(black_piece2)
pieces.append(black_piece3)
pieces.append(black_piece4)
pieces.append(black_piece5)
pieces.append(black_piece6)
pieces.append(black_piece7)
pieces.append(black_piece8)
pieces.append(black_piece9)



def game(screen):    

    return_button = Button(color=BLACK, x=30, y=70, width=200, height=50, text_color=WHITE, text_size=30, outline=CRIMSON, text="Return")    

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

                mX, mY = p.mouse.get_pos()
                if event.key == K_e: # Moves striker right
                    
                    if mX > 600:
                        striker.x = 560
                    else:
                        striker.x += 5
                if event.key == K_q: # Moves striker left
                    if mX < 500:
                        striker.x = 600
                    else:
                        striker.x -= 5

                if event.key == K_w: # Increases striking power
                    if striker.power >= 0:
                        striker.power += 10
                if event.key == K_s: # Decreases striking power
                    if striker.power >= 10:
                        striker.power -= 10
                

                if event.key == K_q: 
                    print("angle - 10")
                if event.key == K_e:
                    print("angle + 10")


            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True                    
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    striker.shot()


        if return_button.mouse_collide() and mouse_click == True:
            run = False        
        
        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()

        queen_piece.draw()
        
        brown_piece1.draw()
        brown_piece2.draw()
        brown_piece3.draw()  
        brown_piece4.draw()  
        brown_piece5.draw()
        brown_piece6.draw()
        brown_piece7.draw()
        brown_piece8.draw()    
        brown_piece9.draw()    
        
        black_piece1.draw()   
        black_piece2.draw()
        black_piece3.draw()  
        black_piece4.draw()  
        black_piece5.draw() 
        black_piece6.draw() 
        black_piece7.draw()  
        black_piece8.draw()  
        black_piece9.draw()  
        
        striker.draw()

        p.display.update()
        clock.tick(FPS)