activated = None


def log(message):
    if activated:
        print(message)
