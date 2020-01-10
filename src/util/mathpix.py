import os, sys, json, base64, requests

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from config import Config

env = os.environ

default_headers = {
    "app_id": env.get("APP_ID", Config.APP_ID),
    "app_key": env.get("APP_KEY", Config.APP_KEY),
    "Content-type": "application/json",
}

# Return the base64 encoding of an image with the given filename.
def image_uri(filename):
    image_data = open(filename, "rb").read()
    return "data:image/jpg;base64," + base64.b64encode(image_data).decode()


# Call the Mathpix service with the given arguments, headers, and timeout.
def latex(args, isClient, headers=default_headers, timeout=30):
    service = "https://api.mathpix.com/v3/" + ("latex" if isClient else "text")
    r = requests.post(service, data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)
