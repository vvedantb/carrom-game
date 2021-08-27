import pygame # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Used to randomise events 
import sys #        
import pyautogui # Custom cursor speed
clock <- pygame.time.Clock() # Creates a clock object that is used to track amount of time
from pygame.locals import * # Imports constants that are used by the Pygame module
pygame.init() # Initialises all imported Pygame modules 
pygame.display.set_caption("Carrom Game") # Sets program caption 
screen <- pygame.display.set_mode((500,700),0,32) # Sets the display resolution
font <- pygame.font.SysFont('Arial Bold', 40) # Sets the font used within the program
FUNCTION draw_text(text, font, color, surface, x, y): # Writes text onto the screen of the program
    textobj <- font.render(text, 1, color)
    textrect <- textobj.get_rect()
    textrect.topleft <- (x,y)
    surface.blit(textobj, textrect)
ENDFUNCTION

click <- False # If a click has been made by the mouse
# ---------
# CONSTANTS
# --------- 
FPS <- 60 # Sets the refresh rate, i.e. 60 times a second
# ------
# COLORS
# ------
BLACK <- (0,0,0)
WHITE <- (255,255,255)
RED <- (255,0,0)
CLASS Player:
    FUNCTION __init__(self, player_turn, taken_pieces, remaining_pieces):
         player_turn <- player_turn
         taken_pieces <- taken_pieces
         remaining_pieces <- remaining_pieces
    ENDFUNCTION

    FUNCTION user_stats(self):
        remaining_pieces <- 9
        IF piece_taken = True:
            remaining_pieces -= 1
        ENDIF
    ENDFUNCTION

ENDCLASS

FUNCTION main_menu(): 
    while True:
        screen.fill(BLACK) # Fills the screen in the desired colour
        draw_text("Main Menu", font, WHITE, screen, 20, 20)
        mx, my <- pygame.mouse.get_pos() # Retrieves the current position of where the mouse is
        button_1 <- pygame.Rect(50,100,200,50)
        button_2 <- pygame.Rect(50,200,200,50)
        button_3 <- pygame.Rect(50,300,200,50)
        button_4 <- pygame.Rect(50,400,200,50)
        button_5 <- pygame.Rect(50,500,200,50)
        button_6 <- pygame.Rect(50,600,200,50)
        IF button_1.collidepoint((mx,my)): # Checks IF mouse location overlaps button 1 location
            IF click: # Checks IF button has been clicked
                game()
        ENDIF
            ENDIF
        IF button_2.collidepoint((mx, my)):
            IF click:
                options()
        ENDIF
            ENDIF
        IF button_3.collidepoint((mx, my)):
            IF click:
                gameMode1()
        ENDIF
            ENDIF
        IF button_4.collidepoint((mx, my)): 
            IF click:
                gameMode2()
        ENDIF
            ENDIF
        IF button_5.collidepoint((mx, my)): 
            IF click:
                settings()
        ENDIF
            ENDIF
        IF button_6.collidepoint((mx, my)): 
            IF click:
                quit_game()
        ENDIF
            ENDIF
        pygame.draw.rect(screen, WHITE, button_1) # Draws a rectangle onto the screen in white colour for button 1
                                                                                                      ENDFOR
        draw_text("Main Game", font, BLACK, screen, 70, 110) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
                                                                                                        ENDIF
        pygame.draw.rect(screen, WHITE, button_2)
        draw_text("Options", font, BLACK, screen, 90, 210)
        pygame.draw.rect(screen, WHITE, button_3)
        draw_text("Game Mode 1", font, BLACK, screen, 60, 310)
        pygame.draw.rect(screen, WHITE, button_4)
        draw_text("Game Mode 2", font, BLACK, screen, 60, 410)
        pygame.draw.rect(screen, WHITE, button_5)
        draw_text("Settings", font, BLACK, screen, 90, 510)
        pygame.draw.rect(screen, WHITE, button_6)
        draw_text("Quit", font, BLACK, screen, 120, 610)
        click <- False
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT: # Checks IF the cross (top right button) has been pressed
                pygame.quit() # Program ends
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN: # Checks IF a key has been pressed
                IF event.key = K_ESCAPE: # Checks IF escape key has been pressed
                    pygame.quit() # Programs ends
                    sys.exit()
            ENDIF
                ENDIF
            IF event.type = MOUSEBUTTONDOWN: # Checks IF mouse button has been pressed
                IF event.button = 1: # Checks IF button has been clicked
                    click <- True
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update() # Updates display
        clock.tick(FPS) # 
ENDFUNCTION

    ENDWHILE
FUNCTION game():
    run <- True
    while run:
        screen.fill(BLACK)
        draw_text('Main Game', font, WHITE, screen, 20, 20)
        player1 <- Player(False, 0, 20)
        player2 <- Player(False, 0, 20)
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT:
                pygame.quit()
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_ESCAPE:
                    run <- False
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update()
        clock.tick(FPS)
ENDFUNCTION

    ENDWHILE
FUNCTION options():
    run <- True
    while run:
        screen.fill(BLACK)
        draw_text('Options', font, WHITE, screen, 20, 20)
        button_7 <- pygame.Rect(20,60,300,50)
        pygame.draw.rect(screen, WHITE, button_7)
        draw_text('Select Striker Colour', font, BLACK, screen, 20, 60)
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT:
                pygame.quit()
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_ESCAPE:
                    run <- False
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update()
        clock.tick(FPS)
ENDFUNCTION

    ENDWHILE
FUNCTION gameMode1():
    run <- True
    while run:
        screen.fill(BLACK)
        draw_text('Game Mode 1', font, WHITE, screen, 20, 20)
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT:
                pygame.quit()
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_ESCAPE:
                    run <- False # Returns to main menu
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update()
        clock.tick(FPS)
ENDFUNCTION

    ENDWHILE
FUNCTION gameMode2():
    run <- True
    while run:
        screen.fill(BLACK)
        draw_text('Game Mode 2', font, WHITE, screen, 20, 20)
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT:
                pygame.quit()
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_ESCAPE:
                    run <- False
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update()
        clock.tick(FPS)
ENDFUNCTION

    ENDWHILE
FUNCTION settings():
    run <- True
    while run:
        screen.fill(BLACK)
        draw_text('Settings', font, WHITE, screen, 20, 20)
        draw_text('X-Senstivity', font, WHITE, screen, 20, 60)
        draw_text('Y-Senstivity', font, WHITE, screen, 20, 100)
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT:
                pygame.quit()
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_ESCAPE:
                    run <- False
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update()
        clock.tick(FPS)
ENDFUNCTION

    ENDWHILE
    
FUNCTION quit_game():
    run <- True
    while run:
        screen.fill(BLACK)
        draw_text('Quit?', font, WHITE, screen, 20, 20)
        draw_text('Press Q to confirm', font, WHITE, screen, 20, 60)
        draw_text('Press ESC to return', font, WHITE, screen, 20, 100)
        events <- pygame.event.get()
        for event in events:
            IF event.type = QUIT:
                pygame.quit()
                sys.exit()
            ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_ESCAPE:
                    run <- False
            ENDIF
                ENDIF
            IF event.type = KEYDOWN:
                IF event.key = K_q:
                    run <- False
                    pygame.quit()
            ENDIF
                ENDIF
        ENDFOR
        pygame.display.update()
        clock.tick(FPS)
ENDFUNCTION

    ENDWHILE
main_menu()
