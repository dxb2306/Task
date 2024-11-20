import psycopg2
import json
from datetime import datetime, timezone
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="db",
        port="5432"
    )

def save_file_metadata(filename, row_count, columns):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO file_metadata (filename, upload_date, row_count, columns) 
            VALUES (%s, %s, %s, %s) RETURNING id
        """, (filename, datetime.now(timezone.utc), row_count, json.dumps(columns)))
        file_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return file_id
    except Exception as e:
        raise Exception(f"Failed to insert into file metadata: {e}")
    
def get_all_files():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM file_metadata")
        files = cur.fetchall()
        cur.close()
        conn.close()
        return files
    except Exception as e:
        raise Exception(f"Failed to fetch files: {e}")
    
def get_file_by_id(file_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM file_metadata WHERE id = %s", (file_id,))
        file_metadata = cur.fetchone()
        cur.close()
        conn.close()
        return file_metadata
    except Exception as e:
        raise Exception(f"Failed to fetch file metadata: {e}")