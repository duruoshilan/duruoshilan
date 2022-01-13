import sys, pygame

class Render:
    def __init__(self, scenes):
        self.scenes = scenes
        self.bgcolor = (240, 240, 240)
        self.size = self.scenes.scale_size
        self.map_line = self.scenes.map_line
        self.map_col = self.scenes.map_col
        self.sprite_group = pygame.sprite.Group()
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.map_col * self.size, self.map_line * self.size))
        clock = pygame.time.Clock()

        self.sprite_group.add(self.scenes.portals)
        self.sprite_group.add(self.scenes.player)
        self.sprite_group.add(self.scenes.hearts)
        self.sprite_group.add(self.scenes.switchs)
        self.sprite_group.add(self.scenes.word)
        self.sprite_group.add(self.scenes.monster)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            screen.fill(self.bgcolor)

            # render ground
            for x in range(self.map_line):
                for y in range(self.map_col):
                    ground = self.scenes.grounds[x][y]
                    image = pygame.image.load(ground.img)
                    image = pygame.transform.scale(image, (self.size, self.size))
                    rect = image.get_rect()
                    rect.center = (y * self.size + self.size // 2, x * self.size + self.size // 2)
                    screen.blit(image, rect)
        
            self.sprite_group.draw(screen)
            self.sprite_group.update()

            clock.tick(40)
            pygame.display.update()