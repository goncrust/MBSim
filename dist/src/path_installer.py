import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_appdata_path(resource_path=None):
    appdata = os.getenv('APPDATA')

    if not os.path.exists(appdata + '/mbsim'):
        os.makedirs(appdata + '/mbsim')

    if resource_path == None:
        return (appdata + '/mbsim')
    else:
        return (appdata + '/mbsim/' + resource_path)
