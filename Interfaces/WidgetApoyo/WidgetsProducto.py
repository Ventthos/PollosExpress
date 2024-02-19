from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from RawInterfaces.WidgetApoyo import InterfazBusquedaProductos, WidgetProducto


class WidgetProduct(WidgetProducto.Ui_Form, QWidget):
    def __init__(self, img, titulo, precio, id):
        super().__init__()
        self.setupUi(self)
        self.imagen_producto_widget.setPixmap(QPixmap(img))
        self.nombre_producto_widget.setText(titulo)
        self.precio_producto_widget.setText(str(precio))
        self.id = id

class InterfazBusquedaProducto(InterfazBusquedaProductos.Ui_Form, QWidget):
    def __init__(self, padre, productos):
        super().__init__()
        self.setupUi(self)
        self.padre = padre
        self.productos = productos

    def show_productos(self):
        for producto in self.productos:
            productoCargado = WidgetProducto()