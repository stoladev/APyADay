from modules.handlers import thread_handler
from utils import debug

debug.activated = True


if __name__ == "__main__":
    try:
        thread_handler.run_threads()
    except (KeyboardInterrupt, SystemExit):
        raise
