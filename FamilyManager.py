class FamilyManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def fetch_families(self):
        conn = self.db_manager.open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT family_id, family_name FROM Families")
            return cursor.fetchall()
        except Exception as e:
            print("Error fetching families:", e)
            return []

    def add_family(self, family_name):
        conn = self.db_manager.open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Families (family_name) VALUES (?)", family_name)
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar {e}")
            return False

    def delete_family(self, family_id):
        conn = self.db_manager.open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Families WHERE family_id = ?", (family_id,))
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la familia: {e}")
            return False

    def fetch_family_members(self, family_id):
        conn = self.db_manager.open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, p.name, f.name AS father_name, m.name AS mother_name
                FROM Persons p
                LEFT JOIN Persons f ON p.father_id = f.id
                LEFT JOIN Persons m ON p.mother_id = m.id
                WHERE p.family_id = ?
                """, (family_id,))
            return cursor.fetchall()
        except Exception as e:
            print("Error fetching family members:", e)
            return []


    def add_family_member(self, family_id, name, father_id, mother_id, photo):
        conn = self.db_manager.open_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO Persons (family_id, name, father_id, mother_id, photo) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql, (family_id, name, father_id, mother_id, photo))
            conn.commit()
            print("Added member successfully with father_id: {}, mother_id: {}".format(father_id, mother_id))
            return True
        except Exception as e:
            print("Error adding family member:", e)
            return False
