import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from RawInterfaces.Venta import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import mysql.connector

class Venta(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        mainWidget = QtWidgets.QWidget()
        self.scrollAreaProducto.setWidget(mainWidget)
        scroll_layout = QtWidgets.QVBoxLayout(mainWidget)
        for i in range(10):
            if i % 3 == 0:
                row_layout = QtWidgets.QHBoxLayout()
                scroll_layout.addLayout(row_layout)
            custom_widget = VentaWidget('image.jpg', f'Label {i}', 'Button 1', 'Button 2')
            row_layout.addWidget(custom_widget)

class VentaWidget(QtWidgets.QWidget):
    def __init__(self, image_path, label_text, button1_text, button2_text):
        super().__init__()
        self.initUI(image_path, label_text, button1_text, button2_text)

    def initUI(self, image_path, label_text, button1_text, button2_text):
        layout = QtWidgets.QVBoxLayout()

        # Image
        pixmap = QPixmap(image_path)
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        # Label
        label = QtWidgets.QLabel(label_text)
        layout.addWidget(label)

        # Buttons
        button1 = QtWidgets.QPushButton(button1_text)
        button2 = QtWidgets.QPushButton(button2_text)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        layout.addLayout(button_layout)

        self.setLayout(layout)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Venta()
    ui.show()
    sys.exit(app.exec_())