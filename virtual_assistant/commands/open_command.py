import re
import webbrowser


def check(command):
    if "open" in command:

        reg_ex = re.search("open (.+)", command)

        if reg_ex:
            domain = reg_ex.group(1)

            if "." not in domain:
                domain += ".com"

            url = "https://www." + domain

            webbrowser.open(url)
        return True
    else:
        return False
