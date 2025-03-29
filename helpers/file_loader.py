import csv
import os

def load_csv(filename, required_col):
    test_data = []
    #filepath = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = set(required_col)
            if not headers.issubset(reader.fieldnames):
                missing = headers - set(reader.fieldnames)
                raise ValueError(f"CSV {filename} missing required columns: {missing}")
            
            for row in reader:
                extracted = tuple(row[col] for col in required_col)
                test_data.append(extracted)
    except Exception as e:
        print(f"Error reading {filename}: {e}")

    if not test_data:
        print(f"Warning: Empty? {filename}")

    return test_data