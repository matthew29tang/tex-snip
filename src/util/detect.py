import sys, os, json
import pyperclip, cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from . import mathpix
from . import snipping_tool as snipper


def ocrClient():
    return _ocr("./capture.png", True)


def ocrServer(filename):
    return _ocr(filename, False)


def _ocr(filename, isClient):
    r = mathpix.latex(
        {
            "src": mathpix.image_uri(filename),
            "ocr": ["math", "text"],
            "formats": ["text"],
            "format_options": {
                "text": {
                    "transforms": ["rm_spaces", "rm_newlines"],
                    "math_delims": ["$", "$"],
                }
            },
        },
        isClient,
    )
    # print(json.dumps(r, indent=4, sort_keys=True))
    if isClient:
        if "text" not in r:
            print("No math found")
            pyperclip.copy("")
        else:
            print(r["text"])
            print("\n")
            pyperclip.copy(r["text"])
    else:
        print("Success: " + filename)

    try:
        os.remove(filename)
        return r["text"]
    except:
        print("Error removing file.")
        return "Error"


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = snipper.MyWidget(ocrClient)
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.exec_()


if __name__ == "__main__":
    run()
