from PyQt5 import QtWidgets, QtGui, QtCore
from RawInterfaces.Empleados import Ui_Form
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado, Empleado
from Crud.CRUD_Rol import *
from WidgetApoyo.NoImageFrame import NoImageFrame

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

        self.iconoBuscar.setPixmap(QtGui.QPixmap("../img/lupa.png"))
        self.label.setPixmap(QtGui.QPixmap("../img/Icons/Telefono.png"))
        self.label_2.setPixmap(QtGui.QPixmap("../img/Icons/Sueldo.png"))
        self.verticalLayout_6.setAlignment(QtCore.Qt.AlignTop)

        self.datos_widget.hide()

        self.__roles = []
        self.__empleadoActivo = None

        self.__updateEmpleados()

    def __createEmpleadoObject(self) -> Empleado:
        if self.__inputContraseña == "":
            empleado = Empleado(
                str(self.__inputName.get()),
                str(self.__inputLastname1.get()),
                str(self.__inputLastname2.get()),
                str(self.__inputCel.get()),
                float(self.__inputSueldo.get()),
                int(self.__findRol(self.__inputRol.get())),
                bool(self.__isAdmin.get()),
                'V'
            )
            print("Empleado sin contraseña creado")

        else:
            empleado = Empleado(
                str(self.__inputName.get()),
                str(self.__inputLastname1.get()),
                str(self.__inputLastname2.get()),
                str(self.__inputCel.get()),
                float(self.__inputSueldo.get()),
                self.__findRol(self.__inputRol.get()),
                bool(self.__isAdmin.get()),
                'V',
                str(self.__inputContraseña.get())

            )
            print("Empleado con contraseña creado")
        return empleado

    def __updateRoles(self):
        self.__roles = self.__rolManager.Read()
        rolesNombre = []
        for rol in self.__roles:
            rolesNombre.append(rol.getNombre())
        return rolesNombre

    def __findRol(self, nombre: str):
        for rol in self.__roles:
            if rol.getNombre() == nombre:
                return rol._getId()

    def __updateEmpleados(self):
        empleados = self.__userManager.Read()
        for empleado in empleados:
            if empleado.activo == 'V':
                newElement = NoImageFrame(f"{empleado.getNombre()} {empleado.getApellido_paterno()} "
                                          f"{empleado.getApellido_materno()}", empleado)
                newElement.add_event(self.__show_empleado)
                self.verticalLayout_6.addWidget(newElement)

        empleados.clear()

    def __show_empleado(self, widget):
        empleado: Empleado = widget.data
        if(self.datos_widget.isHidden()):
            self.datos_widget.show()
        self.nombre_entry.setText(empleado.getNombre())
        self.apellido_p_entry.setText(empleado.getApellido_paterno())
        self.apellido_m_entry.setText(empleado.getApellido_materno())
        self.lineEdit.setText(empleado.getCelular())
        self.lineEdit_2.setText(str(empleado.getSueldo()))
        self.lineEdit_3.setText(empleado.getCelular())
        self.checkBox.setChecked(empleado.getAdministrador())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Empleados()
    ui.show()
    sys.exit(app.exec_())
