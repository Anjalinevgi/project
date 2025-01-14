from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load marks data
with open("q-vercel-python.json") as f:
    marks_data = json.load(f)

# Ensure marks_data is a list
if not isinstance(marks_data, list):
    raise ValueError("q-vercel-python.json must contain a list of dictionaries")

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    result = {"marks": []}

    # For each name in the query parameters, find the corresponding marks
    for name in names:
        student = next((student for student in marks_data if student["name"] == name), None)
        result["marks"].append(student["marks"] if student else None)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

