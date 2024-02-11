from PyQt5 import QtWidgets, QtGui
from RawInterfaces.Promociones import Ui_MainWindow
from Objects.Producto import Producto
import mysql.connector
from tkinter import messagebox

class Promociones(Ui_MainWindow, QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.cursor = self.connection.cursor()
        #Llenar las comboboxes

    def ObtenerDatos(self):
        self.connection.reconnect()
        scriptObtener = "SELECT * FROM producto WHERE activo = 'V'"
        self.cursor.execute(scriptObtener)
        results = self.cursor.fetchall()
        ArregloProductos = []
        for result in results:
            ArregloProductos.append(Producto(*result))
        self.HelloWorld(ArregloProductos)
        scriptObtener = "SELECT * FROM tipo_de_promocion"
        return ArregloProductos
    def LlenarCombos(self):
        pass
    def HelloWorld(self, str):
        print(str)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Promociones()
    ui.show()
    sys.exit(app.exec_())