# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RawInterfaces\WidgetApoyo\WidgetProducto.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 208)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fondo_cuadrado_busqueda = QtWidgets.QWidget(Form)
        self.fondo_cuadrado_busqueda.setStyleSheet("#fondo_cuadrado_busqueda{\n"
"    background-color:white;\n"
"    border-radius: 10px;\n"
"}")
        self.fondo_cuadrado_busqueda.setObjectName("fondo_cuadrado_busqueda")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fondo_cuadrado_busqueda)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imagen_producto_widget = QtWidgets.QLabel(self.fondo_cuadrado_busqueda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagen_producto_widget.sizePolicy().hasHeightForWidth())
        self.imagen_producto_widget.setSizePolicy(sizePolicy)
        self.imagen_producto_widget.setMinimumSize(QtCore.QSize(125, 98))
        self.imagen_producto_widget.setMaximumSize(QtCore.QSize(125, 98))
        self.imagen_producto_widget.setSizeIncrement(QtCore.QSize(1, 98))
        self.imagen_producto_widget.setScaledContents(True)
        self.imagen_producto_widget.setWordWrap(True)
        self.imagen_producto_widget.setObjectName("imagen_producto_widget")
        self.verticalLayout_2.addWidget(self.imagen_producto_widget, 0, QtCore.Qt.AlignHCenter)
        self.nombre_producto_widget = QtWidgets.QLabel(self.fondo_cuadrado_busqueda)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombre_producto_widget.setFont(font)
        self.nombre_producto_widget.setObjectName("nombre_producto_widget")
        self.verticalLayout_2.addWidget(self.nombre_producto_widget, 0, QtCore.Qt.AlignHCenter)
        self.precio_producto_widget = QtWidgets.QLabel(self.fondo_cuadrado_busqueda)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.precio_producto_widget.setFont(font)
        self.precio_producto_widget.setObjectName("precio_producto_widget")
        self.verticalLayout_2.addWidget(self.precio_producto_widget, 0, QtCore.Qt.AlignHCenter)
        self.boton_agregar_producto_widget = QtWidgets.QPushButton(self.fondo_cuadrado_busqueda)
        self.boton_agregar_producto_widget.setStyleSheet("#boton_agregar_producto_widget{\n"
"    background-color: #397bb8;\n"
"    border: none;\n"
"    padding: 6px;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#boton_agregar_producto_widget::hover{\n"
"    background-color: #b0cae3;\n"
"}\n"
"\n"
"#boton_agregar_producto_widget::checked{\n"
"    background-color: #74a3cd;\n"
"}")
        self.boton_agregar_producto_widget.setCheckable(True)
        self.boton_agregar_producto_widget.setChecked(False)
        self.boton_agregar_producto_widget.setObjectName("boton_agregar_producto_widget")
        self.verticalLayout_2.addWidget(self.boton_agregar_producto_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout.addWidget(self.fondo_cuadrado_busqueda)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.imagen_producto_widget.setText(_translate("Form", "TextLabel"))
        self.nombre_producto_widget.setText(_translate("Form", "TextLabel"))
        self.precio_producto_widget.setText(_translate("Form", "TextLabel"))
        self.boton_agregar_producto_widget.setText(_translate("Form", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
