from random import randint
from PointUserVersion import PointUserVersion
from Point import Point
from Board import Board
from Ship import Ship


class Game:
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

        # points that the opponent has shot at
        self.opponentShots = []

        # coordinates of opponent ship of size 2
        self.ship_2 = None

        # coordinates of opponent ship of size 3
        self.ship_3 = None

        # coordinates of opponent ship of size 4
        self.ship_4 = None

        # coordinates of opponent ship of size 5
        self.ship_5 = None

        # coordinates of user's ship of size 2
        self.userShip_2 = None

        # coordinates of user's ship of size 3
        self.userShip_3 = None

        # coordinates of user's ship of size 4
        self.userShip_4 = None

        # coordinates of user's ship of size 5
        self.userShip_5 = None

        # boolean to see if point is occupied by ship
        self.find = False

        # current x-position of user input
        self.x = 0

        # current y-position of user input
        self.y = 0

        # users occupied ships
        self.ownOccupied = []

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

    def generateOwnShips(self):
        num = 0
        while num < 4:
            self.find = False
            orientation = self.determineOrientation()
            size = num + 2
            x = randint(1, 9)
            y = randint(1, 9)
            ship = Ship(size, orientation, x, y)
            ship.createShip()
            coord = ship.getCoordinates()

            for point in coord:
                for occupied in self.ownOccupied:
                    if point == occupied:
                        self.find = True
                        break

                if self.find:
                    break

            if self.find:
                continue

            if size == 2:
                self.userShip_2 = ship.getCoordinates()

            elif size == 3:
                self.userShip_3 = ship.getCoordinates()

            elif size == 4:
                self.userShip_4 = ship.getCoordinates()

            else:
                self.userShip_5 = ship.getCoordinates()

            num += 1
            for point in coord:
                self.ownOccupied.append(point)

    # generate opponent's ships, prevents overlapping of ships
    # generates one - two length ship, one - three length ship, and
    # one - four length ship,
    def generateShips(self):
        num = 0
        while num < 4:
            self.find = False
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
                        self.find = True
                        break

                if self.find:
                    break

            if self.find:
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

    # determines if point is occupied by a opponent's ship
    def occupiedContains(self):
        for occupied in self.occupied:
            if self.point == occupied:
                return True

            elif occupied == self.occupied[len(self.occupied) - 1]:
                return False

            else:
                continue
    # TODO: use in code
    # determines if point is occupied by a user's ship
    def userOccupiedContains(self):
        for occupied in self.ownOccupied:
            if self.point == occupied:
                return True

            elif occupied == self.ownOccupied[len(self.ownOccupied) - 1]:
                return False

            else:
                continue

    # determines if the player has taken a shot at the given point
    def shotContains(self):
        for point in self.shots:
            if self.point == point:
                return True

            elif point == self.shots[len(self.shots) - 1]:
                return False

            else:
                continue

    # TODO: use in code
    # determine if the opponent has taken a shot at the given point
    def opponentShotContains(self):
        for point in self.opponentShots:
            if self.point == point:
                return True

            elif point == self.opponentShots[len(self.opponentShots) - 1]:
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

    # TODO: use in code
    # determines which ship contains the point
    def ownShipContains(self):
        for point1 in self.userShip_2:
            if self.point == point1:
                return self.userShip_2

        for point2 in self.userShip_3:
            if self.point == point2:
                return self.userShip_3

        for point3 in self.userShip_4:
            if self.point == point3:
                return self.userShip_4

        for point4 in self.userShip_5:
            if self.point == point4:
                return self.userShip_5

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
                    self.x = int(pointUV.getX())
                    self.y = int(pointUV.getY())
                    if self.shotContains():
                        print("Shot taken at given point, try again.")
                        continue
                    else:
                        self.board.changeSpotToX(self.x, self.y)
                        self.shots.append(self.point)
                        self.noInput = False

            else:
                print("Invalid input. Please enter a point (ie. 3A).")
                continue

    # TODO: implement method
    def opponentAIPointChooser(self):
        self.point = None
        self.x = randint(1, 9)
        self.y = randint(1, 9)

    # determines if all of opponents ships are down
    def isUserWin(self):
        if not self.occupied:
            return True

        else:
            return False

    # TODO: use in code
    def isUserLose(self):
        if not self.ownOccupied:
            return True

        else:
            return False

    # determines if user wishes to play new game
    def newGame(self):
        userInput = input("Press Y if you want to play again. N if you don't: ").upper()    

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

    # TODO: delete after
    def printOccupied(self):
        for occupied in self.occupied:
            occupied.printPoint()

    # create and play the battleship game
    def playGame(self):
        self.gameStatus = True
        print("Game Start!")
        self.generateShips()
        self.generateOwnShips()
        self.board.createBoard()
        self.printOccupied()

        while self.gameStatus:
            self.printTurn()
            self.board.printBoard()
            self.userPointInput()

            if self.occupiedContains():
                self.board.changeSpotIfHit(self.x, self.y)
                print("You hit the ship!")
                self.occupied.remove(self.point)
                self.turn += 1
                ship = self.shipContains()
                ship.remove(self.point)

                if not ship:
                    print("Ship down!")

                if self.isGUserWin():
                    print("You won!")
                    self.newGame()
            else:
                print("You missed!")
                self.turn += 1


game = Game(10, 10)
game.playGame()
