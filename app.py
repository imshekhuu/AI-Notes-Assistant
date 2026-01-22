from flask import Flask, render_template, jsonify
from chains.notes_chain import summarize_notes, generate_questions, extract_basics


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)