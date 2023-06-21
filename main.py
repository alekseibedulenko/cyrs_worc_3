from utils.utils import loads_json, shows_last_operations, sorts_by_date

if __name__ == '__main__':
    all_operations = loads_json('operations.json')

    all_operations = [operation for operation in all_operations if operation.get('state') == "EXECUTED"]
    all_operations = sorted(all_operations, key=sorts_by_date, reverse=True)[:5]

    shows_last_operations(all_operations)
