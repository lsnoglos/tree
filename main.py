import os
from dotenv import load_dotenv
import pyodbc
import tkinter as tk
from tkinter import messagebox, simpledialog

load_dotenv()

root = tk.Tk()
family_listBox = tk.Listbox(root)

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DRIVER = 'ODBC Driver 17 for SQL Server'
conn = None

def create_connection():
    global conn
    if conn is None or conn.closed:
        try:
            connection_string = f'DRIVER={{{DRIVER}}};SERVER={DB_HOST};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}'
            conn = pyodbc.connect(connection_string)
            print("Conexión exitosa.")
        except Exception as e:
            print("Error de conexión", e)
    return conn

def on_closing():
    if messagebox.askokcancel("Salir","Salir de la aplicación?"):
        if conn is not None:
            conn.close()
            print("Conexión cerrada.")
        root.destroy()

def fetch_families():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT family_id, family_name FROM Families")
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching families:", e)
        return []

def list_families():
    families = fetch_families()
    family_listBox.delete(0, tk.END)
    for family in families:
        family_listBox.insert(tk.END, family[1])

def add_family():
    family_name = simpledialog.askstring("Agregar familia", "Nombre:")
    if family_name:
        conn = create_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Families (family_name) VALUES (?)", family_name)
            conn.commit()
            list_families()
            messagebox.showinfo("Guardado", "Guardado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar {e}")

def main():
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.title("Árbol genealógico")
    root.geometry("400x300")
    family_listBox.pack(pady=20)
    list_families()

    add_button = tk.Button(root, text="Agregar nueva familia", command=add_family)
    add_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
