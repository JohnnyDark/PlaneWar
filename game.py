from enum import Enum


class Status(Enum):
    RUNNING = 1
    PAUSE = 2
    QUIT = 0


class Game(object):
    def __init__(self):
        # 得分记录
        self.score = 0
        # 游戏状态
        self.status = Status.RUNNING
        # 游戏难度
        self.level = 1

    def game_start(self):
        pass

    def game_pause(self):
        self.status = Status.PAUSE

    def game_quit(self):
        self.status = Status.QUIT
