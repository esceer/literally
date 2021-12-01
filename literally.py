import os
import random

from flask import Flask
from flask import redirect
from flask import render_template

project_dir = os.path.dirname(os.path.abspath(__file__))
dictionaries_dir = os.path.join(project_dir, "dictionaries")

app = Flask(__name__)


@app.get("/")
def root():
    return redirect("/literally")


@app.get("/literally")
def home():
    return render_template("home.html")


@app.get("/literally/<language>")
def draw_word(language):
    if language not in ("german", "korean"):
        return "The language '{}' is not supported".format(language)
    dictionary = load_dictionary(language)
    translation, drawn_word = random.choice(list(dictionary.items()))
    return render_template("quiz.html", drawn_word=drawn_word, translation=translation, language=language)


def load_dictionary(language):
    dictionary = {}
    input_file = os.path.join(dictionaries_dir, "{}.txt".format(language))
    with open(input_file, "r", encoding="utf8") as f:
        for line in f:
            key, value = map(str.strip, line.split(","))
            dictionary[key] = value
    return dictionary


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
