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

    play_music_button = Button(
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


    while True:
        screen.fill(BROWN)
        mouse_click = False
        
        drawText("Main Menu", font, WHITE, screen, 20, 20)

        game_button.draw(screen)
        options_button.draw(screen)
        settings_button.draw(screen)
        quit_button.draw(screen)
        play_music_button.draw(screen)

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

                if play_music_button.mouse_collide():
                    play_music_button.color = RED
                else:
                    play_music_button.color = WHITE

                



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

def game():    
    run = True
    while run:
        screen.fill(BROWN)
        BOARD_WIDTH, BOARD_HEIGHT = 900, 900
        BG = p.transform.scale(p.image.load("Game Code/board.png"), ((int(screen.get_width()*0.5625)), screen.get_height())) # TODO: Change this line
        screen.blit(BG, (int(screen.get_width()/2 - (BOARD_WIDTH/2)), 0)) # Puts board in the middle

        drawText("Play Game", font, BLACK, screen, 20, 20) # Writes text onto the screen 


        events = p.event.get()
        for event in events:
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            # if event.type == KEYDOWN:
            #     if event.key == K_SPACE:
            #         striker_shot()

        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()

        draw_pieces()
        draw_striker()

        p.display.update()
        clock.tick(FPS)




def play_music():
    run = True

    return_button = Button(
            color=BLACK,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
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
            x=30,
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
            mainMenu(screen)

        if resolution_button.mouse_collide() and mouse_click == True:
            resolution_settings(screen)
            break

        p.display.update()
        clock.tick(FPS)





def settings():

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

    x_sensitivity_button = Button(
            color=WHITE,
            x=30,
            y=170,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,                        
            text="X-Sensitivity"
        )  

    y_sensitivity_button = Button(
            color=WHITE,
            x=30,
            y=370,
            width=500,
            height=50,
            text_color=BLACK,
            text_size=30,
            outline=CRIMSON,                        
            text="Y-Sensitivity"
        )              
    
    while run:
        screen.fill(BROWN)
        mouse_click = False

        drawText('Settings', font, WHITE, screen, 20, 20)

        return_button.draw(screen)
        x_sensitivity_button.draw(screen)
        y_sensitivity_button.draw(screen)



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
            mainMenu(screen)        
        
        p.display.update()
        clock.tick(FPS)






def quit_game():
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


mainMenu(screen)


        





    
    

