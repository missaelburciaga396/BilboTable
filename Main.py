# Main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from View.BilboMainView import Ui_MainWindow
from ViewModel.BilboMainViewModel import BilboMainViewModel


class MainWindow(QMainWindow):
    def __init__(self, db_path):
        super(MainWindow, self).__init__()

        # Inicializar la interfaz de usuario
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Crear instancia del ViewModel con la base de datos
        self.viewModel = BilboMainViewModel(db_path)

        # Cargar los datos en la tabla
        self.load_data()

    def load_data(self):
        # Obtiene el modelo de tabla desde el ViewModel
        table_model = self.viewModel.get_table_model()

        # Asigna el modelo de datos al QTableView en la interfaz
        self.ui.tableViewBilbo.setModel(table_model)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Define la ruta a tu base de datos SQLite
    db_path = "DB/BilboDb.db"

    mainWindow = MainWindow(db_path)
    mainWindow.show()
    sys.exit(app.exec())
