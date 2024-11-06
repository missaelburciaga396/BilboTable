# Model/fondosModel.py
import sqlite3
import pandas as pd


class FondosModel:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_fondos_data(self):
        # Conecta a la base de datos SQLite
        conn = sqlite3.connect(self.db_path)

        # Lee la tabla "fondos" y la convierte en un DataFrame de pandas
        df = pd.read_sql_query("SELECT * FROM fondos", conn)

        # Cierra la conexión
        conn.close()

        return df
