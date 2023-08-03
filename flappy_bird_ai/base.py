from consts import BASE_IMG, OBJ_VELOCITY


class Base:
    VEL = OBJ_VELOCITY
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y: int) -> None:
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self) -> None:
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win) -> None:
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
