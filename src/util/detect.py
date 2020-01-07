import sys, os, json
import pyperclip, cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from . import mathpix
from . import snipping_tool as snipper


def ocr():
    r = mathpix.latex(
        {
            "src": mathpix.image_uri("./capture.png"),
            "ocr": ["math", "text"],
            "formats": ["text"],
            "format_options": {
                "text": {
                    "transforms": ["rm_spaces", "rm_newlines"],
                    "math_delims": ["$", "$"],
                }
            },
        }
    )
    # print(json.dumps(r, indent=4, sort_keys=True))
    if "text" not in r:
        print("No math found")
        pyperclip.copy("")
    else:
        print(r["text"])
        print("\n")
        pyperclip.copy(r["text"])

    try:
        os.remove("./capture.png")
    except:
        pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = snipper.MyWidget(ocr)
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.exec_()


if __name__ == "__main__":
    run()
