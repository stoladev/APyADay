"""
Creates an automatic directory and file from a template for the APyADay
challenge.
"""

# TODO: Allow user to call script and input their own args.


import errno
import os
from datetime import datetime


env_path = os.getenv('XDG_APYADAY_HOME')
month_year = datetime.now().strftime('%m-%Y/')
month_day_year = datetime.now().strftime('%m-%d-%Y')
dir_path = month_year + month_day_year


TEMPLATE = """\"\"\"

\"\"\"
"""


def filecreation(content, filename):
    """filecreation.

    Args:
        content: String inserted into the created file.
        filename: Name of created file.
    """

    mydir = os.path.join(env_path, dir_path)

    try:
        os.makedirs(mydir)
        print('Success making dir')
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
    with open(os.path.join(mydir, filename), 'w') as apyaday_entry:
        apyaday_entry.writelines(content)
        print('Success writing lines')


filecreation(TEMPLATE, 'entry.py')
