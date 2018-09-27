import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('PyGame demo')

    width, height = 540, 540
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    field = pygame.Rect(0, 0, 500, 500)

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        foreground = pygame.Surface((500, 500), pygame.SRCALPHA)
        foreground.fill(pygame.Color('black'))

        screen.fill((60, 70, 90))
        screen.blit(foreground, (20, 20))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
