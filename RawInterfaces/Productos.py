# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RawInterfaces\Productos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(946, 617)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background_producto = QtWidgets.QWidget(Form)
        self.background_producto.setStyleSheet("#background_producto{\n"
"    border-image: url(../img/Producto.png);\n"
"}")
        self.background_producto.setObjectName("background_producto")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.background_producto)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listado_producto = QtWidgets.QWidget(self.background_producto)
        self.listado_producto.setStyleSheet("#listado_producto{\n"
"    background-color: #185791;\n"
"    border-radius: 14px;\n"
"    \n"
"}\n"
"\n"
"#scrollAreaWidgetContents_product{\n"
"    background-color:white;\n"
"}\n"
"\n"
"#iconoBuscar_producto{\n"
"    background-color: white;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"\n"
"}\n"
"\n"
"#agregar_producto{\n"
"    \n"
"}")
        self.listado_producto.setObjectName("listado_producto")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.listado_producto)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.listado_producto)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iconoBuscar_producto = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconoBuscar_producto.sizePolicy().hasHeightForWidth())
        self.iconoBuscar_producto.setSizePolicy(sizePolicy)
        self.iconoBuscar_producto.setMaximumSize(QtCore.QSize(26, 40))
        self.iconoBuscar_producto.setStyleSheet("#iconoBuscar{\n"
"    background-color: #FFFFFF;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    padding: 4px;\n"
"}")
        self.iconoBuscar_producto.setScaledContents(True)
        self.iconoBuscar_producto.setWordWrap(True)
        self.iconoBuscar_producto.setObjectName("iconoBuscar_producto")
        self.horizontalLayout_2.addWidget(self.iconoBuscar_producto)
        self.barraBusqueda_Productos = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.barraBusqueda_Productos.setFont(font)
        self.barraBusqueda_Productos.setStyleSheet("#barraBusqueda_Productos{\n"
"    background-color: #FFFFFF;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    color: white;\n"
"    padding: 4px;\n"
"}")
        self.barraBusqueda_Productos.setObjectName("barraBusqueda_Productos")
        self.horizontalLayout_2.addWidget(self.barraBusqueda_Productos)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea_productos = QtWidgets.QScrollArea(self.listado_producto)
        self.scrollArea_productos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_productos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_productos.setWidgetResizable(True)
        self.scrollArea_productos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_productos.setObjectName("scrollArea_productos")
        self.scrollAreaWidgetContents_productos = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_productos.setGeometry(QtCore.QRect(0, 0, 306, 452))
        self.scrollAreaWidgetContents_productos.setObjectName("scrollAreaWidgetContents_productos")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_productos)
        self.verticalLayout_6.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_productos.setWidget(self.scrollAreaWidgetContents_productos)
        self.verticalLayout_2.addWidget(self.scrollArea_productos)
        self.agregar_producto = QtWidgets.QPushButton(self.listado_producto)
        self.agregar_producto.setStyleSheet("\n"
"#agregar_producto {\n"
"    background-color: #e73a4b;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"padding:8px;\n"
"}\n"
"\n"
"#agregar_producto:hover {\n"
"    background-color: #EC5B69;\n"
"}")
        self.agregar_producto.setObjectName("agregar_producto")
        self.verticalLayout_2.addWidget(self.agregar_producto)
        self.horizontalLayout.addWidget(self.listado_producto)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.datos_producto = QtWidgets.QWidget(self.background_producto)
        self.datos_producto.setStyleSheet("#widget{\n"
"    margin-left: 20px;\n"
"}")
        self.datos_producto.setObjectName("datos_producto")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.datos_producto)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_producto = QtWidgets.QScrollArea(self.datos_producto)
        self.scrollArea_producto.setStyleSheet("")
        self.scrollArea_producto.setWidgetResizable(True)
        self.scrollArea_producto.setObjectName("scrollArea_producto")
        self.scrollArea_producto_contents = QtWidgets.QWidget()
        self.scrollArea_producto_contents.setGeometry(QtCore.QRect(0, -69, 473, 644))
        self.scrollArea_producto_contents.setStyleSheet("#scrollArea_producto_contents{\n"
"    background-color: white;\n"
"}\n"
"\n"
"#scrollArea_producto_contents QLineEdit, #scrollArea_producto_contents QTextEdit{\n"
"    background-color: #D9D9D9;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    border: 1px solid black; \n"
"} ")
        self.scrollArea_producto_contents.setObjectName("scrollArea_producto_contents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollArea_producto_contents)
        self.verticalLayout_4.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_nombre_producto = QtWidgets.QWidget(self.scrollArea_producto_contents)
        self.widget_nombre_producto.setStyleSheet("#scrollArea_producto{\n"
"    border-radius: 4px;\n"
"}")
        self.widget_nombre_producto.setObjectName("widget_nombre_producto")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_nombre_producto)
        self.horizontalLayout_3.setSpacing(11)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_nombre_producto_2 = QtWidgets.QWidget(self.widget_nombre_producto)
        self.widget_nombre_producto_2.setObjectName("widget_nombre_producto_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_nombre_producto_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_nombre_producto = QtWidgets.QLabel(self.widget_nombre_producto_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_nombre_producto.setFont(font)
        self.label_nombre_producto.setObjectName("label_nombre_producto")
        self.verticalLayout_5.addWidget(self.label_nombre_producto, 0, QtCore.Qt.AlignTop)
        self.lineEdit_nombre_producto = QtWidgets.QLineEdit(self.widget_nombre_producto_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_nombre_producto.setFont(font)
        self.lineEdit_nombre_producto.setObjectName("lineEdit_nombre_producto")
        self.verticalLayout_5.addWidget(self.lineEdit_nombre_producto, 0, QtCore.Qt.AlignTop)
        self.label_precio_producto = QtWidgets.QLabel(self.widget_nombre_producto_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_precio_producto.setFont(font)
        self.label_precio_producto.setObjectName("label_precio_producto")
        self.verticalLayout_5.addWidget(self.label_precio_producto)
        self.lineEdit_precio_producto = QtWidgets.QLineEdit(self.widget_nombre_producto_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_precio_producto.setFont(font)
        self.lineEdit_precio_producto.setObjectName("lineEdit_precio_producto")
        self.verticalLayout_5.addWidget(self.lineEdit_precio_producto)
        self.horizontalLayout_3.addWidget(self.widget_nombre_producto_2, 0, QtCore.Qt.AlignTop)
        self.widget_imagen_producto = QtWidgets.QWidget(self.widget_nombre_producto)
        self.widget_imagen_producto.setObjectName("widget_imagen_producto")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_imagen_producto)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_tituloimagen_producto = QtWidgets.QLabel(self.widget_imagen_producto)
        self.label_tituloimagen_producto.setObjectName("label_tituloimagen_producto")
        self.verticalLayout_7.addWidget(self.label_tituloimagen_producto, 0, QtCore.Qt.AlignRight)
        self.imagen_producto_producto = QtWidgets.QLabel(self.widget_imagen_producto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagen_producto_producto.sizePolicy().hasHeightForWidth())
        self.imagen_producto_producto.setSizePolicy(sizePolicy)
        self.imagen_producto_producto.setMinimumSize(QtCore.QSize(190, 158))
        self.imagen_producto_producto.setScaledContents(True)
        self.imagen_producto_producto.setWordWrap(False)
        self.imagen_producto_producto.setObjectName("imagen_producto_producto")
        self.verticalLayout_7.addWidget(self.imagen_producto_producto, 0, QtCore.Qt.AlignRight)
        self.boton_cambiarimg_producto = QtWidgets.QPushButton(self.widget_imagen_producto)
        self.boton_cambiarimg_producto.setStyleSheet("#boton_cambiarimg_producto{\n"
"    background-color: #737373;\n"
"    color: white;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"\n"
"#boton_cambiarimg_producto::hover{\n"
"    background-color: #c8c8c8;\n"
"}")
        self.boton_cambiarimg_producto.setObjectName("boton_cambiarimg_producto")
        self.verticalLayout_7.addWidget(self.boton_cambiarimg_producto, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_3.addWidget(self.widget_imagen_producto)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.widget_nombre_producto)
        self.widget_descripcion_producto = QtWidgets.QWidget(self.scrollArea_producto_contents)
        self.widget_descripcion_producto.setObjectName("widget_descripcion_producto")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_descripcion_producto)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_descripcion_producto = QtWidgets.QLabel(self.widget_descripcion_producto)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_descripcion_producto.setFont(font)
        self.label_descripcion_producto.setObjectName("label_descripcion_producto")
        self.verticalLayout_8.addWidget(self.label_descripcion_producto)
        self.textEdit_desripcion_producto = QtWidgets.QTextEdit(self.widget_descripcion_producto)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_desripcion_producto.setFont(font)
        self.textEdit_desripcion_producto.setObjectName("textEdit_desripcion_producto")
        self.verticalLayout_8.addWidget(self.textEdit_desripcion_producto)
        self.verticalLayout_4.addWidget(self.widget_descripcion_producto)
        self.widget_paquete_producto = QtWidgets.QWidget(self.scrollArea_producto_contents)
        self.widget_paquete_producto.setObjectName("widget_paquete_producto")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_paquete_producto)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_paquete_producto = QtWidgets.QCheckBox(self.widget_paquete_producto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_paquete_producto.setFont(font)
        self.checkBox_paquete_producto.setObjectName("checkBox_paquete_producto")
        self.verticalLayout_9.addWidget(self.checkBox_paquete_producto)
        self.table_productos_paquete = QtWidgets.QTableWidget(self.widget_paquete_producto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_productos_paquete.sizePolicy().hasHeightForWidth())
        self.table_productos_paquete.setSizePolicy(sizePolicy)
        self.table_productos_paquete.setStyleSheet("#table_productos_paquete QPushButton{\n"
"    background-color: #185791;\n"
"    border: 2px solid #083d6e;\n"
"    color: white;\n"
"    font-weight: Bold;\n"
"}\n"
"\n"
"#table_productos_paquete QPushButton::hover{\n"
"    background-color: #5ea3e3;\n"
"}\n"
"")
        self.table_productos_paquete.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_productos_paquete.setShowGrid(True)
        self.table_productos_paquete.setGridStyle(QtCore.Qt.SolidLine)
        self.table_productos_paquete.setRowCount(0)
        self.table_productos_paquete.setColumnCount(4)
        self.table_productos_paquete.setObjectName("table_productos_paquete")
        item = QtWidgets.QTableWidgetItem()
        self.table_productos_paquete.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_productos_paquete.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_productos_paquete.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_productos_paquete.setHorizontalHeaderItem(3, item)
        self.table_productos_paquete.horizontalHeader().setVisible(True)
        self.table_productos_paquete.horizontalHeader().setCascadingSectionResizes(True)
        self.table_productos_paquete.horizontalHeader().setDefaultSectionSize(112)
        self.table_productos_paquete.horizontalHeader().setHighlightSections(True)
        self.table_productos_paquete.horizontalHeader().setSortIndicatorShown(False)
        self.table_productos_paquete.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_9.addWidget(self.table_productos_paquete)
        self.agregar_producto_paquete = QtWidgets.QPushButton(self.widget_paquete_producto)
        self.agregar_producto_paquete.setStyleSheet("#agregar_producto_paquete{\n"
"    background-color: #02a64d;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"#agregar_producto_paquete::hover{\n"
"    background-color: #54a67b;\n"
"}")
        self.agregar_producto_paquete.setObjectName("agregar_producto_paquete")
        self.verticalLayout_9.addWidget(self.agregar_producto_paquete)
        self.widget_botones_producto = QtWidgets.QWidget(self.widget_paquete_producto)
        self.widget_botones_producto.setStyleSheet("#widget_botones_producto QPushButton{\n"
"    background-color: #e73a4b;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#widget_botones_producto QPushButton:Hover{\n"
"    background-color: #EC5B69;\n"
"}")
        self.widget_botones_producto.setObjectName("widget_botones_producto")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_botones_producto)
        self.horizontalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editar_producto = QtWidgets.QPushButton(self.widget_botones_producto)
        self.editar_producto.setObjectName("editar_producto")
        self.horizontalLayout_4.addWidget(self.editar_producto)
        self.eliminar_producto = QtWidgets.QPushButton(self.widget_botones_producto)
        self.eliminar_producto.setObjectName("eliminar_producto")
        self.horizontalLayout_4.addWidget(self.eliminar_producto)
        self.verticalLayout_9.addWidget(self.widget_botones_producto)
        self.verticalLayout_4.addWidget(self.widget_paquete_producto)
        self.scrollArea_producto.setWidget(self.scrollArea_producto_contents)
        self.verticalLayout_3.addWidget(self.scrollArea_producto)
        self.horizontalLayout.addWidget(self.datos_producto)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout.addWidget(self.background_producto)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.iconoBuscar_producto.setText(_translate("Form", "aaaaa"))
        self.barraBusqueda_Productos.setPlaceholderText(_translate("Form", "Buscar Producto"))
        self.agregar_producto.setText(_translate("Form", "Agregar producto"))
        self.label_nombre_producto.setText(_translate("Form", "Nombre"))
        self.label_precio_producto.setText(_translate("Form", "Precio"))
        self.label_tituloimagen_producto.setText(_translate("Form", "Imagen"))
        self.imagen_producto_producto.setText(_translate("Form", "TextLabel"))
        self.boton_cambiarimg_producto.setText(_translate("Form", "Cambiar imagen"))
        self.label_descripcion_producto.setText(_translate("Form", "Descripción"))
        self.checkBox_paquete_producto.setText(_translate("Form", "Paquete"))
        self.table_productos_paquete.setSortingEnabled(False)
        item = self.table_productos_paquete.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Producto"))
        item = self.table_productos_paquete.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cantidad"))
        item = self.table_productos_paquete.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Id"))
        self.agregar_producto_paquete.setText(_translate("Form", "Agregar producto al paquete"))
        self.editar_producto.setText(_translate("Form", "Guardar cambios"))
        self.eliminar_producto.setText(_translate("Form", "Eliminar producto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
