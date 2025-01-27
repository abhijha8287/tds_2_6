import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load student marks from the JSON file
with open("api/students.json", "r") as f:
    student_marks = json.load(f)


# Route for the root URL
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Student Marks API!"})

# Route for fetching marks based on names
@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get 'name' query parameters as a list
    marks = [student_marks.get(name, None) for name in names]  # Fetch marks for each name
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)

