from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QFont
from RawInterfaces.Empleados import Ui_Form
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado, Empleado
from Crud.CRUD_Rol import *
from WidgetApoyo.NoImageFrame import NoImageFrame
from WidgetApoyo.LoadingScreen import LoadingScreen
from tkinter import messagebox

class Empleados(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )

        self.__userManager = CrudEmpleado(self.__conection)
        self.__rolManager = CrudRol(self.__conection)
        self.setupUi(self)

        self.proporcionMargenes = 20/1010

        self.iconoBuscar.setPixmap(QtGui.QPixmap("../img/lupa.png"))
        self.label.setPixmap(QtGui.QPixmap("../img/Icons/Telefono.png"))
        self.label_2.setPixmap(QtGui.QPixmap("../img/Icons/Sueldo.png"))
        self.verticalLayout_6.setAlignment(QtCore.Qt.AlignTop)

        self.datos_widget.hide()

        self.__roles = []
        self.__empleadoActivo = None
        self.empleados = []

        # Coso para poder agregar empleados
        self.agregarBoton = QtWidgets.QPushButton()
        self.agregarBoton.setText("Agregar empleado")
        self.agregarBoton.clicked.connect(self.__agregarEmpleado)
        self.agregar_empleado_activo = False
        self.horizontalLayout_3.addWidget(self.agregarBoton)
        self.agregarBoton.hide()

        # Conectar para poder eliminar y update
        self.pushButton_3.clicked.connect(self.__editar_empleado)
        self.pushButton_2.clicked.connect(self.__eliminar_empleado)

        self.agregar_empleado.clicked.connect(self.__configure_aregar_empleado)

        # Cargar todos los elementos
        self.__updateEmpleados()

        # Habilitar la funcion de elementos
        self.barraBusqueda.textChanged.connect(self.buscarEmpleado)

        # Habilitar actualización de datos manuales
        self.BotonRefrescar.clicked.connect(self.actualizarConWarnig)

        # Redimensionar margenes?



    def __createEmpleadoObject(self) -> Empleado:
        if self.lineEdit_3.text() == "":
            empleado = Empleado(
                str(self.nombre_entry.text()),
                str(self.apellido_p_entry.text()),
                str(self.apellido_m_entry.text()),
                str(self.lineEdit.text()),
                float(self.lineEdit_2.text()),
                int(self.__findRol(self.rolComboBox.currentText(), "database")),
                bool(self.checkBox.isChecked()),
                'V',
                contraseña= ""
            )
            print("Empleado sin contraseña creado")

        else:
            empleado = Empleado(
                str(self.nombre_entry.text()),
                str(self.apellido_p_entry.text()),
                str(self.apellido_m_entry.text()),
                str(self.lineEdit.text()),
                float(self.lineEdit_2.text()),
                int(self.__findRol(self.rolComboBox.currentText(), "database")),
                bool(self.checkBox.isChecked()),
                'V',
                str(self.lineEdit_3.text())

            )
            print("Empleado con contraseña creado")
        return empleado

    def __updateRoles(self):
        self.__roles = self.__rolManager.Read()
        rolesNombre = []
        for rol in self.__roles:
            rolesNombre.append(rol.getNombre())
        return rolesNombre

    def __findRol(self, nombre: str, mode: str):
        print(nombre)
        if mode == "local":
            for rolIndex in range(len(self.__roles)):
                if self.__roles[rolIndex].getNombre() == nombre:
                    return rolIndex
        else:
            for rol in self.__roles:
                print(rol.getNombre())
                if rol.getNombre() == nombre:
                    print("ya encontrre")
                    print(rol._getId())
                    return rol._getId()


    def __updateEmpleados(self):
        for widget in range(self.verticalLayout_6.count()-1,-1, -1):
            print("borrado")
            self.verticalLayout_6.itemAt(widget).widget().hide()
            self.verticalLayout_6.removeWidget(self.verticalLayout_6.itemAt(widget).widget())
        self.empleados.clear()

        empleados = self.__userManager.Read()
        for empleado in empleados:
            self.empleados.append(empleado)
            if empleado.activo == 'V':
                newElement = NoImageFrame(f"{empleado.getNombre()} {empleado.getApellido_paterno()} "
                                          f"{empleado.getApellido_materno()}", empleado)
                newElement.add_event(self.__show_empleado)
                self.verticalLayout_6.addWidget(newElement)

        empleados.clear()

        roles = self.__updateRoles()
        self.rolComboBox.clear()
        self.rolComboBox.addItems(roles)

    def __show_empleado(self, widget):
        empleado: Empleado = widget.data
        self.__empleadoActivo = empleado
        if self.datos_widget.isHidden():
            self.datos_widget.show()
        if self.agregar_empleado_activo:
            self.agregar_empleado_activo = False
            self.agregarBoton.hide()
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.agregar_empleado.setEnabled(True)

        self.nombre_entry.setText(empleado.getNombre())
        self.apellido_p_entry.setText(empleado.getApellido_paterno())
        self.apellido_m_entry.setText(empleado.getApellido_materno())
        self.lineEdit.setText(empleado.getCelular())
        self.lineEdit_2.setText(str(empleado.getSueldo()))
        if empleado.getAdministrador() is None:
            self.lineEdit_3.setText("")
        else:
            self.lineEdit_3.setText(empleado.getContraseña())
        self.checkBox.setChecked(empleado.getAdministrador())
        self.rolComboBox.setCurrentIndex(self.__findRol(empleado.getIdRol(), "local"))

    def __configure_aregar_empleado(self):
        if self.datos_widget.isHidden():
            self.datos_widget.show()

        self.pushButton_3.hide()
        self.pushButton_2.hide()
        self.agregarBoton.show()
        self.agregar_empleado_activo = True
        self.agregar_empleado.setEnabled(False)

        self.nombre_entry.setText("")
        self.apellido_p_entry.setText("")
        self.apellido_m_entry.setText("")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.checkBox.setChecked(False)
        self.rolComboBox.setCurrentIndex(-1)

    def __agregarEmpleado(self):
        pantallaCarga = LoadingScreen()
        pantallaCarga.show()
        QtWidgets.QApplication.processEvents()
        empleado = self.__createEmpleadoObject()
        self.__userManager.Create(empleado)
        self.__updateEmpleados()
        self.__configure_aregar_empleado()
        pantallaCarga = None
        messagebox.showinfo(title="Operación completada", message="El empleado ha sido agregado con éxito")

    def __editar_empleado(self):
        self.pushButton_3.setEnabled(False)
        pantallaCarga = LoadingScreen()
        pantallaCarga.show()
        QtWidgets.QApplication.processEvents()
        pantallaCarga.gif.start()
        self.__userManager.Update(self.__empleadoActivo.getId(), self.__createEmpleadoObject())
        self.__updateEmpleados()
        pantallaCarga = None
        self.pushButton_3.setEnabled(True)

        messagebox.showinfo(title="Operación completada", message="El empleado ha sido editado con éxito")

    def __eliminar_empleado(self):
        self.pushButton_2.setEnabled(False)
        pantallaCarga = LoadingScreen()
        pantallaCarga.show()
        QtWidgets.QApplication.processEvents()
        self.__userManager.Delete(self.__empleadoActivo.getId())
        self.__updateEmpleados()
        if self.verticalLayout_6.count() > 0:
            self.__show_empleado(self.verticalLayout_6.itemAt(0).widget())
        else:
            self.__configure_aregar_empleado()
        pantallaCarga = None
        messagebox.showinfo(title="Operación completada", message="El empleado ha sido eliminado con éxito")
        self.pushButton_2.setEnabled(True)

    def buscarEmpleado(self):
        for widget in range(self.verticalLayout_6.count()-1,-1, -1):
            self.verticalLayout_6.itemAt(widget).widget().hide()
            self.verticalLayout_6.removeWidget(self.verticalLayout_6.itemAt(widget).widget())

        if self.barraBusqueda.text() != "":
            for empleado in self.empleados:
                if self.barraBusqueda.text().lower() in empleado.getNombre().lower():
                    newElement = NoImageFrame(f"{empleado.getNombre()} {empleado.getApellido_paterno()} "
                                              f"{empleado.getApellido_materno()}", empleado)
                    newElement.add_event(self.__show_empleado)
                    self.verticalLayout_6.addWidget(newElement)
        else:
            for empleado in self.empleados:
                newElement = NoImageFrame(f"{empleado.getNombre()} {empleado.getApellido_paterno()} "
                                          f"{empleado.getApellido_materno()}", empleado)
                newElement.add_event(self.__show_empleado)
                self.verticalLayout_6.addWidget(newElement)

    def actualizarConWarnig(self):
        self.BotonRefrescar.setEnabled(False)
        self.__updateEmpleados()
        messagebox.showinfo("Actualizado", "Los datos del programa han sido actualizados")
        self.BotonRefrescar.setEnabled(True)

    def resizeEvent(self, event):
        margenes = int(self.width()*self.proporcionMargenes)
        self.background.setContentsMargins(margenes, margenes, margenes, margenes)
        margenes = int((11 / 1010) * self.width())
        self.listado.setContentsMargins(margenes, margenes, margenes,margenes)
        self.iconoBuscar.setMaximumSize(int((26/1010) * self.width()), int((40/1010) * self.width()))
        self.label.setMaximumSize(int((30/1010) * self.width()), int((50/1010)*self.width()))
        self.label_2.setMaximumSize(int((30 / 1010) * self.width()), int((50 / 1010) * self.width()))

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(int((9/1010)*self.width()))
        self.barraBusqueda.setFont(font)
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(int((8 / 1010) * self.width()))
        self.agregar_empleado.setFont(font)
        self.BotonRefrescar.setFont(font)
        self.groupBox.setFont(font)
        self.nombre_label.setFont(font)
        self.apellido_p_label.setFont(font)
        self.apellido_m_label.setFont(font)
        self.groupBox_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_2.setFont(font)
        self.rolLabel.setFont(font)

        font.setPointSize(int((9 / 1010) * self.width()))
        print(font.pointSize())
        self.nombre_entry.setFont(font)
        self.apellido_p_entry.setFont(font)
        self.apellido_m_entry.setFont(font)
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3.setFont(font)
        self.checkBox.setFont(font)
        self.label_4.setFont(font)
        self.rolComboBox.setFont(font)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Empleados()
    ui.show()
    sys.exit(app.exec_())
