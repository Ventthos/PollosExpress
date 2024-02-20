from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from RawInterfaces.WidgetApoyo import InterfazBusquedaProductos, WidgetProducto


class WidgetProduct(WidgetProducto.Ui_Form, QWidget):
    def __init__(self, img, titulo, precio, id):
        super().__init__()
        self.setupUi(self)
        self.imagen_producto_widget.setPixmap(QPixmap(img))
        self.nombre_producto_widget.setText(titulo)
        self.precio_producto_widget.setText(str(precio))
        self.id = id
        self.boton_agregar_producto_widget.clicked.connect(self.cambiarTextoBoton)

    def cambiarTextoBoton(self):
        if self.boton_agregar_producto_widget.isChecked():
            self.boton_agregar_producto_widget.setText("Eliminar")
        else:
            self.boton_agregar_producto_widget.setText("Agregar")

class InterfazBusquedaProducto(InterfazBusquedaProductos.Ui_Form, QWidget):
    def __init__(self, padre):
        super().__init__()
        self.setupUi(self)
        self.padre = padre
        self.pushButton_agregar_productos_busqueda.clicked.connect(self.returnProducts)

    def clearGrid(self):
        for i in range(self.gridLayout.rowCount()):
            for j in range(self.gridLayout.columnCount()):
                widget: QWidget = self.gridLayout.itemAtPosition(i,j)
                if widget is not None:
                    widget = widget.widget()
                    widget.hide()
                    self.gridLayout.removeWidget(widget)
                    widget.destroy()

    def cargarProductos(self, productos):
        self.clearGrid()
        i = 0
        j = 0
        for producto in productos:
            if i == 3:
                i = 0
                j += 1
            print(i)
            print(j)
            productoCargado = WidgetProduct("../img/noImage.jpg", producto.nombre, producto.precio, producto.id)
            self.gridLayout.addWidget(productoCargado, j, i, Qt.AlignHCenter)
            i += 1

    def returnProducts(self):
        productosChecked = []
        for i in range(self.gridLayout.count()):
            widget: WidgetProduct = self.gridLayout.itemAt(i).widget()
            if widget.boton_agregar_producto_widget.isChecked():
                productosChecked.append((None, widget.id, 1, None, widget.nombre_producto_widget.text()))
        print(productosChecked)
        self.padre.appendRowsToTable(productosChecked)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = WidgetProduct("../../img/noImage.jpg", "Waos", 433, 1)
    Form.show()
    sys.exit(app.exec_())