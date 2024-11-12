# ViewModel/BilboMainViewModel.py
from Model.fondosModel import FondosModel
from View.RegistrarBilboView import Ui_widget
from PySide6.QtWidgets import QDialog
from Model.pandasModel import PandasModel

class BilboMainViewModel:
    def __init__(self, db_path):
        # Crea una instancia del modelo de datos
        self.model = FondosModel(db_path)

    def get_table_model(self):
        # Obtiene los datos de la tabla en un DataFrame
        data = self.model.get_fondos_data()

        # Retorna un modelo de Pandas para QTableView
        return PandasModel(data)

    def registrar_widget(self):
        self.dialogo_registro = QDialog()
        self.ui_registro = Ui_widget()
        self.ui_registro.setupUi(self.dialogo_registro)

        # Mostrar el diálogo de registro como ventana modal
        self.dialogo_registro.exec()
