from src.heart import Heart
from src.player import Player
from src.scenes import Scenes
from src.switch import Switch
from src.portal import PortalPair
from src.ground import AllAround, DownLeft, Left, LeftRight, NoEntry, NoUp, Right, UpDown

grounds = [
    [NoEntry, NoEntry, NoEntry, NoEntry, NoEntry],
    [NoEntry, NoEntry, NoEntry, NoEntry, NoEntry],
    [NoEntry, Right, LeftRight, LeftRight, Left],
    [NoEntry, NoEntry, NoEntry, NoEntry, NoEntry],
    [NoEntry, NoEntry, NoEntry, NoEntry, NoEntry],
]

game = Scenes(grounds)
player = Player(game, 1, 2)
Heart(game, 4, 2)

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