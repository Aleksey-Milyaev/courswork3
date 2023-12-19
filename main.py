from datetime import datetime
from utils import get_operation, get_sorted_state, get_sorted_date, get_five_operations

def main():
    operations = get_operation()
    sorted_state = get_sorted_state(operations)
    sorted_date = get_sorted_date(sorted_state)
    five_operations = get_five_operations(sorted_state, sorted_date)

    for operation in five_operations:
        requisites = str(operation.get('from')).split()
        to = str(operation["to"]).split()
        if requisites[0].lower().startswith('счет'):
            print(f'{datetime.fromisoformat(operation["date"]).strftime("%d.%m.%Y")} {operation["description"]}\n{requisites[0]} ** {requisites[1][-4:]} -> {to[0]} **{to[1][-4:]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
        elif requisites[0] == "None":
            print(f'{datetime.fromisoformat(operation["date"]).strftime("%d.%m.%Y")} {operation["description"]}\n{to[0]} **{to[1][-4:]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
        else:
            print(f'{datetime.fromisoformat(operation["date"]).strftime("%d.%m.%Y")} {operation["description"]}\n{requisites[0]} {requisites[1][0:4]}** **** {requisites[1][-4:]} -> {to[0]} **{to[1][-4:]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')

main()

