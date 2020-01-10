import os
from app import app
from flask import Flask, Response, request, redirect, render_template
import util

DIR = os.path.dirname(os.path.abspath(__file__)) + "\\"


@app.route("/", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        for key, f in request.files.items():
            if key.startswith("file"):
                f.save(os.path.join(app.config["UPLOADED_PATH"], f.filename))
    return render_template("upload.html")


@app.route("/complete", methods=["POST", "GET"])
def complete():
    if request.referrer is None:
        return render_template("error.html")

    if len(os.listdir(app.config["UPLOADED_PATH"])) != 1:
        return redirect("/", code=302)

    filename = os.listdir(app.config["UPLOADED_PATH"])[0]
    latex = util.convertPdf(app.config["UPLOADED_PATH"] + "\\" + filename)
    texFile = (DIR + "util/" + filename.split("\\")[-1].split(".")[0] + ".tex").replace(
        "\\", "/"
    )
    a = open(texFile, "r")
    tex = a.read()
    a.close()
    os.remove(texFile)
    filelist = [
        f for f in os.listdir(app.config["UPLOADED_PATH"]) if f.endswith(".pdf")
    ]
    for f in filelist:
        os.remove(os.path.join(app.config["UPLOADED_PATH"], f))

    return Response(
        tex,
        mimetype="text",
        headers={
            "Content-disposition": "attachment; filename="
            + filename.split("\\")[-1].split(".")[0]
            + ".tex"
        },
    )


if __name__ == "__main__":
    app.run()
