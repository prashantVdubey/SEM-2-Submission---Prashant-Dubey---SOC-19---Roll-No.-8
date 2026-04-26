# Experiment 12: Count Rows in CSV
import csv

def count_csv_rows(filename):
    """Count total number of data rows (excluding header) in a CSV file."""
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Skip header
            row_count = sum(1 for row in reader)
        return row_count, header
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
        return None, None

# Run
filename = 'students.csv'
count, header = count_csv_rows(filename)

if count is not None:
    print(f'File         : {filename}')
    print(f'Header cols  : {header}')
    print(f'Total data rows: {count}')
