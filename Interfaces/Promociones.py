import datetime

from PyQt5 import QtWidgets, QtGui, QtCore
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
        self.LLenarPromos()
        self.BotonAgregarPromocion.clicked.connect(lambda: self.subirPromocion())



    def subirPromocion(self):
        script = "INSERT INTO promocion(id_producto, descripcion, fecha_de_inicio, fecha_de_finalizacion, id_tipo_promocion) VALUES (%s,%s,%s,%s,%s)"
        datatorecorrer = self.ObtenerDatos()
        values = []
        for producto in datatorecorrer[0]:
            if producto.nombre == self.PromocionBox.currentText():
                idselected = producto.id
        #encintramos el id del producto en el combobox
        values.append(idselected)
        #descripcion
        values.append(self.textEdit.toPlainText())
        #fechas
        values.append(self.FechaInicioBox.text())
        values.append(self.FechaFinalBox.text())
        for tipopromocion in datatorecorrer[1]:
            if tipopromocion.nombre == self.TipoPromocionBox.currentText():
                idselected = tipopromocion.id
        values.append(idselected)
        self.HelloWorld(f"los valores que voy a subiur son {values}")
        self.cursor.execute(script, values)
        self.connection.commit()
        self.LLenarPromos()


    def ObtenerDatos(self):
        self.connection.reconnect()
        scriptObtener = "SELECT * FROM producto WHERE activo = 'V'"
        self.cursor.execute(scriptObtener)
        results = self.cursor.fetchall()
        ArregloProductos = []
        for result in results:
            ArregloProductos.append(Producto(*result))
        scriptObtener = "SELECT * FROM tipo_de_promocion"
        self.cursor.execute(scriptObtener)
        results = self.cursor.fetchall()
        ArregloTipos = []
        for result in results:
            ArregloTipos.append(TipoPromocion(*result))
        return (ArregloProductos, ArregloTipos)
    def LlenarCombos(self):
        ArrPro, ArrTipo = self.ObtenerDatos()
        for producto in ArrPro:
            self.PromocionBox.addItem(producto.nombre)
        for tipoPromocion in ArrTipo:
            self.TipoPromocionBox.addItem(tipoPromocion.nombre)
    def LLenarPromos(self):
        #widgets que sostienen lo que le vamos a poner a la scroll area
        scroll_widget = QtWidgets.QWidget()
        scroll_layout = QtWidgets.QVBoxLayout(scroll_widget)
        self.connection.reconnect()
        script = "SELECT * FROM promocion WHERE activo = 'V'"
        self.cursor.execute(script)
        results = self.cursor.fetchall()
        print(results)
        for i in range(len(results)):
            #añadir los widgets que vamos a tener
            widget = WidgetPromocion(results[i][2], results[i][0], results[i][1], results[i][3], results[i][4], results[i][5])
            scroll_layout.addWidget(widget)
        self.scrollAreaPromociones.setWidget(scroll_widget)


    def HelloWorld(self, str):
        print(str)
class WidgetPromocion(QtWidgets.QWidget):
    def __init__(self, desc: str, idprod: int, idpromo: int, fechaini: datetime.datetime, fechafin:datetime.datetime, idtipo: int, parent=None):
        super().__init__(parent)
        #parametros
        self.idprod = idprod
        self.idpromo = idpromo
        self.fechaini = fechaini
        self.fechafin = fechafin
        self.idtipo = idtipo
        #Necesario para que se vea bien
        self.setMinimumHeight(80)
        self.setMinimumWidth(100)
        layout = QtWidgets.QVBoxLayout()
        self.label = ClickableLabel(f"{desc}")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setMaximumHeight(100)
        # Conectar la señal clicked al método handleClick
        self.label.clicked.connect(self.Clicked)
        #stylesheet
        self.setStyleSheet("background-color: #011936; "
                           "color: white; "
                           "padding: 0 10px 0 10px; "
                           "margin: 0 0 0 0; "
                           "border-radius: 5px;")
    def Clicked(self):
        print(f"Hiciste click en {self.idprod,self.idpromo,self.label.text(), self.fechaini,self.fechafin, self.idtipo}")

class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Promociones()
    ui.show()
    sys.exit(app.exec_())