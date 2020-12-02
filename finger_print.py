import os
import base64
from ai_model import AIModelFingerRealFake
import cv2

os.environ['QT_X11_NO_MITSHM']='1'

class Finger(AIModelFingerRealFake):
    def get_print(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equ = cv2.equalizeHist(gray)
        thresh = cv2.adaptiveThreshold(equ, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
        blur = cv2.GaussianBlur(thresh,(5,5),0)
        _,thresh1 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
        return thresh1, base64.b64encode(thresh1)
