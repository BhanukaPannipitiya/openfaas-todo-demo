from flask import jsonify

# In-memory list of todos (temporary static data)
todos = [
    {"id": 1, "title": "Buy milk"},
    {"id": 2, "title": "Finish OpenFaaS project"}
]

def handle(event, context):
    """
    Returns the list of todos in JSON format.
    """
    return jsonify(todos)
