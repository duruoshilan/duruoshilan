import threading
import math
from src.render import Render

class Scenes:
    def __init__(self, grounds):
        self.scale_size = 100
        self.grounds = grounds
        self.map_line = len(self.grounds)
        self.map_col = len(self.grounds[0])
        self.render = Render(self)
        self.player = None
        self.switchs = []
        self.hearts = []
        self.portals = []
        self.word = []
        self.monster = []

        for x in range(self.map_line):
            for y in range(self.map_col):
                self.grounds[x][y] = self.grounds[x][y]()
        
    def play(self, work):
        t = threading.Thread(target=work, name="PlayerWork")
        t.setDaemon(True)
        t.start()
        self.render.run()

    def getGround(self, x, y):
        x, y = round(x), round(y)
        return self.grounds[y][x]

    def getSwitch(self, x, y):
        x, y = round(x), round(y)
        for switch in self.switchs:
            if switch.x == x and switch.y == y:
                return switch
    
    def getHeart(self, x, y):
        x, y = round(x), round(y)
        for heart in self.hearts:
            if heart.x == x and heart.y == y:
                return heart

    def isOnMonster(self, x, y):
        x, y = round(x), round(y)
        for monster in self.monster:
            if monster.x == x and monster.y == y and monster.status == "open":
                return True
        return False

    def getMonster(self):
        return self.monster[0]

    def getPortal(self, x, y):
        x, y = round(x), round(y)
        for portal in self.portals:
            if portal.x == x and portal.y == y:
                return portal

    def getWord(self, x, y):
        x, y = round(x), round(y)
        for word in self.word:
            if word.x == x and word.y == y:
                return word