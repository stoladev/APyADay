# Goal: Create a python script that prompts for a new file title upon creation.
# The script automatically creates the dated folder and opens vim within the
# newly created file.
file_title = ""


def auto_pyaday(file_title):
    # prompt user for file name
    # append .py to it ONLY IF it doesn't have that already
    # create the file with a ready-to-go template
    # template has a notes section and a code section
    return put_in_vim()


def put_in_vim():
    return "Putting you into the newly created file..."


print(auto_pyaday(file_title))
