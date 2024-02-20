from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QPushButton, QLineEdit
from PyQt5 import QtCore
from PyQt5 import QtGui
from RawInterfaces.Productos import Ui_Form
import mysql.connector
from Crud.CRUD_producto import CrudProducto, Producto
from Interfaces.WidgetApoyo.NoImageFrame import ImageFrame
from Interfaces.WidgetApoyo.WidgetsProducto import WidgetProduct, InterfazBusquedaProducto
import os

from tkinter import messagebox

class ProductosInterface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.cursor = self.__conection.cursor()
        self.__productManager = CrudProducto(conection=self.__conection)
        self.setupUi(self)
        self.verticalLayout_6.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_producto.hide()
        self.__updateProductos()

        #solo para saber que imagen esta activa y que producto
        self.activeImage = ""
        self.productoActivo: Producto

        #Boton para agregar producto
        self.botonAgregarProducto = QPushButton()
        self.botonAgregarProducto.setText("Crear producto")
        self.botonAgregarProducto.clicked.connect(self.crearProducto)
        self.horizontalLayout_4.addWidget(self.botonAgregarProducto)
        self.botonAgregarProducto.hide()


        # Linkear eventos para agregar producto
        self.checkBox_paquete_producto.clicked.connect(self.checkBox_activar_paquetes)
        self.agregar_producto.clicked.connect(self.configure_agregar_producto)

        # Ventana para poder seleccionar los productos de un paquete
        self.ventanaProductosPaquete = InterfazBusquedaProducto(self)
        self.agregar_producto_paquete.clicked.connect(self.mostrarProductosParaPaquete)

    def __updateProductos(self):
        self.__conection.reconnect()
        for file in os.listdir("../img/userImages"):
            f = os.path.join(".../img/userImages", file)
            os.remove(f)

        productos:list[Producto] = self.__productManager.ReadSimplified()
        for producto in productos:
            print(producto)
            nuevoElemento = ImageFrame(producto.nombre, data=producto)
            nuevoElemento.add_event(self.showProducto)
            self.verticalLayout_6.addWidget(nuevoElemento)

    def showProducto(self, widget: ImageFrame):
        # Aqui pone datos generales de todos los productos, independientemente de si es paquete o no
        if self.scrollArea_producto.isHidden():
            self.scrollArea_producto.show()
        data: Producto = widget.data
        self.productoActivo = data
        self.lineEdit_nombre_producto.setText(data.nombre)
        self.lineEdit_precio_producto.setText(str(data.precio))
        self.textEdit_desripcion_producto.setText(data.descripcion)
        self.imagen_producto_producto.setPixmap(QtGui.QPixmap("../img/noImage.jpg"))

        # Activar botones de agregar y editar
        if self.editar_producto.isHidden():
            self.editar_producto.show()
            self.eliminar_producto.show()
            self.botonAgregarProducto.hide()

        # Aqui decide que si es paquete, activara la tabla de paquetes
        if not data.esPaquete:
            self.checkBox_paquete_producto.hide()
            self.table_productos_paquete.hide()
            self.agregar_producto_paquete.hide()
        else:
            self.checkBox_paquete_producto.setChecked(True)
            self.checkBox_paquete_producto.setEnabled(False)
            self.checkBox_paquete_producto.show()
            self.table_productos_paquete.show()
            self.agregar_producto_paquete.show()
            self.table_productos_paquete.setRowCount(0)

            # Poner los productos en la tabla
            self.appendRowsToTable(data.productosPaquete)

    def checkBox_activar_paquetes(self):
        if self.checkBox_paquete_producto.isChecked():
            self.table_productos_paquete.show()
            self.agregar_producto_paquete.show()
        else:
            self.table_productos_paquete.hide()
            self.agregar_producto_paquete.hide()

    def configure_agregar_producto(self):
        if self.scrollArea_producto.isHidden():
            self.scrollArea_producto.show()
        if not self.table_productos_paquete.isHidden():
            self.table_productos_paquete.hide()
            self.agregar_producto_paquete.hide()
        self.checkBox_paquete_producto.show()
        self.checkBox_paquete_producto.setEnabled(True)

        # Borrar botones que no son necesarios
        if self.botonAgregarProducto.isHidden():
            self.editar_producto.hide()
            self.eliminar_producto.hide()
            self.botonAgregarProducto.show()

        # Limpiar toda la entrada
        self.lineEdit_nombre_producto.setText("")
        self.lineEdit_precio_producto.setText("")
        self.imagen_producto_producto.setPixmap(QtGui.QPixmap("../img/noImage.jpg"))
        self.textEdit_desripcion_producto.setText("")
        self.table_productos_paquete.setRowCount(0)
        self.checkBox_paquete_producto.setChecked(False)

    def __crearObjetoProducto(self) -> Producto:
        try:
            float(self.lineEdit_precio_producto.text())
        except ValueError:
            messagebox.showerror("Error", "El precio ingresado es invalido")
        else:
            newProduct = Producto(
                self.lineEdit_nombre_producto.text(),
                self.textEdit_desripcion_producto.toPlainText(),
                float(self.lineEdit_precio_producto.text()),
                self.checkBox_paquete_producto.isChecked(),
                imagen= "xd",
                driveCode= "xd"
                #imagen=self.__activeImage,
                #driveCode=self.__productManager.UploadImage(self.__activeImage)["id"]
            )
            return newProduct

    def mostrarProductosParaPaquete(self):
        ids = []
        productosNoSeleccionados = []
        for i in range(self.table_productos_paquete.rowCount()):
            ids.append(int(self.table_productos_paquete.item(i, 3).text()))

        ids.append(self.productoActivo.id)
        for i in range(self.verticalLayout_6.count()):
            if (self.verticalLayout_6.itemAt(i).widget().data.id not in ids
                    and not self.verticalLayout_6.itemAt(i).widget().data.esPaquete):
                productosNoSeleccionados.append(self.verticalLayout_6.itemAt(i).widget().data)
        self.ventanaProductosPaquete.cargarProductos(productosNoSeleccionados)
        self.ventanaProductosPaquete.show()

    def crearProducto(self):
        try:
            self.__productManager.Create(self.__crearObjetoProducto())
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Ocurrió un error al crear el producto, cheque los datos "
                                          "ingresados e intente de nuevo")
        else:
            if self.productoActivo.esPaquete:
                ids = []
                for i in range(self.table_productos_paquete.rowCount()):
                    ids.append(int(self.table_productos_paquete.item(i, 3).text()))
                self.__productManager.agregarProductosPaquete(self.productoActivo.id, ids)

    def appendRowsToTable(self, products):
        i = self.table_productos_paquete.rowCount()
        self.table_productos_paquete.setRowCount(self.table_productos_paquete.rowCount() + len(products))

        for producto in products:
            print(producto)
            nombreProducto = QTableWidgetItem(producto[4])
            cantidadProducto = QLineEdit()
            cantidadProducto.setText(str(producto[2]))
            botonEliminar = QPushButton()
            botonEliminar.setText("Eliminar")
            idProducto = QTableWidgetItem(str(producto[1]))

            self.table_productos_paquete.setItem(i, 0, nombreProducto)
            self.table_productos_paquete.setCellWidget(i, 1, cantidadProducto)
            self.table_productos_paquete.setCellWidget(i, 2, botonEliminar)
            self.table_productos_paquete.setItem(i, 3, idProducto)
            i += 1

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ProductosInterface()
    ui.show()
    sys.exit(app.exec_())