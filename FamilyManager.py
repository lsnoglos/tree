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