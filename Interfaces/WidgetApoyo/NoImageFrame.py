from RawInterfaces.WidgetApoyo.NoImageFrame import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap

class NoImageFrame(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.punto.setPixmap(QPixmap("../../img/dot.png"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = NoImageFrame()
    Form.show()
    sys.exit(app.exec_())
