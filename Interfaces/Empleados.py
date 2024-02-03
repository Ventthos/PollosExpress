from PyQt5 import QtWidgets, QtGui
from RawInterfaces.Empleados import Ui_Form


class Empleados(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.background.setStyleSheet("#background{border-image: url(../img/Empleado.png);}")

        self.iconoBuscar.setPixmap(QtGui.QPixmap("../img/lupa.png"))
        self.label.setPixmap(QtGui.QPixmap("../img/Icons/Telefono.png"))
        self.label_2.setPixmap(QtGui.QPixmap("../img/Icons/Sueldo.png"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Empleados()
    ui.show()
    sys.exit(app.exec_())
