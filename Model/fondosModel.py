# Model/fondosModel.py
import pandas as pd
from DB.dbconexion import DatabaseConnection

class FondosModel:
    def __init__(self, db_path):
        self.db_path = db_path

    # Create: Agregar un nuevo registro
    def add_fondo(self, nombre, cantidad):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO fondos (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
            conn.commit()

    # Read: Obtener todos los registros
    def get_fondos_data(self):
        with DatabaseConnection(self.db_path) as conn:
            df = pd.read_sql_query("SELECT * FROM fondos", conn)
        return df

    # Update: Modificar un registro existente
    def update_fondo(self, fondo_id, nombre, cantidad):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE fondos SET nombre = ?, cantidad = ? WHERE id = ?", (nombre, cantidad, fondo_id))
            conn.commit()

    # Delete: Eliminar un registro por ID
    def delete_fondo(self, fondo_id):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fondos WHERE id = ?", (fondo_id,))
            conn.commit()
