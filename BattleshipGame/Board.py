class Board:

    # creates a board with given number of rows and columns
    def __init__(self, numRow, numCol):

        # number of rows on board
        self.numRow = numRow

        # number of columns on board
        self.numCol = numCol

        # the board to be displayed on console
        self.board = []

        # alphabet to label top row of board
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                         "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                         "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # create the board to be displayed including labels
    #  for leftmost column and topmost row
    def createBoard(self):
        self.board = []
        for x in range(self.numRow):
            self.board.append(["O"] * self.numCol)

        for x in range(0, self.numRow):
            self.board[x][0] = str(x)
            if x >= self.numRow - 1:
                self.board[x][0] = str(x)

        for y in range(1, self.numCol):
            self.board[0][y] = self.alphabet[y - 1]

    # change a spot to be marked X if user chooses point
    def changeSpotToX(self, x, y):
        self.board[x][y] = "X"

    # change a spot back to O if by off-chance an error occurs
    def changeSpotToO(self, x, y):
        self.board[x][y] = "O"

    # print the board to console
    def printBoard(self):
        for row in self.board:
            print(" ".join(row))
