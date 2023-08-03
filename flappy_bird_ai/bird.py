import pygame

from consts import BIRD_IMGS


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20  # rotation velocity how much we gonna rotate on each frame
    ANIMATION_TIME = 5  # how long we gonna change bird animation - how fast bird flies, waves with wings

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0  # when we last jump, how many times we moved since last jump
        self.vel = 0  # velocity
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self) -> None:
        # because in pygames (0,0) is top left corner if we wanna our bird to
        # fly up, we need - scaler and if down we need positive number...
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self) -> None:
        self.tick_count += 1  # -> how many times we moved since last jump

        # tick_count is the key -> it tells us if the bird is still going up
        # or falling down...
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        if d >= 16:  # if we moving down for too long dont scale more and more
            d = 16

        if d < 0:  # if we moving upwords move upwords more
            d -= 2

        self.y = self.y + d

        # tilt - whitch picture to use... look if we re going up, or down simply put...
        # if we moving up, or falling just a little
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        elif self.tilt > -90:  # we go down
            self.tilt -= self.ROT_VEL  # we wanna tilt all the way down now

    def draw(self, win) -> None:
        self.img_count += 1

        # what image we should show based of image_count
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # if bird is falling down he doesnt flap his wings...
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # rotate image from its center in pygames
        # now rotating from top left corner
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        # defying center of image
        new_rect = rotated_image.get_rect(center=self.img.get_rect(
                topleft=(self.x, self.y)).center
                                          )
        # now we have to blit it into our window... blit -> vypalit -> draw
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

