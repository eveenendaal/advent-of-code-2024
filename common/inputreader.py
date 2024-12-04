from common.matrix import MatrixNavigator


class InputReader:
    """
    Class to read input from file
    """

    def __init__(self, input_source):
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

    def matrix(self) -> MatrixNavigator:
        """
        Read input as grid

        :return:
        """
        return MatrixNavigator([list(x) for x in self.input_data])
