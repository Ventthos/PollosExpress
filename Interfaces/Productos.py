from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QPushButton, QLineEdit
from PyQt5 import QtCore
from PyQt5 import QtGui
from RawInterfaces.Productos import Ui_Form
import mysql.connector
from Crud.CRUD_producto import CrudProducto, Producto
from Interfaces.WidgetApoyo.NoImageFrame import ImageFrame
from Interfaces.WidgetApoyo.WidgetsProducto import InterfazBusquedaProducto
import os
import threading
from WidgetApoyo.LoadingScreen import LoadingScreen
from tkinter import messagebox, filedialog

class ProductosInterface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3306",
        database="pollosexpress"
    )
        #Para la responsividad
        self.anchoReferencia = 946

        # Lista Productos
        self.productos = []

        self.cursor = self.__conection.cursor()
        self.__productManager = CrudProducto(conection=self.__conection)
        self.setupUi(self)
        self.verticalLayout_6.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_producto.hide()
        self.__updateProductos()

        # Poner el ícono de buscar en la barra
        self.iconoBuscar_producto.setPixmap(QtGui.QPixmap("../img/lupaNegra.png"))

        #solo para saber que imagen esta activa y que producto
        self.activeImage = ""
        self.productoActivo: Producto
        self.hasChangedImage = False
        self.boton_cambiarimg_producto.clicked.connect(self.changeImagen)
        self.creandoProducto = False

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

        # Para verificar si ha cambiado disponibilidades
        self.paqueteModificado = False

        # Para eliminar empleados
        self.eliminar_producto.clicked.connect(self.eliminarProducto)

        # Para editar producto
        self.editar_producto.clicked.connect(self.editProducto)

        # Linkear para buscar
        self.barraBusqueda_Productos.textChanged.connect(self.buscarProducto)

        # Linkear actualizar
        self.actualizar_productos.clicked.connect(self.actualizarConWarnig)

        #Validar que el producto no pueda tener un precio menor a 0
        self.lineEdit_precio_producto.textChanged.connect(self.validate_positive_number)


    def downloadImages(self, listaWigets: list[ImageFrame]):
        for widget in listaWigets:
            widgetData:Producto = widget.data
            self.__productManager.downloadImages(widgetData)
            widget.punto.setPixmap(QtGui.QPixmap(widgetData.imagen))

    def __updateProductos(self):
        print("Actualizando...")
        self.clearList()
        self.__conection.reconnect()
        for file in os.listdir("../img/userImages"):
            f = os.path.join("../img/userImages", file)
            os.remove(f)
        self.productos.clear()
        productos:list[Producto] = self.__productManager.ReadSimplified()
        listaWidgetsParaImagenes = []
        for producto in productos:
            self.productos.append(producto)
            nuevoElemento = ImageFrame(producto.nombre, data=producto)
            nuevoElemento.add_event(self.showProducto)
            self.verticalLayout_6.addWidget(nuevoElemento)
            listaWidgetsParaImagenes.append(nuevoElemento)
        hilo = threading.Thread(target=self.downloadImages, args=[listaWidgetsParaImagenes])
        hilo.start()

    def clearList(self):
        for i in range(self.verticalLayout_6.count()-1, -1, -1):
            widget = self.verticalLayout_6.itemAt(i).widget()
            self.verticalLayout_6.removeWidget(widget)
            widget.deleteLater()

    def showProducto(self, widget: ImageFrame):
        self.agregar_producto.setEnabled(True)
        self.creandoProducto = False
        self.paqueteModificado = False
        self.hasChangedImage = False
        # Aqui pone datos generales de todos los productos, independientemente de si es paquete o no
        if self.scrollArea_producto.isHidden():
            self.scrollArea_producto.show()
        data: Producto = widget.data
        self.productoActivo = data
        self.lineEdit_nombre_producto.setText(data.nombre)
        self.lineEdit_precio_producto.setText(str(data.precio))
        self.textEdit_desripcion_producto.setText(data.descripcion)
        ruta = ""
        if os.path.exists(data.imagen):
            ruta = data.imagen
        else:
            ruta = "../img/noImage.jpg"
        self.imagen_producto_producto.setPixmap(QtGui.QPixmap(ruta))
        self.lineEdit_precio_producto.setValidator(QtGui.QIntValidator(0, 100000))

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
        self.agregar_producto.setEnabled(False)
        self.creandoProducto = True
        self.paqueteModificado = False
        self.hasChangedImage = False
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
                imagen= self.activeImage,
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

        for i in range(self.verticalLayout_6.count()):
            if (self.verticalLayout_6.itemAt(i).widget().data.id not in ids
                    and not self.verticalLayout_6.itemAt(i).widget().data.esPaquete):
                productosNoSeleccionados.append(self.verticalLayout_6.itemAt(i).widget().data)
        self.ventanaProductosPaquete.cargarProductos(productosNoSeleccionados)
        self.ventanaProductosPaquete.show()

    def crearProducto(self):
        pantallaCarga = LoadingScreen()
        pantallaCarga.show()
        QApplication.processEvents()
        try:
            objetoProducto = self.__crearObjetoProducto()
            if self.creandoProducto or self.hasChangedImage:
                if self.activeImage == "":
                    drivecode = self.__productManager.UploadImage("../img/noImage.jpg")["id"]
                else:
                    drivecode = self.__productManager.UploadImage(self.activeImage)["id"]
            else:
                drivecode = self.productoActivo.driveCode
            objetoProducto.driveCode = drivecode
            self.__productManager.Create(objetoProducto)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Ocurrió un error al crear el producto, cheque los datos "
                                          "ingresados e intente de nuevo")
            pantallaCarga = None
        else:
            if self.checkBox_paquete_producto.isChecked():
                ultimoProducto = self.__productManager.getLastId()
                ids = []
                for i in range(self.table_productos_paquete.rowCount()):
                    ids.append((int(self.table_productos_paquete.item(i, 3).text()),
                               int(self.table_productos_paquete.cellWidget(i, 1).text())))
                self.__productManager.agregarProductosPaquete(ultimoProducto, ids)
            self.createProductoInInventory()
            self.__updateProductos()
            self.configure_agregar_producto()
            pantallaCarga = None
            messagebox.showinfo(title="Operación completada", message="El producto ha sido agregado con éxito")


    def appendRowsToTable(self, products):
        i = self.table_productos_paquete.rowCount()
        self.table_productos_paquete.setRowCount(self.table_productos_paquete.rowCount() + len(products))

        for producto in products:
            nombreProducto = QTableWidgetItem(producto[4])
            cantidadProducto = QLineEdit()
            cantidadProducto.setText(str(producto[2]))
            cantidadProducto.textChanged.connect(self.setChanged)
            botonEliminar = QPushButton()
            botonEliminar.setText("Eliminar")
            botonEliminar.clicked.connect(self.setChanged)
            idProducto = QTableWidgetItem(str(producto[1]))

            self.table_productos_paquete.setItem(i, 0, nombreProducto)
            self.table_productos_paquete.setCellWidget(i, 1, cantidadProducto)
            self.table_productos_paquete.setCellWidget(i, 2, botonEliminar)
            self.table_productos_paquete.setItem(i, 3, idProducto)
            i += 1

    def setChanged(self, event):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            point = self.table_productos_paquete.indexAt(sender.pos())
            row = point.row()
            self.table_productos_paquete.removeRow(row)
        self.paqueteModificado = True

    def editProducto(self):
        self.editar_producto.setEnabled(False)
        pantallaCarga = LoadingScreen()
        pantallaCarga.show()
        QApplication.processEvents()
        if self.paqueteModificado:
            self.__productManager.Delete(self.productoActivo.id)
            self.crearProducto()
            pantallaCarga = None
            self.editar_producto.setEnabled(True)
        else:
            objetoProducto = self.__crearObjetoProducto()
            if self.hasChangedImage:
                driveCode = self.__productManager.UploadImage(self.activeImage)["id"]
            else:
                driveCode = self.productoActivo.driveCode
            objetoProducto.driveCode = driveCode
            self.__productManager.Update(self.productoActivo.id, objetoProducto)
            self.__updateProductos()
            pantallaCarga = None
            self.editar_producto.setEnabled(True)


    def eliminarProducto(self):
        self.eliminar_producto.setEnabled(False)
        pantallaCarga = LoadingScreen()
        pantallaCarga.show()
        QApplication.processEvents()
        codigoDrive = self.productoActivo.driveCode
        self.__productManager.Delete(self.productoActivo.id)
        self.__productManager.DeleteImage(codigoDrive)
        self.productoActivo= None
        self.__updateProductos()
        if self.verticalLayout_6.count() > 0:
            self.showProducto(self.verticalLayout_6.itemAt(0).widget())
        else:
            self.configure_agregar_producto()
        pantallaCarga = None
        self.eliminar_producto.setEnabled(True)

    def changeImagen(self):
        ruta = filedialog.askopenfilename(filetypes=(("Imágenes", "*.jpg *.png"),))
        if ruta != "":
            self.hasChangedImage = True
            self.activeImage = ruta
            self.imagen_producto_producto.setPixmap(QtGui.QPixmap(self.activeImage))

    def createProductoInInventory(self):
        self.__conection.reconnect()
        self.__conection.commit()
        query1 = "SELECT id_producto, nombre FROM producto WHERE id_producto = (SELECT MAX(id_producto) FROM producto);"
        self.cursor.execute(query1)
        producto = self.cursor.fetchone()
        self.__conection.reconnect()
        query = f"INSERT INTO inventario VALUES(%s, %s, %s, %s, %s)"
        datos = (producto[0], producto[1], "--", 0, 0)
        self.cursor.execute(query, datos)
        self.__conection.commit()

    def buscarProducto(self):
        for widget in range(self.verticalLayout_6.count()-1,-1, -1):
            self.verticalLayout_6.itemAt(widget).widget().hide()
            self.verticalLayout_6.removeWidget(self.verticalLayout_6.itemAt(widget).widget())

        if self.barraBusqueda_Productos.text() != "":
            for producto in self.productos:
                if self.barraBusqueda_Productos.text().lower() in producto.nombre.lower():
                    newElement = ImageFrame(f"{producto.nombre}", producto, producto.imagen)
                    newElement.add_event(self.showProducto)
                    self.verticalLayout_6.addWidget(newElement)
        else:
            for producto in self.productos:
                newElement = ImageFrame(f"{producto.nombre}", producto, producto.imagen)
                newElement.add_event(self.showProducto)
                self.verticalLayout_6.addWidget(newElement)

    def validate_positive_number(self, text):
        if text and (not text.isdigit() or int(text) <= 0):
            cursor = self.lineEdit_precio_producto.cursorPosition()
            self.lineEdit_precio_producto.setText(text[:-1])  # Elimina el último carácter
            self.lineEdit_precio_producto.setCursorPosition(cursor - 1)  # Mantiene el cursor en su posición

    def actualizarConWarnig(self):
        self.actualizar_productos.setEnabled(False)
        self.__updateProductos()
        messagebox.showinfo("Actualizado", "Los datos del programa han sido actualizados")
        self.actualizar_productos.setEnabled(True)

    def resizeEvent(self, event):
        margins = int((9/self.anchoReferencia) * self.width())
        self.listado_producto.setContentsMargins(margins, margins, margins, margins)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(int((9 / self.anchoReferencia) * self.width()))
        self.barraBusqueda_Productos.setFont(font)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(int((11/self.anchoReferencia)*self.width()))
        self.label_nombre_producto.setFont(font)
        self.label_precio_producto.setFont(font)
        self.label_descripcion_producto.setFont(font)
        self.lineEdit_nombre_producto.setFont(font)
        self.lineEdit_precio_producto.setFont(font)
        self.checkBox_paquete_producto.setFont(font)

        font.setPointSize(int((8 / self.anchoReferencia) * self.width()))
        self.agregar_producto.setFont(font)
        self.actualizar_productos.setFont(font)
        self.agregar_producto_paquete.setFont(font)
        self.editar_producto.setFont(font)
        self.boton_cambiarimg_producto.setFont(font)
        self.eliminar_producto.setFont(font)

        font.setPointSize(int((10 / self.anchoReferencia) * self.width()))
        self.textEdit_desripcion_producto.setFont(font)

        # Para la imagen
        self.imagen_producto_producto.setMinimumSize(int((190/self.anchoReferencia)*self.width()),
                                                     int((158/self.anchoReferencia)*self.width()))

        # Para el icono de buscar
        self.iconoBuscar_producto.setMaximumSize(int((26/self.anchoReferencia)*self.width()),
                                                 int((40/self.anchoReferencia)*self.width()))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ProductosInterface()
    ui.show()
    sys.exit(app.exec_())