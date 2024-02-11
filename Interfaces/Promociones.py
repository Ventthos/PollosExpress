from PyQt5 import QtWidgets, QtGui
from RawInterfaces.Promociones import Ui_MainWindow
from Objects.Producto import Producto
from Objects.TiposPromocion import TipoPromocion
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
        self.LlenarCombos()

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
        self.cursor.execute(scriptObtener)
        results = self.cursor.fetchall()
        ArregloTipos = []
        for result in results:
            ArregloTipos.append(TipoPromocion(*result))
        self.HelloWorld(ArregloTipos)
        return (ArregloProductos, ArregloTipos)
    def LlenarCombos(self):
        ArrPro, ArrTipo = self.ObtenerDatos()
        for producto in ArrPro:
            self.PromocionBox.addItem(producto.nombre)
        for tipoPromocion in ArrTipo:
            self.TipoPromocionBox.addItem(tipoPromocion.nombre)
    def HelloWorld(self, str):
        print(str)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Promociones()
    ui.show()
    sys.exit(app.exec_())