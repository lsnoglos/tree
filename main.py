import os
from dotenv import load_dotenv
import tkinter as tk

from DatabaseManager import DatabaseManager
from FamilyManager import FamilyManager
from FamilyApp import FamilyApp

if __name__ == "__main__":
    root = tk.Tk()
    load_dotenv()
    db_manager = DatabaseManager(
        'ODBC Driver 17 for SQL Server',
        os.getenv('DB_HOST'),
        os.getenv('DB_NAME'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
    )
    family_manager = FamilyManager(db_manager)
    app = FamilyApp(root, family_manager)
    root.mainloop()