import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from RawInterfaces.Venta import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import mysql.connector
from Crud.CRUD_producto import CrudProducto, Producto
import WidgetApoyo.ValidadorDeOfertas
from Interfaces.PagarInterface import PagarInterface
from tkinter import messagebox
class Venta(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, descargar=False):
        super().__init__()
        super().setupUi(self)
        self.conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.scroll_layout: QtWidgets.QVBoxLayout = None
        self.row_layouts: list[QtWidgets.QHBoxLayout] = []
        self.cursor = self.conection.cursor()
        self.productManager = CrudProducto(self.conection)
        self.mainWidget = QtWidgets.QWidget()
        self.scrollAreaProducto.setWidget(self.mainWidget)
        self.descargarImagenes: bool = descargar
        self.LlenarDeProductos()
        self.refresh_Button.clicked.connect(self.refresh)
        # Ventana del pago
        self.ventanaPago = PagarInterface(self.conection, 1, self)
        self.pushButton.clicked.connect(self.launchVenta)

    def launchVenta(self):
        self.conection.commit()
        sepuedevender : bool = True
        valoresacambiar : [tuple] = []
        for row in range(self.TablaVenta.rowCount()):
            cantidad = int(self.TablaVenta.item(row, 1).text())
            idProducto = self.TablaVenta.item(row, 4).text()
            print(f"Hay {cantidad} del producto {idProducto}")
            script = "SELECT cantidad FROM inventario WHERE id_producto = %s"
            self.cursor.execute(script, [idProducto])
            cantidadEnInventario = self.cursor.fetchone()
            print(f"En el inventario hay {cantidadEnInventario[0]} de {idProducto}")
            if cantidad > cantidadEnInventario[0]:
                sepuedevender = False
                break
            valoresacambiar.append((idProducto,cantidadEnInventario[0] - cantidad))
        if sepuedevender:
            self.ventanaPago.show()
            self.ventanaPago.setTable(self.TablaVenta, self.LabelPrecioTotalDecimal.text())
            print(f"Los valores para cambiar son: {valoresacambiar}")
            self.ventanaPago.valoresParaCambiar = valoresacambiar
        if not sepuedevender:
            messagebox.askyesno("Inventario","No hay suficiente producto en el inventario")
    def refresh(self):
        for layout in self.row_layouts:
            self.deleteItemsOfLayout(layout)
        #self.descargarImagenes = True
        self.LlenarDeProductos()
    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())
    def LlenarDeProductos(self):
        self.conection.reconnect()
        resultados = self.productManager.ReadSimplified()
        if self.descargarImagenes:
            print(resultados)
            self.productManager.downloadImages(resultados)
        print(resultados)
        if self.scroll_layout is None:
            self.scroll_layout = QtWidgets.QVBoxLayout(self.mainWidget)
        for i in range(len(resultados)):
            if i % 3 == 0:
                self.row_layout = QtWidgets.QHBoxLayout()
                self.row_layouts.append(self.row_layout)
                self.scroll_layout.addLayout(self.row_layout)
            ventawidget = VentaWidget(f'../img/userImages/product_{resultados[i].nombre}.png',
                                      f'{resultados[i].nombre}',
                                      f'${resultados[i].precio}',
                                      'Agregar',
                                      'Eliminar',
                                      f"{resultados[i].id}",
                                      table=self.TablaVenta,
                                      labelTotal=self.LabelPrecioTotalDecimal)
            self.row_layout.addWidget(ventawidget)


