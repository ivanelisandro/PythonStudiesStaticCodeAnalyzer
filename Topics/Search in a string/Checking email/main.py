import re


def check_email(string):
    pattern = r"^[\w\.]+@\w+\.\w+$"
    return bool(re.match(pattern, string))
