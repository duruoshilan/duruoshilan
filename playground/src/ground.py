from enum import Flag
import os, random
from src.player import Face

class Ground:
    def __init__(self, groundType):
        path = os.path.abspath(".")
        self.img = "{0}/images/ground/{1}.png".format(path, groundType)
        self.x, self.y = 0, 0
        self.left = True
        self.right = True
        self.up = True
        self.down = True

    def checkmove(self, playerHeading):
        if playerHeading == Face.Left:
            return self.left
        elif playerHeading == Face.Right:
            return self.right
        elif playerHeading == Face.Up:
            return self.up
        elif playerHeading == Face.Down:
            return self.down

class NoEntry(Ground):
    def __init__(self):
        super().__init__(random.choice(["NoEntry", "NoEntry2"]))
        self.left = False
        self.right = False
        self.up = False
        self.down = False

class Right(Ground):
    def __init__(self):
        super().__init__("Right")
        self.left = False
        self.up = False
        self.down = False

class LeftRight(Ground):
    def __init__(self):
        super().__init__("LeftRight")
        self.up = False
        self.down = False

class Left(Ground):
    def __init__(self):
        super().__init__("Left")
        self.up = False
        self.down = False
        self.right = False

class Down(Ground):
    def __init__(self):
        super().__init__("Down")
        self.up = False
        self.left = False
        self.right = False

class Up(Ground):
    def __init__(self):
        super().__init__("Up")
        self.down = False
        self.left = False
        self.right = False

class UpDown(Ground):
    def __init__(self):
        super().__init__("UpDown")
        self.left = False
        self.right = False

class AllAround(Ground):
    def __init__(self):
        super().__init__("AllAround")

class UpDown(Ground):
    def __init__(self):
        super().__init__("UpDown")
        self.left = False
        self.right = False

class DownLeft(Ground):
    def __init__(self):
        super().__init__("DownLeft")
        self.up = False
        self.right = False

class DownRight(Ground):
    def __init__(self):
        super().__init__("DownRight")
        self.up = False
        self.left = False

class UpLeft(Ground):
    def __init__(self):
        super().__init__("UpLeft")
        self.down = False
        self.right = False

class UpRight(Ground):
    def __init__(self):
        super().__init__("UpRight")
        self.down = False
        self.left = False

class NoDown(Ground):
    def __init__(self):
        super().__init__("NoDown")
        self.down = False

class NoLeft(Ground):
    def __init__(self):
        super().__init__("NoLeft")
        self.left = False

class NoRight(Ground):
    def __init__(self):
        super().__init__("NoRight")
        self.right = False

class NoUp(Ground):
    def __init__(self):
        super().__init__("NoUp")
        self.up = False
