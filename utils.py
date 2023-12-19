import os
import json

file_path = os.path.abspath("operations.json")

def get_operation():
    with open(file_path, encoding="utf-8") as file:
        operation_json = file.read()
        operation = json.loads(operation_json)
        return operation