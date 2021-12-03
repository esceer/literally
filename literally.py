import os
import random

from flask import Flask
from flask import redirect
from flask import render_template

project_dir = os.path.dirname(os.path.abspath(__file__))
dictionaries_dir = os.path.join(project_dir, "dictionaries")

app = Flask(__name__)


@app.get("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")


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
    dictionary, schema_error = load_dictionary(language)
    translation, drawn_word = random.choice(list(dictionary.items()))
    return render_template("quiz.html",
                           drawn_word=drawn_word,
                           translation=translation,
                           language=language,
                           schema_error=schema_error)


def load_dictionary(language):
    dictionary = {}
    schema_error = False
    input_file = os.path.join(dictionaries_dir, "{}.txt".format(language))
    with open(input_file, "r", encoding="utf8") as f:
        for line in f:
            try:
                key, value = map(str.strip, line.split(","))
                dictionary[key] = value
            except ValueError:
                print("[ERROR] Unable to parse line: '{}'".format(line))
                schema_error = True
    return dictionary, schema_error


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
