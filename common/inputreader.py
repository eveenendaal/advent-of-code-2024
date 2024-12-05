from aocd.models import Puzzle
from bs4 import BeautifulSoup

from common.matrix import Matrix


class InputReader:
    """
    Class to read input from file
    """

    def __init__(self, input_source: str):
        self.input_data = input_source.splitlines()

    def lines_as_str(self) -> list:
        """
        Read input as list of strings

        :return:
        """
        return self.input_data

    def as_str(self) -> str:
        """
        Read input as list of strings

        :return:
        """
        return "".join(self.input_data)

    def lines_as_int(self) -> list:
        """
        Read input as list of integers

        :return:
        """
        return list(map(int, self.input_data))

    def lines_as_ints(self) -> list:
        """
        Read input as list of lists of integers

        :return:
        """
        return [list(map(int, x.split())) for x in self.input_data]

    def matrix(self) -> Matrix:
        """
        Read input as matrix

        :return:
        """
        return Matrix([list(x) for x in self.input_data])


class PuzzleWrapper:
    """
    Class to wrap the puzzle
    """

    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle

    def get_code_blocks(self, min_length) -> list:
        files = [
            self.puzzle.prose0_path,
            self.puzzle.prose1_path,
            self.puzzle.prose2_path
        ]

        output = []

        for file in files:
            # read files if they exist
            if file.is_file():
                text = file.read_text()
                soup = BeautifulSoup(text, features="html.parser")
                for code in soup.find_all("code"):
                    text = []
                    for content in code.contents:
                        text.append(content.get_text())
                    text = "".join(text)
                    if len(text) >= min_length:
                        output.append(text)

        return output

    def get_code_block(self, block_number: int, min_length=30) -> str:
        return self.get_code_blocks(min_length)[block_number]
