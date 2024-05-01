from tkinter import messagebox, simpledialog
import tkinter as tk

class FamilyApp:

    def __init__(self, root, family_manager):
        self.root = root
        self.family_manager = family_manager
        self.family_listBox = tk.Listbox(self.root)
        self.setup_ui()

    def setup_ui(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Árbol Genealógico")
        self.root.geometry("400x300")
        self.family_listBox.pack(pady = 20)
        self.list_families()

        add_button = tk.Button(self.root, text="Agregar nueva familia", command=self.add_family)
        add_button.pack(pady=10)

    def list_families(self):
        families = self.family_manager.fetch_families()
        self.family_listBox.delete(0, tk.END)
        for family in families:
            self.family_listBox.insert(tk.END, family[1])

    def add_family(self):
        family_name = simpledialog.askstring("Agregar familia", "Nombre:")
        if family_name:
            if self.family_manager.add_family(family_name):
                self.list_families()
                messagebox.showinfo("Guardado", "Guardado exitosamente")

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Salir de la aplicación?"):
            self.family_manager.db_manager.close_connection()
            self.root.destroy()
