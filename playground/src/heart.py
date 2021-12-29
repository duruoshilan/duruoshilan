import pygame
from .sprite import Sprite

class Heart(Sprite):
    def __init__(self, screens, x, y):
        super().__init__(screens)
        self.status = "open"
        self.x, self.y = x, y

        self.image_src = "{0}/images/sprite/{1}.png".format(self.path, "heart")
        self.image = pygame.image.load(self.image_src)
        self.rect = self.image.get_rect()

        screens.hearts.append(self)

    def update(self):
        if self.status == "close":
            pygame.sprite.Sprite.kill(self)

        super().update()

    def changeStatus(self):
        if self.status == "close":
            self.status = "open"
        else:
            self.status = "close"