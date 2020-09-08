from playsound import playsound

from modules.handlers.data_handler.data_cleaner import voc
from modules.rnn.rnn_tools.rnn_decoder import SearchDecoder
from modules.rnn.rnn_tools.rnn_evaluator import check_input
from modules.rnn.rnn_trainer.rnn_loader import encoder, decoder


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

    encoder.eval()
    decoder.eval()

    # Initialize search module
    searcher = SearchDecoder(encoder, decoder)

    # Begin chatting (uncomment and run the following line to begin)
    check_input(searcher, voc, command)

    # else:
    playsound("audio/cmnd_not_recognized_audio.mp3")
