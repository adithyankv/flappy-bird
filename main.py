import pygame
import math


def main():
    pygame.init()

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    background = pygame.image.load("assets/images/background.png").convert()
    ground = pygame.image.load("assets/images/ground.png").convert()
    shrubs = pygame.image.load("assets/images/shrubs.png").convert_alpha()
    bird = pygame.image.load("assets/images/bird.png").convert_alpha()

    background_x = 0
    ground_x = 0
    shrubs_x = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_tiled_images(background, screen, background_x, 0)
        draw_tiled_images(ground, screen, ground_x, SCREEN_HEIGHT - ground.get_height())
        draw_tiled_images(
            shrubs,
            screen,
            shrubs_x,
            SCREEN_HEIGHT - (shrubs.get_height() + ground.get_height()),
        )

        background_x = scroll_image(background, 1, background_x)
        ground_x = scroll_image(ground, 4, ground_x)
        shrubs_x = scroll_image(shrubs, 2, shrubs_x)

        bird_width, bird_height = 64, 48
        bird_x_pos = SCREEN_WIDTH / 2 - bird_width / 2
        bird_y_pos = SCREEN_HEIGHT / 2 - bird_height / 2
        screen.blit(bird, (bird_x_pos, bird_y_pos))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def draw_tiled_images(image, screen, x_pos, y_pos):
    # Minimum number of tiles that are required to span the whole screen
    # and then one extra tile, as scroll is reset only when one whole tile
    # goes off screen.
    num_tiles = math.ceil(screen.get_width() / image.get_width()) + 1
    for i in range(num_tiles):
        screen.blit(image, ((x_pos + i * image.get_width()), y_pos))


def scroll_image(image, speed, x_pos):
    if x_pos < -image.get_width():
        return 0
    return x_pos - speed


if __name__ == "__main__":
    main()
