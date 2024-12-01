class InputReader:
    def __init__(self, filename):
        self.filename = filename

    def lines_as_str(self):
        """
        Read input as list of strings

        :return:
        """
        with open(self.filename) as f:
            input = f.readlines()
            # trim the newline character of each line
            input = [x.strip() for x in input]
        return input

    def lines_as_int(self):
        """
        Read input as list of integers

        :return:
        """
        return list(map(int, self.lines_as_str()))

    def lines_as_ints(self):
        """
        Read input as list of lists of integers

        :return:
        """
        return [list(map(int, x.split())) for x in self.lines_as_str()]
