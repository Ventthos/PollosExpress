from PyQt5 import QtWidgets, QtGui
from RawInterfaces.Empleados import Ui_Form


class Empleados(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.iconoBuscar.setPixmap(QtGui.QPixmap("../img/lupa.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Empleados()
    ui.show()
    sys.exit(app.exec_())
