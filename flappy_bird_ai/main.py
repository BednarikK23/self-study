import pygame
import neat
from collections import deque

from bird import Bird
from consts import BG_IMG, WIN_HEIGHT, WIN_WIDTH
from base import Base
from pipes import Pipe


def draw_window(win, bird, pipes, base):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)

    pygame.display.update()


def moving_pipes(pipes, bird, score):
    count_remove = 0
    add_pipe = False
    for pipe in pipes:
        if pipe.collide(bird):
            pass
        if pipe.x + pipe.PIPE_TOP.get_width() < 0:
            count_remove += 1

        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            add_pipe = True
        pipe.move()

    if add_pipe:
        score += 1
        pipes.append(Pipe(600))

    for _ in range(count_remove):
        pipes.popleft()

    return score


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = deque()
    pipes.append(Pipe(600))

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    # without this our bird starts falling cause the wile loop iterating so fast
    # on some platform it will be slower or faster, this gives stable time to our game
    clock = pygame.time.Clock()

    score = 0
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():  # chcking for events
            if event.type == pygame.QUIT:
                run = False
        # bird.move()

        score = moving_pipes(pipes, bird, score)

        base.move()
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()
    return


if __name__ == '__main__':
    main()
