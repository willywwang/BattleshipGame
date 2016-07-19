from Point import Point


class Ship:

    # creates a ship with given length, orientation, and initial x, y coordinates
    def __init__(self, size, orientation, x, y):

        # the length of the ship
        self.size = size

        # the orientation of the ship
        self.orientation = orientation

        # the initial x-coordinate of the ship
        self.x = x

        # the initial y-coordinate of the ship
        self.y = y

        # the points that the ship is on
        self.coordinates = []

    # creates a ship and inserts points into list
    def createShip(self):
        if self.orientation == "horizontal":
            if self.x + self.size <= 10:
                self.coordinates.append(Point(self.x, self.y))
                for x in range(1, self.size):
                    self.coordinates.append(Point(self.x + x, self.y))

            elif self.x - self.size + 1 >= 1:
                startPoint = self.x - self.size + 1
                for x in range(0, self.size):
                    self.coordinates.append(Point(startPoint + x, self.y))
            else:
                print("Ship cannot be created")

        elif self.orientation == "vertical":
            if self.y + self.size <= 10:
                self.coordinates.append(Point(self.x, self.y))
                for y in range(1, self.size):
                    self.coordinates.append(Point(self.x, self.y + y))

            elif self.y - self.size + 1 >= 1:
                startPoint = self.y - self.size + 1
                for y in range(0, self.size):
                    self.coordinates.append(Point(self.x, startPoint + y))

            else:
                print("Ship cannot be created.")
        else:
            print("Invalid orientation, please input horizontal or vertical.")

    # returns the points that the ship is on
    def getCoordinates(self):
        return self.coordinates
