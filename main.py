import os
import csv

from flask import request, jsonify, Flask
from werkzeug.utils import secure_filename
from parse_csv import parse_csv
from flask_cors import CORS

from db import *

app = Flask(__name__)
CORS(app) 

app.config['UPLOAD_FOLDER'] = './upload_files'

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file found.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Parse CSV for metadata
    metadata = parse_csv(filepath)
    row_count, columns = metadata['row_count'], metadata['columns']

    # Save metadata to the database
    try:
        file_id = save_file_metadata(filename, row_count, columns)
    except Exception as e:
        return jsonify({'error': f'Failed to save metadata: {e}'}), 500

    return jsonify({'message': 'File uploaded successfully', 'file_id': file_id}), 201

@app.route('/api/files', methods=['GET'])
def list_files():
    try:
        files = get_all_files()
    except Exception as e:
        return jsonify({'error': f'Failed to fetch files: {e}'}), 500

    return jsonify(files), 200

@app.route('/api/file/<int:file_id>', methods=['GET'])
def get_file(file_id):
    try:
        file_metadata = get_file_by_id(file_id)
    except Exception as e:
        return jsonify({'error': f'Failed to fetch file metadata: {e}'}), 500

    if not file_metadata:
        return jsonify({'error': 'File not found'}), 404

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file_metadata['filename'])
    
    # Check if the file exists on the server
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found on server'}), 404
    
    # Read the entire file content
    data = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)  # Read the headers
            for row in reader:
                data.append(row)  # Read all rows
    except Exception as e:
        return jsonify({'error': f'Failed to read file: {e}'}), 500

    # Return headers and rows as JSON
    return jsonify({'headers': headers, 'rows': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
