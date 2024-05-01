import pyodbc

class DatabaseManager:

    def __init__(self, driver, host, db_name, user, password):
        self.driver = driver
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.conn = None

    def open_connection(self):
        if self.conn is None or (self.conn and self.conn.closed):
            try:
                connection_string = f'DRIVER={{{self.driver}}};SERVER={self.host};DATABASE={self.db_name};UID={self.user};PWD={self.password}'
                self.conn = pyodbc.connect(connection_string)
                print("Conexión exitosa.")
            except Exception as e:
                print("Error de conexión", e)
        return self.conn

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            print("Conexión cerrada.")