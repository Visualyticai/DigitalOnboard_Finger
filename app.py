from test import predict
from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route('/detectprints', methods=["POST"])
def detect_prints():
    frame = request.form["image"]

    temp = predict(frame)

    if (temp):
        return "", 200

    return "", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
