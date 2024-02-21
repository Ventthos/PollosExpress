from RawInterfaces.WidgetApoyo.NoImageFrame import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class NoImageFrame(Ui_Form, QWidget):
    def __init__(self, texto, data=None):
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


class ImageFrame(NoImageFrame):
    def __init__(self, texto, data=None, img=""):
        super().__init__(texto, data)
        self.punto.setMaximumWidth(66)
        self.punto.setMaximumHeight(55)
        self.nombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        if img == "":
            self.punto.setPixmap(QPixmap("../img/noImage.jpg"))
        else:
            self.punto.setPixmap(QPixmap(img))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = ImageFrame("si")
    Form.show()
    sys.exit(app.exec_())
