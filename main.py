# Milli Machine
class main(object):
    def __init__(self):
        self.status = 'A'

    def warp(self):
        match self.status:
            case 'A':
                self.status = 'B'
                return 0
            case 'C':
                self.status = 'F'
                return 5
            case 'E':
                self.status = 'F'
                return 7
            case 'F':
                self.status = 'G'
                return 8
            case 'G':
                self.status = 'H'
                return 10
            case _:
                raise KeyError

    def cut(self):
        match self.status:
            case 'B':
                self.status = 'C'
                return 1
            case 'C':
                self.status = 'D'
                return 3
            case 'D':
                self.status = 'E'
                return 6
            case _:
                raise KeyError

    def stare(self):
        match self.status:
            case 'B':
                self.status = 'F'
                return 2
            case 'C':
                self.status = 'E'
                return 4
            case 'F':
                self.status = 'D'
                return 9
            case 'H':
                self.status = 'F'
                return 11
            case _:
                raise KeyError
