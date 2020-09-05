activated = None


def log(message):
    if activated:
        print(message)


def log_lines(file_to_print, quantity=10):
    """
    Prints x (default is 10) lines from the provided file.

    :param file_to_print: The file used to grab and print lines from.
    :param quantity: The quantity of lines to print out (default is 10).
    """

    with open(file_to_print, "rb") as datafile:
        lines = datafile.readlines()
    for line in lines[:quantity]:
        print(line)
