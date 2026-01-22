from flask import Flask, render_template, jsonify, request
from chains.notes_chain import summarize_notes, generate_questions, extract_basics, explain_notes


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_notes():
    data = request.get_json()

    if not data:
        return jsonify({"result": "No data found"}), 400

    notes = data.get("notes", "").strip()
    action = data.get("action", "").strip()

    if not notes:
        return jsonify({"result": "Notes cannot be empty"}), 400

    try:
        if action == "summarize":
            result = summarize_notes(notes)

        elif action == "explain":
            result = explain_notes(notes)

        elif action == "questions":
            result = generate_questions(notes)

        elif action == "basics":
            result = extract_basics(notes)

        else:
            return jsonify({"result": "Invalid action"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"}), 500




if __name__ == "__main__":
    app.run(debug=True)