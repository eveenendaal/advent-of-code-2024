import copy
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8


class MatrixNavigator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        self.current_position = (0, 0)

    def move(self, direction: Direction) -> bool:
        x, y = self.current_position
        if direction == Direction.UP and x > 0:
            self.current_position = (x - 1, y)
        elif direction == Direction.DOWN and x < self.rows - 1:
            self.current_position = (x + 1, y)
        elif direction == Direction.LEFT and y > 0:
            self.current_position = (x, y - 1)
        elif direction == Direction.RIGHT and y < self.cols - 1:
            self.current_position = (x, y + 1)
        elif direction == Direction.UP_LEFT and x > 0 and y > 0:
            self.current_position = (x - 1, y - 1)
        elif direction == Direction.UP_RIGHT and x > 0 and y < self.cols - 1:
            self.current_position = (x - 1, y + 1)
        elif direction == Direction.DOWN_LEFT and x < self.rows - 1 and y > 0:
            self.current_position = (x + 1, y - 1)
        elif direction == Direction.DOWN_RIGHT and x < self.rows - 1 and y < self.cols - 1:
            self.current_position = (x + 1, y + 1)
        else:
            return False
        return True

    def get_position(self):
        return self.current_position

    def get_value(self):
        x, y = self.current_position
        return self.matrix[y][x]

    def peek_value(self, direction: Direction) -> (bool, str):
        start = self.current_position
        ok = self.move(direction)
        value = self.get_value()
        self.current_position = start
        return ok, value

    def set_position(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            self.current_position = (x, y)
        else:
            raise ValueError("Position out of bounds")

    def get_lines(self):
        return self.matrix
