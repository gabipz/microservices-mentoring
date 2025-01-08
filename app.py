from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Hello, world"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200


@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'title': task_data['title'],
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201


@app.route('/tasks/', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200


@app.route('/tasks/', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task_data = request.get_json()
    task['title'] = task_data.get('title', task['title'])
    task['completed'] = task_data.get('completed', task['completed'])
    return jsonify(task), 200


@app.route('/tasks/', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)