import pygame
from .sprite import Sprite

class Monster(Sprite):
    def __init__(self, screens, x, y, name):
        super().__init__(screens)
        self.status = "open"
        self.x, self.y = x, y

        self.image_src = "{0}/images/sprite/{1}.png".format(self.path, name)
        self.image = pygame.image.load(self.image_src)
        self.scale = 40
        self.rect = self.image.get_rect()

        screens.monster.append(self)

    def update(self):
        if self.status == "close":
            pygame.sprite.Sprite.kill(self)

        super().update()
        # self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        # self.rect.center = (self.x * self.screens.scale_size + self.scale // 2 + 10, self.y * self.screens.scale_size + self.scale // 2 + 10)

    def changeStatus(self):
        if self.status == "close":
            self.status = "open"
        else:
            self.status = "close"