def read_input(filename):
    """
    Read input as list of strings

    :param filename:
    :return:
    """

    with open(filename) as f:
        input = f.readlines()
        # trim the newline character of each line
        input = [x.strip() for x in input]
    return input

def read_input_as_int(filename):
    """
    Read input as list of integers

    :param filename:
    :return:
    """
    return list(map(int, read_input(filename)))