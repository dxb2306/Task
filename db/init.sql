CREATE TABLE file_metadata (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    row_count INT,
    columns JSONB
);
