from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# Sample sentences for typing test
SAMPLE_SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and versatile programming language.",
    "Flask is a lightweight web framework in Python.",
    "Practice makes perfect when it comes to typing speed.",
]


@app.route("/", methods=["GET", "POST"])
def typing_test():
    if request.method == "POST":
        sentence = random.choice(SAMPLE_SENTENCES)
        return render_template("typing_test.html", sentence=sentence)
    return render_template("typing_test.html")


@app.route("/calculate_wpm", methods=["POST"])
def calculate_wpm():
    start_time = float(request.form.get("start_time"))
    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0  # in minutes

    typed_text = request.form.get("typed_text")
    typed_words = typed_text.strip().split()
    num_words = len(typed_words)

    wpm = int(num_words / time_elapsed)
    return jsonify({"wpm": wpm})


if __name__ == "__main__":
    app.run(debug=True)
