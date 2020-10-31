class InputFlow:

    def getKey(self):
        direction = [0, 1, 2, 3]
        key = input()
        if key == 'w':
            return direction[0]
        elif key == 's':
            return direction[1]
        elif key == 'a':
            return direction[2]
        elif key == 'd':
            return direction[3]
        else:
            return None


if __name__ == '__main__':
    cin = InputFlow()
    cin.getKey()
