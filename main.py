import pygame


def main():
    pygame.init()

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True

    background = pygame.image.load("assets/images/background.png").convert()
    num_background_tiles = SCREEN_WIDTH // background.get_width() + 1
    background_position = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if background_position < -background.get_width():
            background_position = 0

        for i in range(num_background_tiles):
            screen.blit(background, (background_position, 0))
            screen.blit(background, (background_position + background.get_width(), 0))
        background_position -= 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
