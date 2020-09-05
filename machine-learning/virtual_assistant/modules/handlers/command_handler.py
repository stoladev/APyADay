from playsound import playsound
from commands import open_command
from modules.handlers import thread_handler


def check_cmnd(command):
    """
    Checks the commands that are registered after grabbing input once the hotkey is pressed.

    Procedure:
    Searches through the command using regex.
    Runs through commands that are currently limited to if statements.

    Still needed:
    Transfer checks to use machine learning.
    Sync training_data between app and cloud.
    """

    # while True:
    #     command = input("Command: ")
    #     if command.lower() == "quit":
    #         thread_handler.stop_threads()
    #         break
    #
    #     results = model.predict([bag_of_words(command, word_list)])
    #     print(results)

    # else:
    playsound("audio/cmnd_not_recognized_audio.mp3")
