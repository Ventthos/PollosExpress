import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from RawInterfaces.Venta import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import mysql.connector
from Crud.CRUD_producto import CrudProducto, Producto
import WidgetApoyo.ValidadorDeOfertas

class Venta(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
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
        resultados = self.productManager.ReadSimplified()
        print(resultados)
        scroll_layout = QtWidgets.QVBoxLayout(self.mainWidget)
        for i in range(len(resultados)):
            if i % 3 == 0:
                row_layout = QtWidgets.QHBoxLayout()
                scroll_layout.addLayout(row_layout)
            ventawidget = VentaWidget(f'../img/userImages/product_{resultados[i].nombre}.png',
                                      f'{resultados[i].nombre}',
                                      f'${resultados[i].precio}',
                                      'Agregar',
                                      'Eliminar',
                                      f"{resultados[i].id}",
                                      table=self.TablaVenta)
            row_layout.addWidget(ventawidget)


class VentaWidget(QtWidgets.QWidget):
    def __init__(self, image_path, labelNombre_text : str, labelPrecio_text : str, button1_text : str, button2_text : str, idProducto : int, table: QtWidgets.QTableWidget):
        super().__init__()
        self.setObjectName("VentaWidget")  # Asignamos un nombre al widget principal
        #visual
        layout = QtWidgets.QVBoxLayout(self)  # Indicamos que el layout pertenece al widget principal

        # Image
        pixmap = QtGui.QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(150)  # Limita el ancho máximo de la imagen a 150 píxeles
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label, alignment=QtCore.Qt.AlignCenter)

        # Label Nombre
        labelNombre = QtWidgets.QLabel(labelNombre_text)
        labelNombre.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(labelNombre)

        # Label Precio
        labelPrecio = QtWidgets.QLabel(labelPrecio_text)
        labelPrecio.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(labelPrecio)
        #CantidadAaAgregar
        self.lineCantidad = CustomLineEditVentas()
        self.lineCantidad.setObjectName("CantidadDeProducto")
        layout.addWidget(self.lineCantidad)
        # Botones
        buttonAgregar = QtWidgets.QPushButton(button1_text)
        buttonEliminar = QtWidgets.QPushButton(button2_text)
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(buttonAgregar)
        button_layout.addWidget(buttonEliminar)

        layout.addLayout(button_layout)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setMinimumHeight(350)
        #Logic
        self.idProducto = idProducto
        self.nombreProducto = labelNombre_text
        self.precioProducto = float(labelPrecio_text[1:])
        self.table = table
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        buttonAgregar.clicked.connect(self.AgregarProductoAVenta)
        buttonEliminar.clicked.connect(self.EliminarProductoDeTabla)
        self.validador = WidgetApoyo.ValidadorDeOfertas.Validador(self.idProducto, self.table, self)
    def AgregarProductoAVenta(self):
        # Obtener el subtotal actual
        print(self.idProducto)
        if self.lineCantidad.text() != "":
            subtotal_actual = float(self.lineCantidad.text()) * float(self.precioProducto)
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            values = [self.nombreProducto, #nombre
                      self.lineCantidad.text(), #cantidad
                      str(self.precioProducto), #precio
                      str(subtotal_actual)  # Convertir a texto antes de agregar al QTableWidgetItem
                      ]
            self.validador.BuscarPromocionesRelacionadas(values)
            for i in range(4):
                self.table.setItem(row_count, i, QtWidgets.QTableWidgetItem(values[i]))
            # Calcular el total actual sumando el subtotal actual al total anterior
            total_anterior = 0.0
            if row_count > 0:  # Verificar si hay filas anteriores en la tabla
                total_anterior = float(self.table.item(row_count - 1, 4).text())  # Obtener el total de la fila anterior
            total_actual = total_anterior + subtotal_actual

            # Agregar el total actual a la tabla
            self.table.setItem(row_count, 4, QtWidgets.QTableWidgetItem(str(total_actual)))
            self.lineCantidad.setText("")
            self.validador.CalcularTotal()

    def EliminarProductoDeTabla(self):
        filaAEliminar = self.buscar_producto(self.nombreProducto)
        if filaAEliminar is not None:
             self.table.removeRow(filaAEliminar[1])

    def buscar_producto(self, stringABuscar : str):
        texto_busqueda = stringABuscar.strip().lower()
        for fila in range(self.table.rowCount()):
            for columna in range(self.table.columnCount()):
                item = self.table.item(fila, columna)
                if item is not None and texto_busqueda in item.text().strip().lower():
                    return  (columna,fila)
    def calcularCantidad(self):
        pass
class CustomLineEditVentas(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Configura la validación de entrada para permitir solo números enteros
        self.setValidator(QtGui.QIntValidator())

        # Establece la longitud máxima de caracteres
        self.setMaxLength(2)  # Aquí se establece en 2 para limitar a un máximo de 25
        self.textChanged.connect(self.limitar_a_25)
    def limitar_a_25(self):
        # Verifica si el valor actual es mayor a 25
        if self.text() and int(self.text()) > 25:
            # Si es mayor a 25, establece el valor a 25
            self.setText("25")
        if self.text() and int(self.text()) <= 0:
            self.setText("1")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Venta()
    ui.show()
    sys.exit(app.exec_())
