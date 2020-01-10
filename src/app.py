from flask import Flask
from flask_dropzone import Dropzone
import os

basedir = os.path.abspath(os.path.dirname(__file__))
if not os.path.exists("./uploads"):
    os.makedirs("./uploads")
if not os.path.exists("./util/pieces"):
    os.makedirs("./util/pieces")

app = Flask(__name__)
app.secret_key = "1337secret"

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, "uploads"),
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE=".pdf",
    DROPZONE_MAX_FILE_SIZE=5,
    DROPZONE_MAX_FILES=1,
    DROPZONE_UPLOAD_ON_CLICK=True,
    DROPZONE_PARALLEL_UPLOADS=1,
    DROPZONE_DEFAULT_MESSAGE="Upload PDF to convert to TeX",
    DROPZONE_INVALID_FILE_TYPE="Must be PDF",
    DROPZONE_FILE_TOO_BIG="File must be <5MB in size",
    DROPZONE_REDIRECT_VIEW="complete",
)
dropzone = Dropzone(app)
