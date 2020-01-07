from PyQt5 import QtCore
from pynput.keyboard import Key

try:
    import credentials
except:
    raise Exception('CUSTOM ERROR: src/credentials.py not found. See the README for instructions.')

class Config:
    # API credentials - See README for how to generate
    APP_ID = credentials.APP_ID
    APP_KEY = credentials.APP_KEY
    VERBOSE = False

    # snipping_tool
    escapeScreenshot = QtCore.Qt.Key_Escape

    # imgLatex
    terminate = Key.scroll_lock
    combo = set([str(Key.alt_l), "p"]) # Elements must be string