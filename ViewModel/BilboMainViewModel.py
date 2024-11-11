# ViewModel/BilboMainViewModel.py
from PySide6.QtCore import QAbstractTableModel, Qt
from Model.fondosModel import FondosModel
from View.RegistrarBilboView import Ui_widget
from PySide6.QtWidgets import QDialog


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None


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
