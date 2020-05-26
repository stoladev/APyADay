"""
Creates an automatic directory for the APyADay challenge.
"""

import subprocess
import sys
import errno
import os
from datetime import datetime

# Args passed from terminal
template_arg = sys.argv[1]
filename_arg = sys.argv[2]

env_path = os.getenv('XDG_APYADAY_HOME')
month_year = datetime.now().strftime('%m-%Y/')
month_day_year = datetime.now().strftime('%m-%d-%Y')
date_path = month_year + month_day_year
folder_path = os.path.join(env_path, date_path)
file_path = folder_path + '/' + filename_arg
shell_command = os.environ.get('EDITOR', 'vim') + ' ' + file_path


D_TEMPLATE = """\"\"\"
file_docstring_here
\"\"\"
"""


def file_creation(template=template_arg, filename=filename_arg):
    """file_creation.
    Args are passed through terminal command when called.

    Args:
        content: Which template to use for the new file.
        filename: What the file name will be.
    """

    try:
        os.makedirs(folder_path)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
    with open(os.path.join(folder_path, filename), 'w') as apyaday_entry:
        if template_arg == "default":
            template = D_TEMPLATE
        apyaday_entry.writelines(template)


def open_file_choice():
    """open_file_choice.
    Gives the user the choice to open the newly created file with Vim.
    """
    open_option = input("Do you want to open this file? (y/n): ")
    if open_option == 'y':
        print('Opening file...')
        subprocess.call(shell_command, shell=True)


if __name__ == "__main__":
    file_creation()
    print('File \"' + filename_arg + '\" created at:')
    print(file_path)
    open_file_choice()
