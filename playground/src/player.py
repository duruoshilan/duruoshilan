import os
import pygame
from enum import Enum

class Face(Enum):
    Right = 0
    Up = 1
    Left = 2
    Down = 3
    
    def forward(self, x, y, delaytime = 1):
        if self.value == self.Right.value:
            return x + delaytime, y
        elif self.value == self.Left.value:
            return x - delaytime, y
        elif self.value == self.Up.value:
            return x, y - delaytime
        elif self.value == self.Down.value:
            return x, y + delaytime

    def turnLeft(self):
        return Face((self.value + 1) % len(Face))
    
    def turnRight(self):
        return Face((self.value - 1) % len(Face))
    
    def turnAround(self):
        return Face((self.value + 2) % len(Face))

class Player(pygame.sprite.Sprite):
    def __init__(self, scenes, x = 0, y = 0):
        super().__init__()

        path = os.path.abspath(".")
        self.idle_src = "{0}/images/player/Idle32_32.png".format(path)
        self.run_src = "{0}/images/player/Run32_32.png".format(path)

        self.scenes = scenes
        self.idle_image = pygame.image.load(self.idle_src)
        self.run_image = pygame.image.load(self.run_src)

        self.image = self.idle_image.subsurface(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.sprite_x = 0

        self.start_x, self.start_y = x, y
        self.x, self.y = x, y
        self.scale = 50

        self.scenes.player = self
        self.status = "idle"
        self.heading = Face.Right
        self.isFlip = False
      
    def update(self):
        if self.status == "idle":
            # 闲置状态 11 张图
            self.update_player(11-1, self.idle_image)
        elif self.status == "run":
            # 奔跑状态 12 张图
            self.update_player(12-1, self.run_image)

    def update_player(self, actionNumber, playerImage):
        if self.sprite_x > 32 * actionNumber - 1:
            self.sprite_x = 0
        
        self.sprite_x += 32
        rect = self.sprite_x, 0, 32, 32

        self.image = playerImage.subsurface(rect)
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.image = pygame.transform.flip(self.image, self.isFlip, False)
        self.rect.center = (self.x * self.scenes.scale_size + self.scale // 2 + 15, self.y * self.scenes.scale_size + self.scale // 2 + 10)

    def moveforward(self):
        nextX, nextY = self.heading.forward(self.x, self.y)
        thisGround = self.scenes.getGround(self.x, self.y)
        nextGround = self.scenes.getGround(nextX, nextY)

        self.status = "run"
        delaytime = 1 / 25
        if thisGround.checkmove(self.heading) and nextGround.checkmove(self.heading.turnAround()):
            for i in range(25):
                self.x, self.y = self.heading.forward(self.x, self.y, delaytime)
                pygame.time.delay(60)
        else:
            for i in range(5):
                self.x, self.y = self.heading.forward(self.x, self.y, delaytime)
                pygame.time.delay(60)
            for i in range(5):
                self.x, self.y = self.heading.forward(self.x, self.y, -delaytime)
                pygame.time.delay(60)
        
        self.status = "idle"
        pygame.time.delay(1*500)

        portal = self.scenes.getPortal(self.x, self.y)
        if self.scenes.isOnMonster(self.x, self.y):
            self.x, self.y = self.start_x, self.start_y
        if portal:
            portal.jump()

    def toggleSwitch(self):
        switch = self.scenes.getSwitch(self.x, self.y)
        monster = self.scenes.getMonster()
        if switch :
            pygame.time.delay(1*200)
            switch.changeStatus()
            monster.changeStatus()
            pygame.time.delay(1*200)

    def collectHeart(self):
        heart = self.scenes.getHeart(self.x, self.y)
        if heart:
            pygame.time.delay(1*200)
            heart.changeStatus()
            pygame.time.delay(1*200)

    def turnLeft(self):
        self.heading = self.heading.turnLeft()
        if self.heading == Face.Right:
            self.isFlip = False
        elif self.heading == Face.Left:
            self.isFlip = True

        pygame.time.delay(1*500)

    def turnRight(self):
        self.heading = self.heading.turnRight()
        if self.heading == Face.Right:
            self.isFlip = False
        elif self.heading == Face.Left:
            self.isFlip = True
            
        pygame.time.delay(1*500)
    
    def collectWord(self):
        word = self.scenes.getWord(self.x, self.y)
        if word:
            word.x = word.to_x
            word.y = word.to_y