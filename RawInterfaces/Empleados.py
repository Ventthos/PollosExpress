# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RawInterfaces\Empleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(856, 611)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background = QtWidgets.QWidget(Form)
        self.background.setStyleSheet("#background{\n"
"    background-color: purple;\n"
"}")
        self.background.setObjectName("background")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.background)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listado = QtWidgets.QWidget(self.background)
        self.listado.setStyleSheet("#listado{\n"
"    background-color: rgba(255, 255, 255, 210);\n"
"    border-radius: 14px;\n"
"    \n"
"}")
        self.listado.setObjectName("listado")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.listado)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.listado)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iconoBuscar = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconoBuscar.sizePolicy().hasHeightForWidth())
        self.iconoBuscar.setSizePolicy(sizePolicy)
        self.iconoBuscar.setMaximumSize(QtCore.QSize(29, 29))
        self.iconoBuscar.setStyleSheet("#iconoBuscar{\n"
"    background-color: #185791;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    padding: 4px;\n"
"}")
        self.iconoBuscar.setScaledContents(True)
        self.iconoBuscar.setObjectName("iconoBuscar")
        self.horizontalLayout_2.addWidget(self.iconoBuscar)
        self.barraBusqueda = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.barraBusqueda.setFont(font)
        self.barraBusqueda.setStyleSheet("#barraBusqueda{\n"
"    background-color: #185791;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    color: white;\n"
"    padding: 4px;\n"
"}")
        self.barraBusqueda.setObjectName("barraBusqueda")
        self.horizontalLayout_2.addWidget(self.barraBusqueda)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea = QtWidgets.QScrollArea(self.listado)
        self.scrollArea.setStyleSheet("#scrollArea{\n"
"    border: 0px solid black;\n"
"    border-radius: 14px;\n"
"}\n"
"#contenidoScroll{\n"
"    background-color: white;\n"
"    \n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.contenidoScroll = QtWidgets.QWidget()
        self.contenidoScroll.setGeometry(QtCore.QRect(0, 0, 272, 454))
        self.contenidoScroll.setObjectName("contenidoScroll")
        self.scrollArea.setWidget(self.contenidoScroll)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.agregar_empleado = QtWidgets.QPushButton(self.listado)
        self.agregar_empleado.setStyleSheet("\n"
"#agregar_empleado {\n"
"    background-color: #e73a4b;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#agregar_empleado:hover {\n"
"    background-color: #EC5B69;\n"
"}")
        self.agregar_empleado.setObjectName("agregar_empleado")
        self.verticalLayout_2.addWidget(self.agregar_empleado)
        self.horizontalLayout.addWidget(self.listado)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.datos = QtWidgets.QWidget(self.background)
        self.datos.setStyleSheet("#widget{\n"
"    margin-left: 20px;\n"
"}")
        self.datos.setObjectName("datos")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.datos)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.datos_widget = QtWidgets.QWidget(self.datos)
        self.datos_widget.setStyleSheet("#datos_widget{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"#datos_widget QPushButton{\n"
"    background-color: #e73a4b;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#datos_widget QPushButton:Hover{\n"
"    background-color: #EC5B69;\n"
"}")
        self.datos_widget.setObjectName("datos_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.datos_widget)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.datos_widget)
        self.groupBox.setStyleSheet("#groupBox QLineEdit {\n"
"    background-color: #013a70;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    border: 1px solid red ;\n"
"    border-radius: 6px\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nombre_label = QtWidgets.QLabel(self.groupBox)
        self.nombre_label.setObjectName("nombre_label")
        self.verticalLayout_5.addWidget(self.nombre_label)
        self.nombre_entry = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nombre_entry.setFont(font)
        self.nombre_entry.setObjectName("nombre_entry")
        self.verticalLayout_5.addWidget(self.nombre_entry)
        self.apellido_p_label = QtWidgets.QLabel(self.groupBox)
        self.apellido_p_label.setObjectName("apellido_p_label")
        self.verticalLayout_5.addWidget(self.apellido_p_label)
        self.apellido_p_entry = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.apellido_p_entry.setFont(font)
        self.apellido_p_entry.setObjectName("apellido_p_entry")
        self.verticalLayout_5.addWidget(self.apellido_p_entry)
        self.apellido_m_label = QtWidgets.QLabel(self.groupBox)
        self.apellido_m_label.setObjectName("apellido_m_label")
        self.verticalLayout_5.addWidget(self.apellido_m_label)
        self.apellido_m_entry = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.apellido_m_entry.setFont(font)
        self.apellido_m_entry.setObjectName("apellido_m_entry")
        self.verticalLayout_5.addWidget(self.apellido_m_entry)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.datos_widget)
        self.frame_2.setStyleSheet("#frame_2 QLineEdit {\n"
"    background-color: #013a70;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    border-bottom: 1px solid red;\n"
"    border-top: 1px solid red;\n"
"    border-right: 1px solid red;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"#frame_2 QLabel{\n"
"    background-color: #013a70;\n"
"    padding: 4px;\n"
"    border-bottom-left-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"    border-bottom: 1px solid red;\n"
"    border-top: 1px solid red;\n"
"    border-left: 1px solid red;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(34, 34))
        self.label.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(34, 34))
        self.label_2.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.rolLabel = QtWidgets.QLabel(self.datos_widget)
        self.rolLabel.setObjectName("rolLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rolLabel)
        self.rolComboBox = QtWidgets.QComboBox(self.datos_widget)
        self.rolComboBox.setObjectName("rolComboBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rolComboBox)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.datos_widget)
        self.groupBox_2.setStyleSheet("#groupBox_2 QLineEdit {\n"
"    background-color: #013a70;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    border-radius: 6px;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.datos_widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.datos_widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.datos_widget)
        self.horizontalLayout.addWidget(self.datos)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout.addWidget(self.background)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.iconoBuscar.setText(_translate("Form", "aaaaa"))
        self.barraBusqueda.setPlaceholderText(_translate("Form", "Buscar Empleado"))
        self.agregar_empleado.setText(_translate("Form", "Agregar empleado"))
        self.groupBox.setTitle(_translate("Form", "Nombre"))
        self.nombre_label.setText(_translate("Form", "Nombre(s):"))
        self.apellido_p_label.setText(_translate("Form", "Apellido paterno:"))
        self.apellido_m_label.setText(_translate("Form", "Apellido materno:"))
        self.label.setText(_translate("Form", "sp"))
        self.label_2.setText(_translate("Form", "so"))
        self.rolLabel.setText(_translate("Form", "Rol"))
        self.groupBox_2.setTitle(_translate("Form", "Datos de la cuenta"))
        self.label_4.setText(_translate("Form", "Contraseña"))
        self.checkBox.setText(_translate("Form", "Admin"))
        self.pushButton_3.setText(_translate("Form", "Editar"))
        self.pushButton_2.setText(_translate("Form", "Eliminar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
