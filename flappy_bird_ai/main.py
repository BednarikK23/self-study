import pygame
import neat
from collections import deque

from bird import Bird
from consts import BG_IMG, WIN_HEIGHT, WIN_WIDTH, GROUND_LEVEL, PIPE_DIST, \
    STAT_FONT
from base import Base
from pipes import Pipe


def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

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
        pipes.append(Pipe(PIPE_DIST))

    for _ in range(count_remove):
        pipes.popleft()

    return score


def floor_hit(bird):
    if bird.y + bird.img.get_height() >= GROUND_LEVEL:
        pass


def main():
    bird = Bird(230, 350)
    base = Base(GROUND_LEVEL)
    pipes = deque([Pipe(PIPE_DIST)])

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
        floor_hit(bird)
        base.move()

        draw_window(win, bird, pipes, base, score)


    pygame.quit()
    quit()
    return


if __name__ == '__main__':
    main()
