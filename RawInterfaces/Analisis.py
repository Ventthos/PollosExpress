# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RawInterfaces\Analisis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetRealAnalisis = QtWidgets.QWidget(self.centralwidget)
        self.widgetRealAnalisis.setStyleSheet("#widgetRealAnalisis{\n"
"    background-color: #091949;\n"
"}")
        self.widgetRealAnalisis.setObjectName("widgetRealAnalisis")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetRealAnalisis)
        self.verticalLayout_3.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetAnalisis = QtWidgets.QWidget(self.widgetRealAnalisis)
        self.widgetAnalisis.setStyleSheet("#widgetAnalisis{\n"
"    background-color: rgba(255,255,255,0.8);\n"
"    border-radius: 20px;\n"
"}")
        self.widgetAnalisis.setObjectName("widgetAnalisis")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetAnalisis)
        self.verticalLayout_2.setContentsMargins(10, 6, 10, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widgetAnalisis)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.contenedorSemanas = QtWidgets.QWidget(self.widget_2)
        self.contenedorSemanas.setStyleSheet("#contenedorSemanas{\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#contenedorSemanas QPushButton{\n"
"    background-color: #d9d9d9;\n"
"    border: none;\n"
"    padding: 8px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#contenedorSemanas QPushButton:Hover{\n"
"    background-color: #c3c3c3;\n"
"}")
        self.contenedorSemanas.setObjectName("contenedorSemanas")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contenedorSemanas)
        self.horizontalLayout.setContentsMargins(12, 5, 40, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonRewind = QtWidgets.QPushButton(self.contenedorSemanas)
        self.buttonRewind.setObjectName("buttonRewind")
        self.horizontalLayout.addWidget(self.buttonRewind)
        self.labelTiempo = QtWidgets.QLabel(self.contenedorSemanas)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTiempo.setFont(font)
        self.labelTiempo.setObjectName("labelTiempo")
        self.horizontalLayout.addWidget(self.labelTiempo)
        self.buttonFord = QtWidgets.QPushButton(self.contenedorSemanas)
        self.buttonFord.setObjectName("buttonFord")
        self.horizontalLayout.addWidget(self.buttonFord)
        self.buttonBuscar = QtWidgets.QPushButton(self.contenedorSemanas)
        self.buttonBuscar.setObjectName("buttonBuscar")
        self.horizontalLayout.addWidget(self.buttonBuscar)
        self.verticalLayout_4.addWidget(self.contenedorSemanas, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widgetCentral = QtWidgets.QWidget(self.widgetAnalisis)
        self.widgetCentral.setObjectName("widgetCentral")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetCentral)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetGrafica = QtWidgets.QWidget(self.widgetCentral)
        self.widgetGrafica.setObjectName("widgetGrafica")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widgetGrafica)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2.addWidget(self.widgetGrafica)
        self.Estadisticos = QtWidgets.QWidget(self.widgetCentral)
        self.Estadisticos.setObjectName("Estadisticos")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Estadisticos)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidgetDatos = QtWidgets.QStackedWidget(self.Estadisticos)
        self.stackedWidgetDatos.setStyleSheet("")
        self.stackedWidgetDatos.setObjectName("stackedWidgetDatos")
        self.pageValoresTiempo = QtWidgets.QWidget()
        self.pageValoresTiempo.setStyleSheet("#pageValoresTiempo{\n"
"    background-color: #ced1db;\n"
"}")
        self.pageValoresTiempo.setObjectName("pageValoresTiempo")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pageValoresTiempo)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.labelLineEdit_1 = QtWidgets.QWidget(self.pageValoresTiempo)
        self.labelLineEdit_1.setObjectName("labelLineEdit_1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.labelLineEdit_1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelVentasTot = QtWidgets.QLabel(self.labelLineEdit_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelVentasTot.setFont(font)
        self.labelVentasTot.setObjectName("labelVentasTot")
        self.verticalLayout_8.addWidget(self.labelVentasTot)
        self.lineEditVentasTot = QtWidgets.QLineEdit(self.labelLineEdit_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditVentasTot.setFont(font)
        self.lineEditVentasTot.setObjectName("lineEditVentasTot")
        self.verticalLayout_8.addWidget(self.lineEditVentasTot)
        self.verticalLayout_11.addWidget(self.labelLineEdit_1, 0, QtCore.Qt.AlignTop)
        self.labelLineEdit_2 = QtWidgets.QWidget(self.pageValoresTiempo)
        self.labelLineEdit_2.setObjectName("labelLineEdit_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.labelLineEdit_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelGastosTot = QtWidgets.QLabel(self.labelLineEdit_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelGastosTot.setFont(font)
        self.labelGastosTot.setObjectName("labelGastosTot")
        self.verticalLayout_7.addWidget(self.labelGastosTot)
        self.lineEditGastosTot = QtWidgets.QLineEdit(self.labelLineEdit_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditGastosTot.setFont(font)
        self.lineEditGastosTot.setObjectName("lineEditGastosTot")
        self.verticalLayout_7.addWidget(self.lineEditGastosTot)
        self.verticalLayout_11.addWidget(self.labelLineEdit_2, 0, QtCore.Qt.AlignTop)
        self.labelLineEdit_5 = QtWidgets.QWidget(self.pageValoresTiempo)
        self.labelLineEdit_5.setObjectName("labelLineEdit_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.labelLineEdit_5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.labelRendimientoTotal = QtWidgets.QLabel(self.labelLineEdit_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelRendimientoTotal.setFont(font)
        self.labelRendimientoTotal.setObjectName("labelRendimientoTotal")
        self.verticalLayout_12.addWidget(self.labelRendimientoTotal)
        self.GananciasTotales = QtWidgets.QLineEdit(self.labelLineEdit_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.GananciasTotales.setFont(font)
        self.GananciasTotales.setObjectName("GananciasTotales")
        self.verticalLayout_12.addWidget(self.GananciasTotales)
        self.verticalLayout_11.addWidget(self.labelLineEdit_5, 0, QtCore.Qt.AlignTop)
        self.labelLineEdit_3 = QtWidgets.QWidget(self.pageValoresTiempo)
        self.labelLineEdit_3.setObjectName("labelLineEdit_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.labelLineEdit_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.text = QtWidgets.QLabel(self.labelLineEdit_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.verticalLayout_9.addWidget(self.text)
        self.lineEditPromedioGananciaDia = QtWidgets.QLineEdit(self.labelLineEdit_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditPromedioGananciaDia.setFont(font)
        self.lineEditPromedioGananciaDia.setObjectName("lineEditPromedioGananciaDia")
        self.verticalLayout_9.addWidget(self.lineEditPromedioGananciaDia)
        self.verticalLayout_11.addWidget(self.labelLineEdit_3, 0, QtCore.Qt.AlignTop)
        self.labelLineEdit_4 = QtWidgets.QWidget(self.pageValoresTiempo)
        self.labelLineEdit_4.setObjectName("labelLineEdit_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.labelLineEdit_4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.labelPromedioGastoDia = QtWidgets.QLabel(self.labelLineEdit_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelPromedioGastoDia.setFont(font)
        self.labelPromedioGastoDia.setObjectName("labelPromedioGastoDia")
        self.verticalLayout_10.addWidget(self.labelPromedioGastoDia)
        self.PromGastos = QtWidgets.QLineEdit(self.labelLineEdit_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PromGastos.setFont(font)
        self.PromGastos.setObjectName("PromGastos")
        self.verticalLayout_10.addWidget(self.PromGastos)
        self.verticalLayout_11.addWidget(self.labelLineEdit_4, 0, QtCore.Qt.AlignTop)
        self.contenedorPagina = QtWidgets.QWidget(self.pageValoresTiempo)
        self.contenedorPagina.setStyleSheet("#contenedorPagina QPushButton{\n"
"    background-color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#contenedorPagina QPushButton:Hover{\n"
"    background-color: #e6e6e6;\n"
"}")
        self.contenedorPagina.setObjectName("contenedorPagina")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.contenedorPagina)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.contenedorPagina)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.contenedorPagina)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.contenedorPagina)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addWidget(self.contenedorPagina)
        self.stackedWidgetDatos.addWidget(self.pageValoresTiempo)
        self.pageValoresPermanentes = QtWidgets.QWidget()
        self.pageValoresPermanentes.setObjectName("pageValoresPermanentes")
        self.stackedWidgetDatos.addWidget(self.pageValoresPermanentes)
        self.verticalLayout_6.addWidget(self.stackedWidgetDatos)
        self.horizontalLayout_2.addWidget(self.Estadisticos)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.widgetCentral)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_3.addWidget(self.widgetAnalisis)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout.addWidget(self.widgetRealAnalisis)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidgetDatos.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonRewind.setText(_translate("MainWindow", "AA"))
        self.labelTiempo.setText(_translate("MainWindow", "Semana 2/08/2023 - 8/08/2023"))
        self.buttonFord.setText(_translate("MainWindow", "AA"))
        self.buttonBuscar.setText(_translate("MainWindow", "AA"))
        self.labelVentasTot.setText(_translate("MainWindow", "Ventas Totales"))
        self.labelGastosTot.setText(_translate("MainWindow", "Gastos Totales"))
        self.labelRendimientoTotal.setText(_translate("MainWindow", "Ganancias totales"))
        self.text.setText(_translate("MainWindow", "Promedio de ventas por día"))
        self.labelPromedioGastoDia.setText(_translate("MainWindow", "Promedio de gastos por día"))
        self.pushButton_4.setText(_translate("MainWindow", "<"))
        self.label_7.setText(_translate("MainWindow", "1/2"))
        self.pushButton_5.setText(_translate("MainWindow", ">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
