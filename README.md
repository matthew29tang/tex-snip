# LaTeX OCR
[![Version](https://img.shields.io/badge/Version-1.1.1-1f425f.svg)](https://shields.io/)
[![Python](https://img.shields.io/badge/Python-3.6-1abc9c.svg)](https://shields.io/)
[![Updates](https://pyup.io/repos/github/matthew29tang/img-latex/shield.svg)](https://pyup.io/repos/github/matthew29tang/img-latex/)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## PDF to TeX
Flask server to convert PDF to TeX files. Limited to <5MB files.

Online usage: `https://tex-snip.herokuapp.com/`

Offline usage (requires API credentials): `python src/main.py`

---

## TeX Snip

Python utility to take a screenshot of latex math equation and convert it to LaTeX. Supports text and math (but only one paragraph at a time). If the screenshot cannot be converted, nothing will be copied to your clipboard.

Handwritten conversion is in beta mode.

### Usage
0) Install python. Developed on Python 3.6, use any other verions at your own risk.
1) Install python requirements `pip install -r requirements.txt`
2) Create API credentials (see below)
3) (Optional) Change keyboard config in `src/config.py`
4) Run the program using `python src/texSnip.py`
5) Start a screen cap, drag the dimensions, and release. The equation will be copied to your keyboard!
6) To terminate, use `SCROLL LOCK` or a key of your choice in `src/config.py`

### API Credentials

This utility uses MathPix as the OCR API. To create API credentials visit [https://dashboard.mathpix.com/](https://dashboard.mathpix.com/)

Documentation can be found [here](https://docs.mathpix.com/#request-parameters6).

Create a new file `src/credentials.py` in the following format:
```python
APP_ID = "<APP_ID>"
APP_KEY = "<APP_KEY>"
```

### Custom config
The default keybindings are:
* `ALT + P` to begin a screen capture
* `ESC` to cancel a screen capture
* `SCROLL LOCK` to terminate the program

All of the keybindings can be changed in `src/config.py`. See the [pynput documentation](https://pynput.readthedocs.io/en/latest/keyboard.html) for details of each key.
