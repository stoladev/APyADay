"""Automated creation process for APyADay."""


# Goal: Create a python script that prompts for a new file title upon creation.
# The script automatically creates the dated folder and opens vim within the
# newly created file.


file_title = input()


def auto_pyaday():
    """Automatically creates the dated folder and titled file, which is
    automatically formatted appropriately."""
    # prompt user for file name
    # append .py to it ONLY IF it doesn't have that already
    # create the file with a ready-to-go template
    # template has a notes section and a code section
    print("What would you like to call the file?")
    input("File name: ")
    return put_in_vim()


def put_in_vim():
    """Puts the user into the vim instance."""
    return "Putting you into the newly created file..."


auto_pyaday()
