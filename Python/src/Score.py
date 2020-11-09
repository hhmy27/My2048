class Score:
    def __init__(self):
        self.record_score = None
        self.cur_score = None
        self.path = '../history/score'
        self.readHistory()

    def readHistory(self):
        with open(self.path, 'r') as f:
            record = f.read()
            self.record_score = 0 if record == '' else int(record, 10)
            self.cur_score = 0

    def writeScore(self):
        if self.record_score > self.cur_score:
            with open(self.path, 'w') as f:
                f.write(str(self.record_score))

    def showScore(self):
        print(f'score: {self.cur_score} \t record: {self.record_score}')


if __name__ == '__main__':
    score = Score()
    score.readHistory()
    score.showScore()
