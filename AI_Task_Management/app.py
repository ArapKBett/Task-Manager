# app.py
from flask import Flask, request, jsonify
from task_manager import predict_task_duration, suggest_optimizations, automate_assignment

app = Flask(__name__)

@app.route('/predict_duration', methods=['POST'])
def predict_duration():
    data = request.json
    result = predict_task_duration(data['task_description'])
    return jsonify({"result": result})

@app.route('/suggest_optimizations', methods=['POST'])
def suggest_optimizations():
    data = request.json
    result = suggest_optimizations(data['task_description'])
    return jsonify({"result": result})

@app.route('/automate_assignments', methods=['POST'])
def automate_assignments():
    data = request.json
    result = automate_assignment(data['tasks'])
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
