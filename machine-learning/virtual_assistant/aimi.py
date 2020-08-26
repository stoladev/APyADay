from utils import debug
from modules.handlers import thread_handler

debug.activated = True


if __name__ == "__main__":
    try:
        thread_handler.run_threads()
    except (KeyboardInterrupt, SystemExit):
        raise
