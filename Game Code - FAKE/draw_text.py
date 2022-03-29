def drawText(text, font, color, surface, x, y): # Writes text onto the screen of the program
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)