from commands import open_command


def main(command):
    if open_command.check(command):
        return True
