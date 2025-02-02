from flask import Flask, request, jsonify
import json

app = Flask(__name__)


def load_student_marks():
    with open('student_marks.json', 'r') as file:
        return json.load(file)

@app.route('/api', methods=['GET'])
def get_student_marks():
    student_marks = load_student_marks()

    names = request.args.getlist('name')
    result = {}

    for name in names:
        if name in student_marks:
            result[name] = student_marks[name]
        else:
            result[name] = None  # If student not found

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
