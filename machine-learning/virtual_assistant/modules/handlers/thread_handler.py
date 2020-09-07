import concurrent.futures
import playsound
import os
from modules.listeners import microphone_listener
from modules.listeners import keyboard_listener

from modules.rnn.rnn_tools import rnn_evaluator


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
        threads.append(executor.submit(playsound, "audio/start_audio.mp3"))
        # threads.append(executor.submit(rnn_evaluator.converse))
        threads.append(executor.submit(microphone_listener.microphone_input))
        threads.append(executor.submit(keyboard_listener.keyboard_input))


def stop_threads():
    os._exit(0)
