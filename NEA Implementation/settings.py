def settings():

    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Settings', font, WHITE, screen, 20, 20)

        drawText('X-Senstivity', font, WHITE, screen, 20, 60)
        drawText('Y-Senstivity', font, WHITE, screen, 20, 100)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        
        pygame.display.update()
        clock.tick(FPS)