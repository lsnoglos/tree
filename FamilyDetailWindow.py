import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, Toplevel, Label, Entry, Button, Listbox
from tkinter import ttk 
import base64

class FamilyDetailWindow:
    def __init__(self, parent, family_manager, family_id):
        self.top = tk.Toplevel(parent)
        self.family_manager = family_manager
        self.family_id = family_id
        self.selected_father_id = None
        self.selected_mother_id = None
        self.setup_ui()

    def setup_ui(self):
        self.top.title("Detalles de la Familia")
        self.top.geometry("600x600")

        list_frame = tk.Frame(self.top)
        list_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.top.grid_columnconfigure(0, weight=1)
        self.top.grid_rowconfigure(0, weight=1)

        self.member_list_box = tk.Listbox(list_frame, width=50, height=20)
        self.member_list_box.pack(expand=True, fill=tk.BOTH)

        button_frame = tk.Frame(self.top)
        button_frame.grid(row=0, column=1, sticky="ns", padx=20)

        add_button = tk.Button(button_frame, text="Agregar", command=self.add_member)
        add_button.pack()

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_member)
        delete_button.pack()

        add_member_frame = tk.Frame(self.top)
        add_member_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20)
        self.top.grid_rowconfigure(1, weight=0)

        tk.Label(add_member_frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(add_member_frame)
        self.name_entry.grid(row=0, column=1, sticky="we", padx=5)

        tk.Label(add_member_frame, text="Padre:").grid(row=1, column=0, sticky="e")
        self.father_combobox = ttk.Combobox(add_member_frame, state="readonly")
        self.father_combobox.grid(row=1, column=1, sticky="we", padx=5)
        self.father_combobox.bind("<<ComboboxSelected>>", self.update_father_combobox)

        tk.Label(add_member_frame, text="Madre:").grid(row=2, column=0, sticky="e")
        self.mother_combobox = ttk.Combobox(add_member_frame, state="readonly")
        self.mother_combobox.grid(row=2, column=1, sticky="we", padx=5)
        self.mother_combobox.bind("<<ComboboxSelected>>", self.update_mother_combobox)

        tk.Label(add_member_frame, text="Foto:").grid(row=3, column=0, sticky="e")
        self.photo_entry = tk.Entry(add_member_frame)
        self.photo_entry.grid(row=3, column=1, sticky="we", padx=5)

        upload_button = tk.Button(add_member_frame, text="Cargar Foto", command=self.upload_photo)
        upload_button.grid(row=4, column=1, sticky="e", padx=5)

        self.load_members()

    def update_father_combobox(self, event=None):
        current_father = self.father_combobox.get()
        self.selected_father_id = next((id for id, name in self.members if name == current_father), None)
        self.populate_comboboxes()

    def update_mother_combobox(self, event=None):
        current_mother = self.mother_combobox.get()
        self.selected_mother_id = next((id for id, name in self.members if name == current_mother), None)
        self.populate_comboboxes()

    def populate_comboboxes(self):
        members = self.family_manager.fetch_family_members(self.family_id)
        self.members = [(member[0], member[1]) for member in members]
        self.father_combobox['values'] = [name for id, name in self.members if id != self.selected_mother_id]
        self.mother_combobox['values'] = [name for id, name in self.members if id != self.selected_father_id]

    def load_members(self):
        self.populate_comboboxes()
        self.member_list_box.delete(0, tk.END)
        for member_id, name in self.members:
            self.member_list_box.insert(tk.END, name)

    def upload_photo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'rb') as file:
                binary_data = file.read()
                self.photo_data = base64.b64encode(binary_data) 
            self.photo_entry.delete(0, tk.END)
            self.photo_entry.insert(0, file_path)

    def add_member(self):
        print("Intentando agregar miembro...")
        name = self.name_entry.get()
        father_id = self.selected_father_id
        mother_id = self.selected_mother_id
        photo = self.photo_data if hasattr(self, 'photo_data') else None
        if name:
            print("Datos del nuevo miembro:", name, father_id, mother_id)
            success = self.family_manager.add_family_member(self.family_id, name, father_id, mother_id, photo)
            if success:
                print("Miembro agregado correctamente.")
                self.load_members()
                messagebox.showinfo("Éxito", "Miembro agregado correctamente")
            else:
                print("Error al agregar miembro.")
                messagebox.showerror("Error", "No se pudo agregar el miembro")
        else:
            print("El campo nombre está vacío.")
            messagebox.showerror("Error", "Por favor, ingrese un nombre para el miembro.")

    def delete_member(self):
        selected_index = self.member_list_box.curselection()[0]
        member_id = self.members[selected_index][0]
        if self.family_manager.delete_family_member(member_id):
            self.load_members()
            messagebox.showinfo("Eliminado", "Miembro eliminado exitosamente")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el miembro")