import random
from copy import deepcopy


class Board:
    def __init__(self):
        self.size = 4
        self.board = [[0 for i in range(self.size)] for i in range(self.size)]
        # test use it
        # self.board = [[0, 0, 0, 0], [2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.randomGenerate(2)

    def randomGenerate(self, num):
        # pick two grid let it have 2 or 4
        cnt = 0
        while cnt < num:
            i, j, n = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.randint(1, 10)
            ind = self.board[i][j]
            if ind:
                continue
            # 8:2 to generate 2 and 4
            n = 2 if n <= 8 else 4
            self.board[i][j] = n
            cnt += 1

    def drawBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                num = self.board[i][j]
                if num == 0:
                    num = '*'
                print(f'\t{num}', end='')
            print()

    def moveBoard(self, ind):
        # move to up, down, left, right
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        temp_board = deepcopy(self.board)
        add_score = 0

        def inBoard(x, y):
            if x < 0 or y < 0 or x >= self.size or y >= self.size:
                return False
            return True

        # move algorithm
        def moveAlgorithm():
            up_d = [[0, i] for i in range(self.size)]
            down_d = [[self.size - 1, i] for i in range(self.size)]
            left_d = [[i, 0] for i in range(self.size)]
            right_d = [[i, self.size - 1] for i in range(self.size)]

            sequence = [up_d, down_d, left_d, right_d]

            add_score = 0

            # get all start point
            for point in sequence[ind]:
                # x_,y_ is start point in every iteration
                x, y = point[0], point[1]
                x_, y_ = x, y
                while True:
                    dir = direction[ind]
                    nx, ny = x + dir[0], y + dir[1]

                    # continue move to target direction
                    while inBoard(nx, ny) and (temp_board[nx][ny] == temp_board[x][y] or temp_board[nx][ny] == 0):
                        tnum = temp_board[x][y]
                        if tnum == temp_board[nx][ny]:
                            add_score += (tnum * 2)

                        temp_board[x][y] = 0
                        temp_board[nx][ny] += tnum
                        # add_score += (tnum * 2)
                        x, y = nx, ny
                        nx, ny = x + dir[0], y + dir[1]

                    # break if stop at end end point else continue move
                    x_, y_ = x_ - dir[0], y_ - dir[1]
                    if not inBoard(x_, y_):
                        break
                    else:
                        x, y = x_, y_
            return add_score

        add_score = moveAlgorithm()

        zero_sum = sum([temp_board[i][j] == 0 for i in range(self.size) for j in range(self.size)])

        # if board after move equals board origin and no more place to generate num
        # game over
        if temp_board == self.board:
            if zero_sum == 0:
                return -1  # return -1 denote end game
            else:
                return None  # nothing change, dont generate new number

        # replace old board
        self.board = temp_board
        # generate number
        self.randomGenerate(1)
        #
        return add_score


if __name__ == '__main__':
    board = Board()
    board.drawBoard()
    board.moveBoard(3)
