from finger_print import Finger
import cv2
import base64
import io
import numpy as np
from PIL import Image

finger = Finger()

def _base64_to_image(base_string):
    base_string = base64.b64decode(base_string)
    base_string = io.BytesIO(base_string)
    base_string = Image.open(base_string)
    base_string = base_string.convert('RGB')
    base_string = np.array(base_string)
    base_string = base_string[:, :, ::-1].copy()

    return base_string

def predict(img):

    fingerprint, base_string = finger.get_print(img)
    prediction_class, prediction_index = finger.get_prediction(img, loglevel=True)
    return prediction_index

    
