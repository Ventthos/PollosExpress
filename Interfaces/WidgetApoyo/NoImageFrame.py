from RawInterfaces.WidgetApoyo.NoImageFrame import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap

class NoImageFrame(Ui_Form, QWidget):
    def __init__(self, texto, data):
        super().__init__()
        super().setupUi(self)
        self.punto.setPixmap(QPixmap("../img/dot.png"))
        self.nombre.setText(texto)
        self.data = data
        self.funcion = None

    def get_data(self):
        return self.data

    def add_event(self, function):
        self.funcion = function
        self.background.mousePressEvent = self.__lauch_function

    def __lauch_function(self, event):
        self.funcion(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = NoImageFrame("si")
    Form.show()
    sys.exit(app.exec_())
