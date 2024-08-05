from flask import Flask, render_template, request, jsonify
from wordle import Wordle

app = Flask(__name__)
game = Wordle()

@app.route('/')
def index():
    return render_template("view_wordle.html")



@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    word = data['word']
    result = game.guess(word)
    response = {"result": result, "history": game.history}
    return jsonify(response)

if __name__ == "__main__":
    app.run()