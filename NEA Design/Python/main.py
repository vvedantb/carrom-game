import pygame # Used to create GUI
import time # Used to set refresh rate
import os # Used to import images
import random # Randomises events 
import sys #          
import pygame_widgets as pw # Used to create buttons


























WIDTH, HEIGHT = 1900, 1000 # Height dimensions
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) # Sets the width and height of the program
pygame.display.set_caption("Carrom Game") # Caption of the app when program is run


pygame.init()
screen = pygame.display.set_mode((1280,720))
menuAtivo = True

start_button = pygame.draw.rect(screen,(20,0,240),(150,90,100,50))
continue_button = pygame.draw.rect(screen,(20,244,0),(150,160,100,50))
quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50))


# ---------
# CONSTANTS 
# ---------
BLACK = (0,0,0)



def startGame():
    screen.fill(BLACK)
    pygame.display.update()
    import game.py


def main():
    pygame.init()
    clock = pygame.time.Clock() # Controls the speed of how many times the while loop gets refreshed. 
    FPS = 60
    run = True

    while run:        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                sys.exit()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                    if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                            pygame.quit();
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                    if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                            startGame();
        clock.tick(FPS) # While loop will refresh 60 times a second, no matter what. Ensures it doesn't go above 60.
        WIN.fill(BLACK)


main()
