import json
import os

DB_FILE = "/tmp/todos.json"

def handle(event, context):
    try:
        data = json.loads(event.body or "{}")
        title = data.get("title")

        if not title:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "title is required"})
            }

        todos = []
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                todos = json.load(f)

        new_todo = {"id": len(todos) + 1, "title": title}
        todos.append(new_todo)

        with open(DB_FILE, "w") as f:
            json.dump(todos, f)

        return {
            "statusCode": 201,
            "body": json.dumps(new_todo)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
