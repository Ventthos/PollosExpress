from RawInterfaces.MainMenuAdmin import Ui_MainWindowMenuAdmin
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap,QIcon, QFont, QCursor
from PyQt5 import QtCore

from Interfaces.Venta import Venta


class MainMenu(QMainWindow, Ui_MainWindowMenuAdmin):
    def __init__(self, admin, idUser, userName):
        super().__init__()
        super().setupUi(self)

        self.BotonMiniMenu.setText("")
        self.BotonMiniMenu.setIcon(QIcon("../img/MiniMenuSymbol.png"))
        self.BotonMiniMenu_2.setText("")
        self.BotonMiniMenu_2.setIcon(QIcon("../img/MiniMenuSymbol.png"))
        self.Vender.setIcon(QIcon("../img/VenderIcon.png"))

        # Hacer que los botones del menu aparenten que aplian el menu
        self.BarraHerramientas.hide()
        self.BotonMiniMenu.clicked.connect(self.activarMiniMenu)
        self.BotonMiniMenu_2.clicked.connect(self.activarMiniMenu)
        self.HomeButton.setIcon(QIcon("../img/HomeMenu.png"))

        # Poner el nombre del Empleado Para que se sienta feliz
        self.LabelEmpleado.setText(f"Bienvenido {userName}")

        # Hacer que la imagen del menu grande sea el logo de PollosExpress
        self.MenuGrandeImagen.setPixmap(QPixmap("../img/logo.png"))

        # Linkear a Home
        self.HomeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))


        if admin:
            # ToDo Falta hacer la distincion entre empleado y admin
            # Personalizar los botones de la interfaz con sus imagenes

            self.label_imagen_admin.setPixmap(QPixmap("../img/Admin.png"))
            self.AdministrarProductos.setIcon(QIcon("../img/Products.png"))
            self.AdministrarEmpleados.setIcon(QIcon("../img/Empleados.png"))
            self.AdministrarPromociones.setIcon(QIcon("../img/PromocionesIcon.png"))
            self.AdministrarVentas.setIcon(QIcon("../img/Venta.png"))
            self.AdministrarGastos.setIcon(QIcon("../img/GASTOS.png"))
            self.Estadisticas.setIcon(QIcon("../img/Estadisticas.png"))
            self.InventarioButton.setIcon(QIcon("../img/Invernario.png"))

            # Imports
            from Interfaces.Productos import ProductosInterface
            from Interfaces.Empleados import Empleados
            from Interfaces.Promociones import Promociones
            from Interfaces.admin_gastos import Admin_Gastos
            from Interfaces.Admin_Ventas import Admin_Ventas
            from Interfaces.admin_inventario import Admin_Inventario
            from Interfaces.Analisis import Analisis

            # Conectar interfaces a el menu principal
            self.stackedWidget.insertWidget(1, ProductosInterface())
            self.stackedWidget.insertWidget(2, Empleados())
            self.stackedWidget.insertWidget(3, Promociones())
            self.stackedWidget.insertWidget(4, Admin_Ventas())
            self.stackedWidget.insertWidget(5, Admin_Gastos())
            self.stackedWidget.insertWidget(6, Analisis())
            self.stackedWidget.insertWidget(7, Admin_Inventario())
            self.stackedWidget.insertWidget(8, Venta(False, idUser))

            # Conectar los eventos del menu a abrir las ventanas
            # ToDo falta por poner ventas y estadisticas

            self.AdministrarProductos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
            self.AdministrarEmpleados.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
            self.AdministrarPromociones.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
            self.AdministrarVentas.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
            self.AdministrarGastos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
            self.Estadisticas.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
            self.InventarioButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
            self.Vender.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))

        else:
            self.HeaderFuncionesAdmin.hide()
            self.verticalLayout_3.removeWidget(self.HeaderFuncionesAdmin)
            self.FuncionesAdmin.hide()
            self.verticalLayout_3.removeItem(self.spacerItem)
            self.verticalLayout_3.removeWidget(self.FuncionesAdmin)
            self.buttonGastosEmpleado = QPushButton()
            self.buttonGastosEmpleado.setText("Crear gastos")
            font = QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(11)
            self.buttonGastosEmpleado.setFont(font)
            self.verticalLayout_3.addWidget(self.buttonGastosEmpleado)
            self.buttonInventarioEmpleado = QPushButton()
            self.buttonInventarioEmpleado.setText("Ver inventario")
            self.buttonInventarioEmpleado.setFont(font)
            self.verticalLayout_3.addWidget(self.buttonInventarioEmpleado)

            spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem)

            # Iconos
            self.buttonInventarioEmpleado.setIcon(QIcon("../img/Invernario.png"))
            self.buttonInventarioEmpleado.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.buttonGastosEmpleado.setIcon(QIcon("../img/GASTOS.png"))
            self.buttonGastosEmpleado.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

            # Imports
            from Interfaces.gasteichons import RegistroGastos
            from Interfaces.Inventario import Inventario

            # Conectar interfaces a el menu principal
            self.stackedWidget.insertWidget(1, Venta(True))
            self.stackedWidget.insertWidget(2, RegistroGastos())
            self.stackedWidget.insertWidget(3, Inventario())

            # Linkear a botones
            self.Vender.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
            self.buttonGastosEmpleado.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
            self.buttonInventarioEmpleado.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

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
    ui = MainMenu(False, 1, "Tester")
    ui.show()
    sys.exit(app.exec_())
