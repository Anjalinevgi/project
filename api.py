from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load marks data from JSON file
with open("marks.json") as f:
    marks_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the 'name' parameters from the query string
    names = request.args.getlist('name')
    # Fetch the marks for the requested names
    result = {"marks": [marks_data.get(name, None) for name in names]}
    return jsonify(result)

# For local testing
if __name__ == "__main__":
    app.run(debug=True)
