
import os
from github import Github


try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def __read_creds(creds_directory, creds_filename):
    with open(creds_directory + creds_filename) as in_file:
        creds = in_file.read()
        parts = creds.split(',')
        return parts[0], parts[1]


def __write_creds(creds_directory, creds_filename, username, password):
    with open(creds_directory + creds_filename, 'w') as out_file:
        creds = "{},{}".format(username, password)
        out_file.write(creds)


def init(creds_filename, username=None, password=None, creds_directory='.Credentials'):
    creds_directory = creds_directory or ''
    if creds_directory and (creds_directory[-1] != os.sep):
        creds_directory += os.sep
    if creds_directory not in ('', '.'):
        if not os.path.exists(creds_directory):
            os.mkdir(creds_directory)
    if not username:
        if os.path.exists(creds_directory + creds_filename):
            username, password = __read_creds(creds_directory, creds_filename)
        else:
            return None
    else:
        if os.path.exists(creds_directory + creds_filename):
            os.remove(creds_directory + creds_filename)
        __write_creds(creds_directory, creds_filename, username, password)
    gh = Github(username, password)
    return gh


def get_username():
    """
    Prompt for and get the username.
    This method is provided so that a consistent prompt is always used.
    """
    return raw_input('Enter Github Username:').strip()


def get_password():
    """
    Prompt for and get the password.
    This method is provided so that a consistent prompt is always used.
    """
    return raw_input('Enter Github Password:').strip()


def get_creds_filename():
    """
    Prompt for and get the creds filename.
    This method is provided so that a consistent prompt is always used.
    """
    return raw_input('Enter Github Credentials Filename:').strip()


if __name__ == '__main__':


    gh = init(get_creds_filename(), get_username(), get_password)
