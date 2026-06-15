import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from databases.connection import get_connection

conn = get_connection()

if conn:
    print("Test Passed")
    conn.close()
else:
    print("Test Failed")
