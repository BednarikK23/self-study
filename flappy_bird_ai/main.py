import pygame
import neat
import time
import os
import random

from bird import Bird
from consts import BG_IMG, WIN_HEIGHT, WIN_WIDTH



def draw_window(win, bird):
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)

    pygame.display.update()


def main():
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    # without this our bird starts falling cause the wile loop iterating so fast
    # on some platform it will be slower or faster, this gives stable time to our game
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():  # chcking for events
            if event.type == pygame.QUIT:
                run = False
        bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()
    return


if __name__ == '__main__':
    main()
