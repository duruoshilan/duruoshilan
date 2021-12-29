import pygame
from .sprite import Sprite

class Switch(Sprite):
    def __init__(self, screens, x, y):
        super().__init__(screens)
        self.status = "switch_close"
        self.scale = 40
        self.x, self.y = x, y

        self.close_src = "{0}/images/sprite/{1}.png".format(self.path, "switch_close")
        self.close_image = pygame.image.load(self.close_src)

        self.open_src = "{0}/images/sprite/{1}.png".format(self.path, "switch_open")
        self.open_image = pygame.image.load(self.open_src)

        self.image = self.close_image
        self.rect = self.image.get_rect()
        
        screens.switchs.append(self)

    def update(self):
        
        if self.status == "switch_close":
            self.image = self.close_image            
        else:
            self.image = self.open_image

        super().update()

    def changeStatus(self):
        if self.status == "switch_close":
            self.status = "switch_open"
            
        else:
            self.status = "switch_close"