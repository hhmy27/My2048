from InputFlow import InputFlow
from Score import Score
from Board import Board


class Game:
    def __init__(self):
        self.board_controller = Board()
        self.input_flow = InputFlow()
        pass

    def runGame(self):
        flag = None
        self.board_controller.drawBoard()
        while True:
            key = self.input_flow.getKey()
            flag = self.board_controller.moveBoard(key)
            if not flag:
                break
            self.board_controller.randomGenerate()
            self.board_controller.drawBoard()

        print("Game over")


if __name__ == '__main__':
    game = Game()
    game.runGame()
