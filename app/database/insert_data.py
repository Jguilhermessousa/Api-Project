from sqlalchemy import text
from app.database.imports import get_db
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def populate():
    def insert(filePath):
        db = get_db()
        sql_file = open(BASE_DIR + filePath, "r")
        sql = text(sql_file.read())

        db.execute(sql)

        try:
            db.commit()
        except:
            print(f"Error in file: {filePath}")
    
    insert("/scripts/employee_test.sql")

if __name__ == "__main__":
    populate()