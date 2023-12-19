import os
import json

file_path = os.path.abspath("operations.json")

def get_operation():
    with open(file_path, encoding="utf-8") as file:
        operation_json = file.read()
        operation = json.loads(operation_json)
        return operation

def get_sorted_state(operations):
    sorted_list_state = []
    for operation in get_operation():
        if operation.get('state') == 'EXECUTED':
            sorted_list_state.append(operation)
    return sorted_list_state

def get_sorted_date(sorted_state):
    date_list = []
    for operation in sorted_state:
        date_list.append(operation['date'])
    sorted_list_date = sorted(date_list, reverse=True)
    return sorted_list_date[0:5]

def get_five_operations(sorted_state, sorted_date):

    five_operations = []
    for operation_time in sorted_date:
        for operation in sorted_state:
            if operation_time == operation['date']:
                five_operations.append(operation)
    return five_operations