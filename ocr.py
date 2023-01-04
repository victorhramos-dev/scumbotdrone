import os
import sys
import time

import cv2
import numpy as np
import pyautogui
from mss import mss
from PIL import Image, ImageChops, ImageOps
from tesserocr import PyTessBaseAPI

pyautogui.FAILSAFE = False


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


tess_path = resource_path('tess/tessdata')


def screenshot(reg):
    with mss() as sct:
        rect = {"left": reg['x'], "top": reg['y'],
                "width": reg['w'], "height": reg['h']}
        sct_img = sct.grab(rect)
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

        return img


def ocr(reg, scale=3, psm=3):
    img = np.array(screenshot(reg))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, None, fx=scale, fy=scale,
                     interpolation=cv2.INTER_LINEAR)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = 255 - img
    # cv2.imwrite('samples/' + str(time.time()) + '.png', img)

    with PyTessBaseAPI(path=tess_path, oem=0, psm=psm) as tess:
        tess.SetImage(Image.fromarray(img))
        text = tess.GetUTF8Text().strip()

    return text
