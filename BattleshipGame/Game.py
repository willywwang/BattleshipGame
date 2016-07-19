from random import randint
from PointUserVersion import PointUserVersion
from Point import Point
from Board import Board
from Ship import Ship


class Game():
    # creates a game with given number of rows and columns (max ten rows)
    def __init__(self, numRow, numColumn):

        # the number of rows on the board
        self.numRow = numRow

        # the number of columns on the board
        self.numCol = numColumn

        # the board for the game to be played on
        self.board = Board(numRow, numColumn)

        # the opponents ships to be targeted
        self.ships = []

        # the points currently being occupied by opponent
        self.occupied = []

        # the current turn of the game, initialized at turn 1
        self.turn = 1

        # the current status of the game
        self.gameStatus = False

        # the possible coordinates for the topmost row
        self.possibleLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

        # determines if a user has not inputted an input
        self.noInput = True

        # resets the users point input
        self.userInput = ""

        # resets current point
        self.point = None

        # points that the player has shot at
        self.shots = []

        # coordinates of ship of size 2
        self.ship_2 = None

        # coordinates of ship of size 3
        self.ship_3 = None

        # coordinates of ship of size 4
        self.ship_4 = None

        # coordinates of ship of size 5
        self.ship_5 = None

    # creates a random orientation for ship
    def determineOrientation(self):
        num = randint(0, 1)
        if num == 0:
            return "horizontal"
        else:
            return "vertical"

    # generate opponent's ships, prevents overlapping of ships
    # generates one - two length ship, one - three length ship, and
    # one - four length ship,
    def generateShips(self):
        num = 0
        while num < 4:
            orientation = self.determineOrientation()
            size = num + 2
            x = randint(1, 9)
            y = randint(1, 9)
            ship = Ship(size, orientation, x, y)
            ship.createShip()
            coord = ship.getCoordinates()

            for point in coord:
                for occupied in self.occupied:
                    if point == occupied:
                        continue

            if size == 2:
                self.ship_2 = ship.getCoordinates()

            elif size == 3:
                self.ship_3 = ship.getCoordinates()

            elif size == 4:
                self.ship_4 = ship.getCoordinates()

            else:
                self.ship_5 = ship.getCoordinates()

            num += 1
            for point in coord:
                self.occupied.append(point)

    # determines if point is occupied by a ship
    def occupiedContains(self):
        for occupied in self.occupied:
            if self.point == occupied:
                return True

            elif occupied == self.occupied[len(self.occupied) - 1]:
                return False

            else:
                continue

    #  determines if the player has taken a shot at the given point
    def shotContains(self):
        for point in self.shots:
            if self.point == point:
                return True

            elif point == self.shots[len(self.shots) - 1]:
                return False

            else:
                continue

    # determines which ship contains the point
    def shipContains(self):
        for point1 in self.ship_2:
            if self.point == point1:
                return self.ship_2

        for point2 in self.ship_3:
            if self.point == point2:
                return self.ship_3

        for point3 in self.ship_4:
            if self.point == point3:
                return self.ship_4

        for point4 in self.ship_5:
            if self.point == point4:
                return self.ship_5

    # prints the current turn to console
    def printTurn(self):
        print("Turn", self.turn)

    # gathers user input for point and determines if point is valid
    def userPointInput(self):
        self.noInput = True
        self.point = None
        while self.noInput:
            self.userInput = ""
            self.userInput = input("Enter a point: ")

            if self.userInput[:1].isdigit() and self.userInput[1:2].isalpha():
                num = int(self.userInput[:1])
                alpha = self.userInput[1:2].upper()

                if len(self.userInput) != 2:
                    print("Invalid input. Please enter a point (ie. 3A).")
                    continue

                elif num == 0:
                    print("Invalid input. Please enter a point (ie. 3A).")
                    continue

                elif alpha not in self.possibleLetters:
                    print("Invalid input. Please enter a point (ie. 3A).")
                    continue

                else:
                    pointUV = PointUserVersion(self.userInput)
                    self.point = Point(pointUV.getX(), pointUV.getY())
                    x = int(pointUV.getX())
                    y = int(pointUV.getY())
                    if self.shotContains():
                        print("Shot taken at given point, try again.")
                        continue
                    else:
                        self.board.changeSpotToX(x, y)
                        self.shots.append(self.point)
                        self.noInput = False

            else:
                print("Invalid input. Please enter a point (ie. 3A).")
                continue

    # determines if all of opponents ships are down
    def isGameOver(self):
        if not self.occupied:
            return True

        else:
            return False

    # determines if user wishes to play new game
    def newGame(self):
        userInput = input("Press Y if you want to play again. N if you don't: ")

        if userInput == "Y":
            self.board = Board(self.numRow, self.numCol)
            self.ships = []
            self.occupied = []
            self.turn = 1
            self.gameStatus = False
            self.possibleLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
            self.noInput = True
            self.userInput = ""
            self.point = None

            self.playGame()

        elif userInput == "N":
            self.gameStatus = False
            print("Good game!")

        else:
            print("Invalid character entered.")
            self.newGame()

    def printOccupied(self):
        for occupied in self.occupied:
            occupied.printPoint()

    # create and play the battleship game
    def playGame(self):
        self.gameStatus = True
        print("Game Start!")
        self.generateShips()
        self.board.createBoard()
        self.printOccupied()
        while self.gameStatus:
            self.printTurn()
            self.board.printBoard()
            self.userPointInput()
            if self.occupiedContains():
                print("You hit the ship!")
                self.occupied.remove(self.point)
                self.turn += 1
                ship = self.shipContains()
                ship.remove(self.point)

                if not ship:
                    print("Ship down!")

                if self.isGameOver():
                    print("You won!")
                    self.newGame()
            else:
                print("You missed!")
                self.turn += 1


game = Game(10, 10)
game.playGame()
