import sqlite3
from databases.db_config import DB_PATH

def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        print("Connected to Telco Churn database successfully!")
        return conn
    except Exception as e:
        print(f"Connection Error: {e}")
        return None