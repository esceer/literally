import os
import random

from flask import Flask
from flask import render_template

project_dir = os.path.dirname(os.path.abspath(__file__))
dictionaries_dir = os.path.join(project_dir, "dictionaries")
dictionary = os.path.join(dictionaries_dir, "korean.txt")

app = Flask(__name__)


@app.get("/literally")
def home():
    return render_template("home.html")


@app.get("/literally/korean")
def draw_word():
    words = {}
    with open(dictionary, "r", encoding="utf8") as f:
        for line in f:
            key, value = map(str.strip, line.split(","))
            words[key] = value

    translation, drawn_word = random.choice(list(words.items()))
    return render_template("home.html", drawn_word=drawn_word, translation=translation)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
