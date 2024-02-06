from PyQt5 import QtWidgets, QtGui
from RawInterfaces.Empleados import Ui_Form
import mysql.connector
from Crud.CRUD_Usuario import CrudEmpleado, Empleado
from Crud.CRUD_Rol import *


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

        self.datos_widget.hide()

        self.__roles = []
        self.__empleadoActivo = None

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
        self.get_list_elements().clear()
        empleados = self.__userManager.Read()
        for empleado in empleados:
            if empleado.activo == 'V':
                newElement = NoImageFrame(self.get_list_elements(),
                                          f"{empleado.getNombre()} {empleado.getApellido_paterno()} {empleado.getApellido_materno()}",
                                          empleado)
                newElement.addEvent("<Button-1>", self.__showEmpleado)
                self.get_list_elements().add(newElement)
        empleados.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Empleados()
    ui.show()
    sys.exit(app.exec_())