class VentaWidget(QtWidgets.QWidget):
    def __init__(self, image_path, labelNombre_text : str, labelPrecio_text : str, button1_text : str,
                 button2_text : str, idProducto : int, table: QtWidgets.QTableWidget, labelTotal: QtWidgets.QLabel):
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
        self.table: QtWidgets.QTableWidget = table
        self.labelTotal = labelTotal
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        buttonAgregar.clicked.connect(self.AgregarProductoAVenta)
        buttonEliminar.clicked.connect(self.EliminarProductoDeTabla)
        self.validador = WidgetApoyo.ValidadorDeOfertas.Validador(self.idProducto, self.table, self)


    def AgregarProductoAVenta(self):
        # Obtener el subtotal actual
        yaexiste = False
        print(self.idProducto)
        if self.lineCantidad.text() != "":
            subtotal_actual = float(self.lineCantidad.text()) * float(self.precioProducto)
            IndiceNombre = self.BuscarEnTablaVentas(self.nombreProducto)
            if IndiceNombre != None:
                yaexiste = True
                print(f"Ya existe un producto con el nombre: {self.nombreProducto}")
            else:
                row_count = self.table.rowCount()
                self.table.insertRow(row_count)
            values = [self.nombreProducto, #nombre
                      self.lineCantidad.text(), #cantidad
                      str(self.precioProducto), #precio
                      str(subtotal_actual),  # Convertir a texto antes de agregar al QTableWidgetItem
                      str(self.idProducto)
                      ]
            self.validador.BuscarPromocionesRelacionadas(values)

            # Me arrepiento de todos mis cambios
            """"
            existente, index = self.buscarIndexEnTabla()
            if not existente:
                self.table.insertRow(row_count)
                for i in range(5):
                    self.table.setItem(row_count, i, QtWidgets.QTableWidgetItem(values[i]))
            else:
                self.table.item(index, 1).setText(str(float(self.table.item(index, 1).text()) + float(self.lineCantidad.text())))
            """
            if yaexiste:
                cantidadprevia = self.table.item(IndiceNombre, 1)
                self.table.setItem(IndiceNombre, 1, QtWidgets.QTableWidgetItem(str(int(cantidadprevia.text()) + int(values[1]))))
            if not yaexiste:
                for i in range(5):
                    self.table.setItem(row_count, i, QtWidgets.QTableWidgetItem(values[i]))
            self.ActualizarSubTotal()
            # Calcular el total actual sumando el subtotal actual al total anterior
            self.sacarTotal()
    def ActualizarSubTotal(self):
        if self.table.rowCount() > 0:
            for fila in range(self.table.rowCount()):
                cantidad = int(self.table.item(fila,1).text())
                precio = float(self.table.item(fila,2).text())
                nuevosubtotal = str(cantidad * precio)
                self.table.setItem(fila,3,QtWidgets.QTableWidgetItem(nuevosubtotal))
#funcion que devuelve el indice de la tabla en la que el nombre es igual a el dado
    def BuscarEnTablaVentas(self, name : str):
        if self.table.rowCount() > 0:
            for fila in range(self.table.rowCount()):
                if self.table.item(fila,0) != None:
                    nombreProducto = self.table.item(fila,0).text()
                else:
                    nombreProducto = None
                print(nombreProducto)
                if nombreProducto == name:
                    return fila
        return None

    def sacarTotal(self):
        total = 0
        if self.table.rowCount() > 0:
            for fila in range(self.table.rowCount()):
                if self.table.item(fila, 3) is not None:
                    total += float(self.table.item(fila, 3).text())
        self.labelTotal.setText(f"${total}")

    def EliminarProductoDeTabla(self):
        filaAEliminar = self.buscar_producto(self.nombreProducto)
        if filaAEliminar is not None:
            self.table.removeRow(filaAEliminar[1])
            self.sacarTotal()

    def buscar_producto(self, stringABuscar : str):
        texto_busqueda = stringABuscar.strip().lower()
        for fila in range(self.table.rowCount()-1, -1,-1):
            for columna in range(self.table.columnCount()):
                item = self.table.item(fila, columna)
                if item is not None and texto_busqueda in item.text().strip().lower():
                    return  (columna,fila)
    def calcularCantidad(self):
        pass

    def buscarIndexEnTabla(self):

        for i in range(self.table.rowCount()):
            if self.table.item(i,0) is not None and self.table.item(i, 0).text() == self.nombreProducto and float(self.table.item(i, 2).text()) == float(self.precioProducto):
                return True, i
        return False, -1

class CustomLineEditVentas(QtWidgets.QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Con esto ya hago lo del rango
        self.setRange(1, 30)
        # Poner en defecto 1
        self.setValue(1)

        # Configura la validación de entrada para permitir solo números enteros
        #self.setValidator(QtGui.QIntValidator())

        # Establece la longitud máxima de caracteres
        #self.setMaxLength(2)  # Aquí se establece en 2 para limitar a un máximo de 25
        #self.textChanged.connect(self.limitar_a_25)
    def limitar_a_25(self):
        # Verifica si el valor actual es mayor a 25
        if self.text() and int(self.text()) > 25:
            # Si es mayor a 25, establece el valor a 25
            self.setValue(25)
        if self.text() and int(self.text()) <= 0:
            self.setValue(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Venta()
    ui.show()
    sys.exit(app.exec_())
