class Score:
    def __init__(self):
        self.__score = None
        self.__ini_score = None
        self.path = '../history/score'
        self.readHistory()

    @property
    def ini_score(self):
        return self.__ini_score

    @ini_score.setter
    def ini_score(self, value):
        self.__ini_score = value

    @property
    def score(self):
        return self.__score

    @score.getter
    def score(self):
        return self.__score

    @score.setter
    def score(self, num):
        if isinstance(num, int):
            self.__score = num

    def readHistory(self):
        with open(self.path, 'r') as f:
            record = f.read()
            self.score = 0 if record == '' else int(record, 10)
            self.ini_score = self.score

    def writeScore(self):
        if self.score > self.ini_score:
            with open(self.path, 'w') as f:
                f.write(str(self.score))

    def showScore(self):
        print(f'score: {self.score} \t record:{self.ini_score if self.ini_score > self.score else self.score}')


if __name__ == '__main__':
    score = Score()
    score.readHistory()
    score.showScore()
