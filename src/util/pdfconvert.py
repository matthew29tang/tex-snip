import os, cv2
import numpy as np
import pdf2image as pdfIm
from . import detect

DEBUG = False
SCALE = 2
DIR = os.path.dirname(os.path.abspath(__file__)) + "\\"


def convertPdf(pdf):
    texFile = DIR + pdf.split("\\")[-1].split(".")[0] + ".tex"
    a = open(texFile.replace("\\", "/"), "w")

    pages = pdfIm.convert_from_path(pdf.replace("\\", "/"))
    totalPieces = []
    for i in range(len(pages)):
        # print(DIR + str(i) + ".jpg")
        pages[i].save(DIR + str(i) + ".jpg", "JPEG")
        totalPieces += _findBoxes(str(i))
    print(totalPieces)
    if len(totalPieces) > 50:
        a.write("Too many pieces - try splitting the file up")
        return "Too many pieces"
    latex = [detect.ocrServer(piece) for piece in totalPieces]
    text = "\n\n".join(latex)
    text = text.replace("\n", "\n\n")
    text = text.replace("\\(", "$")
    text = text.replace("\\)", "$")

    a.write(text)
    a.close()
    return text


def _findBoxes(filename):
    image = cv2.imread(DIR + filename + ".jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    dilate = cv2.dilate(thresh, kernel, iterations=7)

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    pieces = []
    for i in range(len(cnts) - 1, -1, -1):
        x, y, w, h = cv2.boundingRect(cnts[i])
        if w * h > 20000:
            # cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            part = image[y : y + h, x : x + w]
            pieceName = (
                DIR + "pieces/" + filename + "_" + str(len(cnts) - 1 - i) + ".jpg"
            ).replace("\\", "/")
            cv2.imwrite(pieceName, part)
            pieces.append(pieceName)

    try:
        os.remove(DIR + filename + ".jpg")
    except:
        pass

    if DEBUG:
        cv2.imshow("thresh", thresh)
        cv2.imshow("dilate", dilate)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image", image)
        cv2.resizeWindow(
            "image", (int(image.shape[1] / SCALE), int(image.shape[0] / SCALE))
        )
        cv2.waitKey()
    return pieces


if __name__ == "__main__":
    convert()
