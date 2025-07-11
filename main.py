import pygame
import math


def main():
    pygame.init()

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True

    background = pygame.image.load("assets/images/background.png").convert()
    ground = pygame.image.load("assets/images/ground.png").convert()
    # needs atleast two tiles to keep the screen always covered
    num_background_tiles = max(2, math.ceil(SCREEN_WIDTH / background.get_width()))
    num_ground_tiles = max(2, math.ceil(SCREEN_WIDTH / ground.get_width()))

    background_x = 0
    ground_x = 0

    background_scroll_speed = 1
    ground_scroll_speed = 4

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # if background_scroll < -background.get_width():
        #     background_scroll = 0

        if background_x < -background.get_width():
            background_x = 0

        if ground_x < -ground.get_width():
            ground_x = 0

        for i in range(num_background_tiles):
            screen.blit(background, (background_x + i * background.get_width(), 0))

        for i in range(num_ground_tiles):
            screen.blit(
                ground,
                (
                    ground_x + i * ground.get_width(),
                    SCREEN_HEIGHT - ground.get_height(),
                ),
            )
        ground_x -= ground_scroll_speed
        background_x -= background_scroll_speed

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
