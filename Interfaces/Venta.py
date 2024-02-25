import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from RawInterfaces.Venta import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import mysql.connector
from Crud.CRUD_producto import CrudProducto, Producto
class Venta(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self,self)
        self.conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.cursor = self.conection.cursor()
        self.productManager = CrudProducto(self.conection)
        self.mainWidget = QtWidgets.QWidget()
        self.scrollAreaProducto.setWidget(self.mainWidget)
        self.LlenarDeProductos()

    def LlenarDeProductos(self):
        resultados = self.productManager.Read()
        print(resultados)
        scroll_layout = QtWidgets.QVBoxLayout(self.mainWidget)
        for i in range(len(resultados)):
            if i % 3 == 0:
                row_layout = QtWidgets.QHBoxLayout()
                scroll_layout.addLayout(row_layout)
            ventawidget = VentaWidget(f'../img/userImages/product_{resultados[i].nombre}.png', f'{resultados[i].nombre}', f'${resultados[i].precio}', '+', '-')
            row_layout.addWidget(ventawidget)

class VentaWidget(QtWidgets.QWidget):
    def __init__(self, image_path, labelNombre_text, labelPrecio_text, button1_text, button2_text):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        # Image
        pixmap = QPixmap(image_path)
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        # Label Nombre
        labelNombre = QtWidgets.QLabel(labelNombre_text)
        layout.addWidget(labelNombre)
        # Label Precio
        labelPrecio = QtWidgets.QLabel(labelPrecio_text)
        layout.addWidget(labelPrecio)
        # Buttons
        button1 = QtWidgets.QPushButton(button1_text)
        button2 = QtWidgets.QPushButton(button2_text)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        layout.addLayout(button_layout)

        self.setLayout(layout)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Venta()
    ui.show()
    sys.exit(app.exec_())