from Point import Point


class PointUserVersion:

    # create a special type of point specifically for the board
    def __init__(self, alphaNum):

        # the coordinate of the board, inputted by user
        self.alphaNum = alphaNum

        # the alphabet to convert to integer
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                         "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # the y-coordinate of the point
        self.y = self.convertAlphaToInt()

        # the x-coordinate of the point
        self.x = int(alphaNum[:1])

    # converts the letter to designated integer on board
    def convertAlphaToInt(self):
        letter = self.alphaNum[1:2]
        num = self.alphabet.index(letter) + 1
        return num

    # creates a point with converted x and y coordinates
    def createPoint(self):
        point = Point(self.x, self.y)
        return point

    # return the x-coordinate of point
    def getX(self):
        return self.x

    # return the y-coordinate of point
    def getY(self):
        return self.y

