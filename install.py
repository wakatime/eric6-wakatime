# -*- coding: utf-8 -*-
"""
    WakaTime Eric6/Pymakr Installer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Downloads and installs the WakaTime Plugin for Eric6 and Pymakr.
    :copyright: (c) 2016 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import os
import platform
import sys
from ssl import SSLError
try:
    from urllib2 import urlopen, URLError
except ImportError:
    from urllib.request import urlopen
    from urllib.error import URLError


PY2 = (sys.version_info[0] == 2)
ROOT_URL = 'https://raw.githubusercontent.com/wakatime/eric6-wakatime/master/'
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIRS = []
if platform.system() == 'Windows':
    CONFIG_DIRS.append(os.path.join(os.path.expanduser('~'), '_pymakr', 'eric6plugins'))
    CONFIG_DIRS.append(os.path.join(os.path.expanduser('~'), '_eric6', 'eric6plugins'))
else:
    CONFIG_DIRS.append(os.path.join(os.path.expanduser('~'), '.pymakr', 'eric6plugins'))
    CONFIG_DIRS.append(os.path.join(os.path.expanduser('~'), '.eric6', 'eric6plugins'))
FILES = [
    'PluginWakaTime.py',
]


if PY2:
    import codecs
    open = codecs.open
    input = raw_input


def main():
    for filename in FILES:
        contents = get_file_contents(filename)
        if not contents:
            return 1
        for folder in CONFIG_DIRS:
            if os.path.exists(os.path.dirname(folder)):
                if not os.path.exists(folder):
                    os.mkdir(folder)
                save_file(os.path.join(folder, filename), contents)

    print('Installed. You may now restart Eric6/Pymakr.')
    if platform.system() == 'Windows':
        input('Press [Enter] to exit...')
    return 0


def get_file_contents(filename):
    """Get file contents from local clone or GitHub repo."""

    if os.path.exists(os.path.join(SRC_DIR, filename)):
        with open(os.path.join(SRC_DIR, filename), 'r', encoding='utf-8') as fh:
            return fh.read()
    else:
        url = ROOT_URL + filename
        try:
            resp = urlopen(url)
        except (SSLError, URLError) as e:
            if 'CERTIFICATE_VERIFY_FAILED' in str(e) and not PY2 and show_certs_message():
                return
            raise
        return resp.read() if PY2 else resp.read().decode('utf-8')


def show_certs_message():
    """Show Install Certificates command so Python can make SSL requests."""

    major, minor, patch = sys.version_info[0], sys.version_info[1], sys.version_info[2]
    script = 'Install Certificates.command'
    folder = os.path.join('/Applications/Python {major}.{minor}'.format(
        major=major,
        minor=minor,
    ))
    if not os.path.exists(os.path.join(folder, script)):
        folder = os.path.join('/Applications/Python {major}.{minor}.{patch}'.format(
            major=major,
            minor=minor,
            patch=patch,
        ))

    if os.path.exists(os.path.join(folder, script)):
        print('Please run this command:')
        print(os.path.join(folder, script).replace(' ', '\\ '))
        print('Then re-run this script.')
        return True
    return False


def save_file(filename, contents):
    """Saves contents to filename."""

    with open(filename, 'w', encoding='utf-8') as fh:
        fh.write(contents)


if __name__ == '__main__':
    sys.exit(main())
