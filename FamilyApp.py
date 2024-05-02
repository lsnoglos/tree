from tkinter import messagebox, simpledialog
import tkinter as tk

from FamilyDetailWindow import FamilyDetailWindow

class FamilyApp:

    def __init__(self, root, family_manager):
        self.root = root
        self.family_manager = family_manager
        self.family_listBox = tk.Listbox(self.root)
        self.setup_ui()

    def setup_ui(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Árbol Genealógico")
        self.root.geometry("600x400")

        list_frame = tk.Frame(self.root)
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.family_listBox = tk.Listbox(list_frame, width=50, height=20)
        self.family_listBox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.list_families()

        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=20, pady=20)

        add_button = tk.Button(button_frame, text="Agregar familia", command=self.add_family)
        add_button.pack(fill=tk.X)

        delete_button = tk.Button(button_frame, text="Eliminar familia", command=self.delete_selected_family)
        delete_button.pack(fill=tk.X)

        detail_button = tk.Button(button_frame, text="Miembros familia", command=self.show_family_details)
        detail_button.pack(fill=tk.X)

    def list_families(self):
        self.families = self.family_manager.fetch_families()
        self.family_listBox.delete(0, tk.END)
        for family_id, name in self.families:
            self.family_listBox.insert(tk.END, name)

    def add_family(self):
        family_name = simpledialog.askstring("Agregar familia", "Nombre:")
        if family_name:
            if self.family_manager.add_family(family_name):
                self.list_families()
                messagebox.showinfo("Guardado", "Guardado exitosamente")

    def delete_selected_family(self):
        try:
            selected_index = self.family_listBox.curselection()[0]
            family_id = self.families[selected_index][0]
            if self.family_manager.delete_family(family_id):
                self.list_families()
                messagebox.showinfo("Eliminado", "Familia eliminada exitosamente")
        except IndexError:
            messagebox.showerror("Error", "Seleccione una familia para eliminar")

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Salir de la aplicación?"):
            self.family_manager.db_manager.close_connection()
            self.root.destroy()

    def show_family_details(self):
        try:
            selected_index = self.family_listBox.curselection()[0]
            family_id = self.families[selected_index][0]
            detail_window = FamilyDetailWindow(self.root, self.family_manager, family_id)
        except IndexError:
            messagebox.showerror("Error", "Seleccione una familia para ver detalles")