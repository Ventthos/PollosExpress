from RawInterfaces.MainMenuAdmin import Ui_MainWindowMenuAdmin
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from  PyQt5.QtGui import QPixmap,QIcon

from Interfaces.Productos import ProductosInterface
from Interfaces.Empleados import Empleados
from Interfaces.Promociones import Promociones
from Interfaces.admin_gastos import Admin_Gastos
from Interfaces.Admin_Ventas import Admin_Ventas
from Interfaces.admin_inventario import Admin_Inventario
from Interfaces.Venta import Venta

class MainMenu(QMainWindow, Ui_MainWindowMenuAdmin):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ToDo Falta hacer la distincion entre empleado y admin
        # Personalizar los botones de la interfaz con sus imagenes
        self.BotonMiniMenu.setText("")
        self.BotonMiniMenu.setIcon(QIcon("../img/MiniMenuSymbol.png"))
        self.BotonMiniMenu_2.setText("")
        self.BotonMiniMenu_2.setIcon(QIcon("../img/MiniMenuSymbol.png"))
        self.label_imagen_admin.setPixmap(QPixmap("../img/Admin.png"))
        self.AdministrarProductos.setIcon(QIcon("../img/Products.png"))
        self.AdministrarEmpleados.setIcon(QIcon("../img/Empleados.png"))
        self.AdministrarPromociones.setIcon(QIcon("../img/PromocionesIcon.png"))
        self.AdministrarVentas.setIcon(QIcon("../img/Venta.png"))
        self.AdministrarGastos.setIcon(QIcon("../img/GASTOS.png"))
        self.Estadisticas.setIcon(QIcon("../img/Estadisticas.png"))
        self.InventarioButton.setIcon(QIcon("../img/Invernario.png"))
        self.Vender.setIcon(QIcon("../img/VenderIcon.png"))

        # Hacer que los botones del menu aparenten que aplian el menu
        self.BarraHerramientas.hide()
        self.BotonMiniMenu.clicked.connect(self.activarMiniMenu)
        self.BotonMiniMenu_2.clicked.connect(self.activarMiniMenu)
        self.HomeButton.setIcon(QIcon("../img/HomeMenu.png"))

        # Hacer que la imagen del menu grande sea el logo de PollosExpress
        self.MenuGrandeImagen.setPixmap(QPixmap("../img/logo.png"))

        # Conectar interfaces a el menu principal
        self.stackedWidget.insertWidget(1, ProductosInterface())
        self.stackedWidget.insertWidget(2, Empleados())
        self.stackedWidget.insertWidget(3, Promociones())
        self.stackedWidget.insertWidget(4, Admin_Ventas())
        self.stackedWidget.insertWidget(5, Admin_Gastos())
        self.stackedWidget.insertWidget(6, Admin_Gastos()) # Cambiar este a la interfaz de estadísticas luego
        self.stackedWidget.insertWidget(7, Admin_Inventario())
        self.stackedWidget.insertWidget(8, Venta())

        # Conectar los eventos del menu a abrir las ventanas
        # ToDo falta por poner ventas y estadisticas
        self.HomeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.AdministrarProductos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.AdministrarEmpleados.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.AdministrarPromociones.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.AdministrarGastos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.InventarioButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.Vender.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))


    def activarMiniMenu(self):
        if self.BarraHerramientas.isHidden():
            self.BarraHerramientas.show()
            self.BarraDeHerramientoMini.hide()
        else:
            self.BarraHerramientas.hide()
            self.BarraDeHerramientoMini.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec_())