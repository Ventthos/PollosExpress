# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RawInterfaces\Promociones.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color: #8fb8de;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3 {\n"
"color: white;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.BuscadorPromociones = QtWidgets.QLineEdit(self.centralwidget)
        self.BuscadorPromociones.setMaximumSize(QtCore.QSize(500, 16777215))
        self.BuscadorPromociones.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.BuscadorPromociones.setObjectName("BuscadorPromociones")
        self.gridLayout.addWidget(self.BuscadorPromociones, 2, 0, 1, 1)
        self.BotonAgregarPromocion = QtWidgets.QPushButton(self.centralwidget)
        self.BotonAgregarPromocion.setMaximumSize(QtCore.QSize(500, 16777215))
        self.BotonAgregarPromocion.setObjectName("BotonAgregarPromocion")
        self.gridLayout.addWidget(self.BotonAgregarPromocion, 4, 0, 1, 1)
        self.scrollAreaPromociones = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaPromociones.sizePolicy().hasHeightForWidth())
        self.scrollAreaPromociones.setSizePolicy(sizePolicy)
        self.scrollAreaPromociones.setMinimumSize(QtCore.QSize(240, 0))
        self.scrollAreaPromociones.setMaximumSize(QtCore.QSize(500, 16777215))
        self.scrollAreaPromociones.setWidgetResizable(True)
        self.scrollAreaPromociones.setObjectName("scrollAreaPromociones")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 238, 590))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaPromociones.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollAreaPromociones, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(400, 200, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.GridPromociones = QtWidgets.QGridLayout()
        self.GridPromociones.setContentsMargins(20, 20, 50, 10)
        self.GridPromociones.setObjectName("GridPromociones")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GridDatos = QtWidgets.QGridLayout()
        self.GridDatos.setContentsMargins(0, 100, -1, -1)
        self.GridDatos.setObjectName("GridDatos")
        self.FechaFinalBox = QtWidgets.QDateEdit(self.centralwidget)
        self.FechaFinalBox.setObjectName("FechaFinalBox")
        self.GridDatos.addWidget(self.FechaFinalBox, 3, 1, 1, 1)
        self.FechaInicioBox = QtWidgets.QDateEdit(self.centralwidget)
        self.FechaInicioBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.FechaInicioBox.setObjectName("FechaInicioBox")
        self.GridDatos.addWidget(self.FechaInicioBox, 3, 0, 1, 1)
        self.TipoPromocionBox = QtWidgets.QComboBox(self.centralwidget)
        self.TipoPromocionBox.setObjectName("TipoPromocionBox")
        self.GridDatos.addWidget(self.TipoPromocionBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"color: white;\n"
"}")
        self.label.setObjectName("label")
        self.GridDatos.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2 {\n"
"color: white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.GridDatos.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
"color: white;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.GridDatos.addWidget(self.label_4, 2, 1, 1, 1)
        self.PromocionBox = QtWidgets.QComboBox(self.centralwidget)
        self.PromocionBox.setObjectName("PromocionBox")
        self.GridDatos.addWidget(self.PromocionBox, 1, 0, 1, 1)
        self.labelFechaInicio = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelFechaInicio.setFont(font)
        self.labelFechaInicio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelFechaInicio.setStyleSheet("#labelFechaInicio {\n"
"color: white;\n"
"}")
        self.labelFechaInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFechaInicio.setObjectName("labelFechaInicio")
        self.GridDatos.addWidget(self.labelFechaInicio, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.GridDatos, 0, 0, 1, 1)
        self.GridPromociones.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5{\n"
"color: white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.GridPromociones.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EditarPromocionButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditarPromocionButton.setObjectName("EditarPromocionButton")
        self.gridLayout_2.addWidget(self.EditarPromocionButton, 0, 0, 1, 1)
        self.BorrarPromocionBoton = QtWidgets.QPushButton(self.centralwidget)
        self.BorrarPromocionBoton.setObjectName("BorrarPromocionBoton")
        self.gridLayout_2.addWidget(self.BorrarPromocionBoton, 0, 1, 1, 1)
        self.GridPromociones.addLayout(self.gridLayout_2, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.GridPromociones.addItem(spacerItem1, 4, 0, 1, 1)
        self.textodescripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.textodescripcion.setObjectName("textodescripcion")
        self.GridPromociones.addWidget(self.textodescripcion, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.GridPromociones)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.BuscadorPromociones)
        self.label.setBuddy(self.PromocionBox)
        self.label_2.setBuddy(self.TipoPromocionBox)
        self.label_4.setBuddy(self.FechaFinalBox)
        self.labelFechaInicio.setBuddy(self.FechaInicioBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Promociones"))
        self.label_3.setText(_translate("MainWindow", "Promociones"))
        self.BuscadorPromociones.setPlaceholderText(_translate("MainWindow", "Buscar"))
        self.BotonAgregarPromocion.setText(_translate("MainWindow", "Agregar Promocion"))
        self.FechaFinalBox.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.FechaInicioBox.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.label.setText(_translate("MainWindow", "Producto relacionado:"))
        self.label_2.setText(_translate("MainWindow", "Tipo de promocion"))
        self.label_4.setText(_translate("MainWindow", "Fecha final"))
        self.labelFechaInicio.setText(_translate("MainWindow", "Fecha inicio"))
        self.label_5.setText(_translate("MainWindow", "Descripcion"))
        self.EditarPromocionButton.setText(_translate("MainWindow", "Editar Promocion"))
        self.BorrarPromocionBoton.setText(_translate("MainWindow", "Borrar Promocion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
