import os
from dotenv import load_dotenv
import pyodbc
import tkinter as tk
from tkinter import messagebox, simpledialog

load_dotenv()

DB_HOST=os.getenv('DB_HOST')
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DRIVER='ODBC Driver 17 for SQL Server'

def create_connection ():
    try:
        connection_string = f'DRIVER={{{DRIVER}}};SERVER={DB_HOST};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}'
        print("Conexión exitosa.")
        return pyodbc.connect(connection_string)
    except Exception as e:
        print("Error de conexio'n", e)
        return None

def fetch_families():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT family_id, family_name FROM Families")
            return cursor.fetchall()
        finally:
            conn.close()
    else:
        return []

def main():
    root = tk.Tk()
    root.title("Árbol genealógico")
    root.geometry("400x300")

    family_listBox = tk.Listbox(root)
    family_listBox.pack(pady = 20)
    families = fetch_families()

    for family in families:
        family_listBox.insert(tk.END, family[1])

    root.mainloop()

if __name__ == "__main__":
    main()