import os


file_ext = None
if os.name == 'nt':
    file_ext = '.exe'


TEST_DIR = os.path.dirname(os.path.abspath(__file__))

PROJ_DIR = os.path.dirname(TEST_DIR)

CHROME_DRIVER = PROJ_DIR + '/browsers/chromedriver' + file_ext