from RawInterfaces.MainMenuAdmin import Ui_MainWindowMenuAdmin
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from  PyQt5.QtGui import QPixmap,QIcon

class MainMenu(QMainWindow, Ui_MainWindowMenuAdmin):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

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