import os
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, screens):
        super().__init__()
        self.screens = screens
        self.scale = 30
        self.x, self.y = 0, 0
        self.path = self.path = os.path.abspath(".")
        

    def update(self):
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect.center = (self.x * self.screens.scale_size + self.scale // 2 + 27, self.y * self.screens.scale_size + self.scale // 2 + 25)