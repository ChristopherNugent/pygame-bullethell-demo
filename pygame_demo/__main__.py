import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('PyGame demo')

    # Set up some stuff for our window
    width, height = 540, 540
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # Main event loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            # Quit if the exit button is clicked
            if event.type == pygame.QUIT:
                game_exit = True
        # Some background stuff
        foreground = pygame.Surface((500, 500), pygame.SRCALPHA)
        foreground.fill(pygame.Color('black'))

        # Draw our output to the screen
        screen.fill((60, 70, 90))   # a gray color
        screen.blit(foreground, (20, 20))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
