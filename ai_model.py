import tensorflow.keras
import numpy as np
import cv2

class AIModelFingerRealFake:
    def get_prediction(self, frame, loglevel=None):
        prediction_map = {0 : "Fake", 1 : "Real"}

        frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

        np.set_printoptions(suppress=True)

        model = tensorflow.keras.models.load_model('models/keras_model.h5')

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        normalized_image_array = (frame.astype(np.float32) / 127.0) - 1

        data[0] = normalized_image_array

        prediction = model.predict(data)
        print("[INFO] Prediction Metrics, ", prediction) if loglevel else print("")
        prediction = np.argmax(prediction)
        return prediction_map[prediction], prediction
