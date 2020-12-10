import api
from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route('/detectprints', methods=["POST"])
def detect_prints():
    frame = request.form["image"]

    img = api._base64_to_image(frame)
    temp = api.predict(img)


    if (temp =="Real"):
        return "",200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
