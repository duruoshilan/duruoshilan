from src.heart import Heart
from src.player import Player
from src.scenes import Scenes
from src.switch import Switch
from src.portal import PortalPair
from src.ground import AllAround, Down, DownLeft, DownRight, Left, LeftRight, NoDown, NoEntry, NoLeft, NoRight, NoUp, Right, UpDown, UpLeft, UpRight

grounds = [
    [DownRight, LeftRight, NoUp, LeftRight, DownLeft],
    [UpDown, NoEntry, UpDown, Down, UpDown],
    [NoLeft, LeftRight, AllAround, AllAround, NoRight],
    [NoLeft, LeftRight, AllAround, AllAround, NoRight],
    [UpRight, LeftRight, NoDown, NoDown, UpLeft],
]

game = Scenes(grounds)
player = Player(game, 1, 2)
Heart(game, 4, 2)
Heart(game, 2, 2)
Heart(game, 3, 4)
Switch(game, 0, 3)
Switch(game, 2, 0)
PortalPair(game, (3, 3), (1, 0), "yellow")

def moveForward():
    player.moveforward()

def toggleSwitch():
    player.toggleSwitch()

def collectHeart():
    player.collectHeart()

def turnLeft():
    player.turnLeft()

def turnRight():
    player.turnRight()