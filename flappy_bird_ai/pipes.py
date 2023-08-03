import random
import pygame
import neat
import time

from consts import PIPE_IMG, OBJ_VELOCITY

class Pipe:
    GAP = 200
    VEL = OBJ_VELOCITY  # how fast pipes are moving

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100

        self.top = 0  # where the top and bottom gonna be drawn
        self.bottom = 0
        # just rotate upside down - flip y - see params
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        # every time this foo is called we just move pipes a bit to the left
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        # for collision checking we will use masks - they represent the objects
        # threw "2d array" and we will just check if bird's mask hit something
        bird_mask = bird.get_mask()

        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # offset - how far are mask from each other
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        # look for point of collision
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)  # return None if not

        return t_point is not None or b_point is not None
