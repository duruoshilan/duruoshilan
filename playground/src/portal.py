import pygame
from .sprite import Sprite

class Portal(Sprite):
    def __init__(self, screens, x, y, color):
        super().__init__(screens)
        self.x, self.y = x, y
        self.another = None

        self.image_src = "{0}/images/sprite/{1}_portal.png".format(self.path, color)
        self.image = pygame.image.load(self.image_src)
        self.rect = self.image.get_rect()

        screens.portals.append(self)

    def jump(self):
        player = self.screens.player
        player.x, player.y = self.another.x, self.another.y

class PortalPair:
    def __init__(self, screens, pos1, pos2, color):
        portal1 = Portal(screens, pos1[0], pos1[1], color)
        portal2 = Portal(screens, pos2[0], pos2[1], color)
        portal1.another = portal2
        portal2.another = portal1