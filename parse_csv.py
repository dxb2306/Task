import csv

def parse_csv(filepath):
    row_count = 0
    columns = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for header in headers:
            column_type = get_column_type(header)
            columns.append({'name': header, 'type': column_type})
        for _ in reader:
            row_count += 1

    return {'row_count': row_count, 'columns': columns}

def get_column_type(column_name):
    name = column_name.strip().lower()
    if 'temp' in name or 'temperature' in name:
        return 'float'
    elif 'humid' in name or 'pressure' in name:
        return 'float'
    elif 'time' in name or 'date' in name:
        return 'datetime'
    elif 'id' in name or 'count' in name:
        return 'integer'
    else:
        return 'text'