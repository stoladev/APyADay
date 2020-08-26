from playsound import playsound
from modules.listeners.microphone_listener import microphone_input
from modules.listeners.keyboard_listener import keyboard_input
import concurrent.futures
import os

threads = []


def run_threads():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        threads.append(executor.submit(playsound, "audio/start_audio.mp3"))
        threads.append(executor.submit(microphone_input))
        threads.append(executor.submit(keyboard_input))


def stop_threads():
    print("Exiting program...")
    os._exit(0)
