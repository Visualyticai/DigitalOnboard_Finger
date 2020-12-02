from finger_print import Finger
import cv2

img = cv2.imread("sample.jpg")

finger = Finger()

"""Testing Finger image to Finger print conversion"""
fingerprint, base_string = finger.get_print(img)
print("[INFO] Base64 Image String, ", base_string)
cv2.imshow("Finger Print", fingerprint)
cv2.waitKey(0)

"""Testing Finger Print Prediction"""
prediction_class, prediction_index = finger.get_prediction(img, loglevel=True)
assert(prediction_class, "Real")
assert(prediction_index, 1)
