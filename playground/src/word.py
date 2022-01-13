import pygame
from .sprite import Sprite

class Word(Sprite):
    def __init__(self, screens, x, y, name, to_x, to_y):
        super().__init__(screens)
        self.status = "open"
        self.x, self.y = x, y
        self.to_x = to_x
        self.to_y = to_y

        self.image_src = "{0}/images/sprite/{1}.png".format(self.path, name)
        self.image = pygame.image.load(self.image_src)
        self.scale = 50
        self.rect = self.image.get_rect()

        screens.word.append(self)

    def update(self):
        if self.status == "close":
            pygame.sprite.Sprite.kill(self)

        # super().update()
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect.center = (self.x * self.screens.scale_size + self.scale // 2 + 38, self.y * self.screens.scale_size + self.scale // 2 + 42)

    def changeStatus(self):
        if self.status == "close":
            self.status = "open"
        else:
            self.status = "close"