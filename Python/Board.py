import random
import Input


class Board:
    def __init__(self):
        self.size = 4
        self.array = [[0 for i in range(self.size)] for i in range(self.size)]
        self.randomStart()

    def randomStart(self):
        # pick two grid let it have 2 or 4
        # 避免随机到两个数的情况
        cnt = 0
        while cnt < 2:
            i, j, n = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.randint(1, 2) * 2
            ind = self.array[i][j]
            if ind:
                continue
            self.array[i][j] = n
            cnt += 1

        pass

    def drawBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                num = self.array[i][j]
                if num == 0:
                    num = '*'
                print(f'\t{num}', end='')
            print()



if __name__ == '__main__':
    board = Board()
    board.drawBoard()
