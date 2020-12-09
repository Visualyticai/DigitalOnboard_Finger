import base64
import requests
from pathlib import Path

#passing real image
with open(str(Path(__file__).resolve().parent)+"/images/real.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())


r = requests.post('http://0.0.0.0:5000/detectprints', data={'image': my_string})

assert(r.status_code==200)
