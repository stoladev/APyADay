import concurrent.futures
import os

from modules.rnn.rnn_tools.rnn_evaluator import converse

threads = []


def run_threads():
    """
    Runs the main threads for the program.

    Threads:
    Starting welcome audio
    Microphone listener
    Keyboard listener
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        converse()
        # threads.append(executor.submit(playsound, "audio/start_audio.mp3"))
        # threads.append(executor.submit(microphone_input))
        # threads.append(executor.submit(keyboard_input))


def stop_threads():
    os._exit(0)
