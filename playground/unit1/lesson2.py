from src.portal import PortalPair
from src.scenes import Scenes
from src.player import Player
from src.heart import Heart
from src.word import Word
from src.monster import Monster
from src.switch import Switch
from src.ground import AllAround, DownLeft, Left, LeftRight, NoDown, NoEntry, NoLeft, NoRight, NoUp, Right, UpDown

grounds = [
    [NoEntry, NoEntry, NoEntry, NoEntry, NoEntry],
    [Right,  NoUp, NoUp, NoUp, Left],
    [Right, NoRight,  UpDown, NoLeft, Left],
    [Right, NoRight,  UpDown, NoLeft, Left],
    [Right, NoRight,  UpDown, NoLeft, Left],
    [Right, NoDown,  NoDown, NoDown, Left],
]

game = Scenes(grounds)
player = Player(game, 0, 5)
# Heart(game, 1, 1)
Word(game, 1, 1, "春", 0, 0)
Word(game, 1, 4, "暖", 1, 0)
Word(game, 1, 3, "花", 2, 0)
Word(game, 3, 3, "开", 3, 0)
Monster(game, 3, 2, "mst01")
# Monster(game, 2, 4, "mst02")
Switch(game, 2, 5)
PortalPair(game, (1, 2), (3, 4), "yellow")

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

def collectWord():
    player.collectWord()