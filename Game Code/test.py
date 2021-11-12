import pygame
run = True
while run:
    window = pygame.display.set_mode((300, 300))
    colour = (0,0,255) #green
    circle_x_y = (150, 50)
    circle_radius = 12
    border_width = 0 #0 = filled circle

    pygame.draw.circle(window, colour, circle_x_y, circle_radius, border_width)

    pygame.display.update()