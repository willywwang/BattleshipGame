class Point:

    # creates a point with given x, y coordinate
    def __init__(self, x, y):

        # the x-coordinate of the point
        self.x = x

        # the y-coordinate of the point
        self.y = y

    # overloaded equal, two points are only equal if
    # y-coordinate and x-coordinate are the same.
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # TODO: delete after
    def printPoint(self):
        print(self.x, self.y)

    # return the x-coordinate of the point
    def getX(self):
        return self.x

    # return the y-coordinate of the point
    def getY(self):
        return self.y
