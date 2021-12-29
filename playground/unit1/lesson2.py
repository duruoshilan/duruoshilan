from src.portal import PortalPair
from src.scenes import Scenes
from src.player import Player
from src.heart import Heart
from src.ground import AllAround, DownLeft, Left, LeftRight, NoDown, NoEntry, NoLeft, NoRight, NoUp, Right, UpDown

grounds = [
    [Right,  NoUp, NoUp, NoUp, Left],
    [Right, NoRight,  UpDown, NoLeft, Left],
    [Right, NoRight,  UpDown, NoLeft, Left],
    [Right, NoRight,  UpDown, NoLeft, Left],
    [ Right, NoDown,  NoDown, NoDown, Left]
]

game = Scenes(grounds)
player = Player(game, 0, 4)
Heart(game, 2, 2)
Heart(game, 3, 0)
Heart(game, 1, 1)
Heart(game, 2, 1)
Heart(game, 3, 1)
Heart(game, 1, 2)
Heart(game, 1, 3)
Heart(game, 1, 4)
PortalPair(game, (1, 0), (3, 4), "yellow")

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