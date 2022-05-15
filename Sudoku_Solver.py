Sudoku =[[ 1 , 4, 3,  0 , 8, 0, 2, 5, 0],
       [ 6 , 0, 0,  0 , 0, 0, 0, 0, 0],
       [ 0 , 0, 0,  0 , 0, 1, 0, 9, 4],
       [ 9 , 0, 0,  0 , 0, 4, 0, 7, 0],
       [ 0 , 0, 0,  6 , 0, 8, 0, 0, 0],
       [ 0 , 1, 0,  2 , 0, 0, 0, 0, 3],
       [ 8 , 2, 0,  5 , 0, 0, 0, 0, 0],
       [ 0 , 0, 0,  0 , 0, 0, 0, 0, 5],
       [ 5 , 3, 4,  8 , 9, 0, 7, 1, 0]]

#print(board[1][0]) = 6 -> Y / X
class Board:
    def __init__(self, _inputBoard):
        self.board = _inputBoard

    def getRow(self, _Yin):
        return self.board[_Yin]

    def getColum(self, _Xin):
        colum = []
        for row in self.board:
            colum.append(row[_Xin])
        return colum

    def getValue (self, point):
        return (self.board[point.getY()][point.getX()])

    def getValue (self, _Xin, _Yin):
        return (self.board[_Yin][_Xin])

    def check(self, point, value):
        #Check Row
        X = point.getX()
        Y = point.getY()

        for i in range(len(self.board[0])):
            if ( self.board[Y][i] == value and X != i):
                return False

        #Check Colum
        for i in range(len(self.board)):
            if ( self.board[i][X] == value and Y != i):
                return False

        #Check Box -> Box coordinates 
        box_x = X // 3
        box_y = Y //3

        for i in range(box_y*3, box_y*3 +3):
            for j in range(box_x*3, box_x*3 +3):
                if self.board[i][j] == value and (i,j) != (Y,X):
                    return False

        return True


    def set(self, point, value):
        self.board[point.getY()][point.getX()] = value

class Point:
    def __init__ (self, _Xin, _Yin):
        self.x = _Xin
        self.y = _Yin

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def findCero(_inputBoard):
    for i in range( len( _inputBoard.getRow(0) ) ):
        for j in range(len(_inputBoard.getRow(i))):
            if (_inputBoard.getRow(i)[j] == 0):
                return_point = Point(j,i)
                return (return_point)
    return None


myBoard = Board(Sudoku)

def solveSudoku(Sudoku):

    point = findCero(Sudoku)
    if not point:
        return True
    else:
        for i in range(1,10):
            if Sudoku.check(point, i):
                Sudoku.set(point, i)

                if solveSudoku(Sudoku):
                    return True

                Sudoku.set(point, 0)


def fancyPrint(Sudoku):
    for i in range(len(myBoard.getRow(0))):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")

        row = myBoard.getRow(i)
        print(row)

        





print("Unsolved Sudoku:")
fancyPrint(myBoard)
solveSudoku(myBoard)

print("")
print("Solved Sudoku:")
fancyPrint(myBoard)
