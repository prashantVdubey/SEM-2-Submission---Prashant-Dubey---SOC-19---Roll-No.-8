# Experiment 13: JSON Array to CSV
import json
import csv

# Sample JSON array
json_data = '''
[
    {"id": 1, "name": "Alice",   "age": 21, "city": "Mumbai"},
    {"id": 2, "name": "Bob",     "age": 22, "city": "Delhi"},
    {"id": 3, "name": "Charlie", "age": 20, "city": "Pune"},
    {"id": 4, "name": "Diana",   "age": 23, "city": "Chennai"},
    {"id": 5, "name": "Evan",    "age": 25, "city": "Bangalore"}
]
'''

def json_to_csv(json_string, output_file):
    data = json.loads(json_string)
    if not data:
        print('JSON array is empty.')
        return

    # Extract column headers from first record
    fieldnames = list(data[0].keys())

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f'Converted {len(data)} records to "{output_file}"')
    print(f'Columns: {fieldnames}')

    # Display the CSV
    print('\n--- CSV Content ---')
    with open(output_file, 'r') as f:
        print(f.read())

json_to_csv(json_data, 'output.csv')
