from enum import Enum


class Matrix:
    """
    Class to represent a matrix
    """

    def __init__(self, matrix):
        """
        Constructor

        :param matrix:
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def get_value(self, x, y):
        """
        Get value at position

        :param x:
        :param y:
        :return:
        """
        return self.matrix[y][x]

    def get_lines(self):
        """
        Get lines

        :return:
        """
        return self.matrix

    def __str__(self):
        return "\n".join(["".join(row) for row in self.matrix])


class Direction(Enum):
    """
    Enum for directions
    """
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8


class MatrixNavigator:
    """
    Class to navigate a matrix
    """

    def __init__(self, matrix: Matrix, x=0, y=0):
        """
        Constructor

        :param matrix:
        :param x:
        :param y:
        """
        self.matrix = matrix
        self.current_position = (x, y)

    def move(self, direction: Direction) -> bool:
        """
        Move in a direction

        :param direction:
        :return:
        """
        x, y = self.current_position
        if direction == Direction.UP and y > 0:
            self.current_position = (x, y - 1)
        elif direction == Direction.DOWN and y < self.matrix.rows - 1:
            self.current_position = (x, y + 1)
        elif direction == Direction.LEFT and x > 0:
            self.current_position = (x - 1, y)
        elif direction == Direction.RIGHT and x < self.matrix.cols - 1:
            self.current_position = (x + 1, y)
        elif direction == Direction.UP_LEFT and x > 0 and y > 0:
            self.current_position = (x - 1, y - 1)
        elif direction == Direction.DOWN_LEFT and x > 0 and y < self.matrix.rows - 1:
            self.current_position = (x - 1, y + 1)
        elif direction == Direction.UP_RIGHT and x < self.matrix.cols - 1 and y > 0:
            self.current_position = (x + 1, y - 1)
        elif direction == Direction.DOWN_RIGHT and x < self.matrix.cols - 1 and y < self.matrix.rows - 1:
            self.current_position = (x + 1, y + 1)
        else:
            return False
        return True

    def get_position(self):
        """
        Get current position

        :return:
        """
        return self.current_position

    def get_value(self):
        """
        Get value at current position

        :return:
        """
        x, y = self.current_position
        return self.matrix.get_value(x, y)

    def peek_value(self, direction: Direction) -> (bool, str):
        """
        Peek value in a direction

        :param direction:
        :return:
        """
        start = self.current_position
        ok = self.move(direction)
        value = self.get_value()
        self.current_position = start
        return ok, value

    def set_position(self, x, y):
        """
        Set current position

        :param x:
        :param y:
        :return:
        """
        if 0 <= x < self.matrix.rows and 0 <= y < self.matrix.cols:
            self.current_position = (x, y)
        else:
            raise ValueError("Position out of bounds")
