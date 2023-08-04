import os
import pygame
import neat
# https://neat-python.readthedocs.io/en/latest/config_file.html

from collections import deque

from bird import Bird
from consts import BG_IMG, WIN_HEIGHT, WIN_WIDTH, GROUND_LEVEL, PIPE_DIST, \
    STAT_FONT
from base import Base
from pipes import Pipe


def draw_window(win, birds, pipes, base, score):
    win.blit(BG_IMG, (0, 0))

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    for bird in birds:
        bird.draw(win)

    pygame.display.update()


def moving_pipes(pipes, birds, score, ge, nets):
    count_remove = 0
    add_pipe = False

    for pipe in pipes:
        for i, bird in enumerate(birds):
            if pipe.collide(bird):
                ge[i].fitness -= 1
                birds.pop(i)
                nets.pop(i)
                ge.pop(i)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

        if pipe.x + pipe.PIPE_TOP.get_width() < 0:
            count_remove += 1

        pipe.move()

    if add_pipe:
        score += 1
        for g in ge:
            g.fitness += 5

        pipes.append(Pipe(PIPE_DIST))


    for _ in range(count_remove):
        pipes.popleft()

    return score


def floor_hit(birds, ge, nets):
    for i, bird in enumerate(birds):
        if bird.y + bird.img.get_height() >= GROUND_LEVEL or bird.y < 0:
            birds.pop(i)
            ge.pop(i)
            nets.pop(i)


def main(genomes, config):
    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)


    base = Base(GROUND_LEVEL)
    pipes = deque([Pipe(PIPE_DIST)])

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    # without this our bird starts falling cause the wile loop iterating so fast
    # on some platform it will be slower or faster, this gives stable time to our game
    clock = pygame.time.Clock()

    score = 0
    is_run = True
    while is_run:
        clock.tick(30)
        for event in pygame.event.get():  # chcking for events
            if event.type == pygame.QUIT:
                is_run = False
                pygame.quit()
                quit()

        # on the screen there can be 2 pipes, we need to know with which to
        # work with... initially work with first pipe - pipes[0]:
        pip_ind = 0
        # then look, if birds are living, on screen are 2 pipes, and the living
        # bird is behind the first pipe work with the second pipe (pipes[1]):
        if len(birds) <= 0:
            break

        if len(pipes) > 1 and \
                birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
            pip_ind = 1

        for i, bird in enumerate(birds):
            bird.move()
            if len(ge) > i:
                ge[i].fitness += 0.1

            output = nets[i].activate((bird.y,
                                       abs(bird.y - pipes[pip_ind].height),
                                       abs(bird.y - pipes[pip_ind].bottom)
                                       ))
            if output[0] > 0.5:
                bird.jump()

        score = moving_pipes(pipes, birds, score, ge, nets)
        floor_hit(birds, ge, nets)
        base.move()

        draw_window(win, birds, pipes, base, score)

    return


def run(config_path):
    # load up the configuration file for neat
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                              neat.DefaultSpeciesSet, neat.DefaultStagnation,
                              config_path)

    # set up population
    p = neat.Population(config)
    # set the output we gonna see
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # set the fitness function -> we will use main
    winner = p.run(main, 50)



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)  # fancy way to get local position
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
