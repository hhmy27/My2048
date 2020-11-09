from src.InputFlow import InputFlow
from src.Board import Board
from src.Score import Score


class Game:
    def __init__(self):
        self.board_controller = Board()
        self.input_flow = InputFlow()
        self.score_controller = Score()
        pass

    def runGame(self):
        self.displayEvent()
        while True:
            key = self.getKeyEvent()
            flag = self.moveBoardEvent(key)
            if flag == -1:
                break
            # add score
            self.score_controller.cur_score += flag if flag != None else 0
            self.displayEvent()
        self.gameOverEvent()

    def getKeyEvent(self):
        # process keyboard input
        while True:
            key = self.input_flow.getKey()
            if key is not None:
                return key

    def moveBoardEvent(self, key):
        flag = self.board_controller.moveBoard(key)
        return flag

    def displayEvent(self):
        print('*' * 30)
        self.score_controller.showScore()
        self.board_controller.drawBoard()
        print('*' * 30)

    def gameOverEvent(self):
        self.score_controller.writeScore()
        print("Game over")


if __name__ == '__main__':
    game = Game()
    game.runGame()
