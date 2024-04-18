from RawInterfaces.Login import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui

from Crud.CRUD_Usuario import CrudEmpleado
import mysql.connector
from tkinter import messagebox
from MainMenu import MainMenu


class Login(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.label_2.setPixmap(QtGui.QPixmap("../img/logo.png"))
        self.connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.pushButton.clicked.connect(self.iniciarSesion)

    def iniciarSesion(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if user != "" and password != "":
            try:
                userManager = CrudEmpleado(self.connection)
                result, is_administrator, idU = userManager.iniciarSesion(user, password)

                if result:
                    messagebox.showinfo("Mensaje de inicio de sesión", f"Sesión iniciada con éxito, bienvenido {user}")
                    if is_administrator == 1:
                        menu = MainMenu(True, idU, self.getUserName(userManager, idU))
                        messagebox.showinfo("Mensaje de inicio de sesión", "Entrando en modo administrador")

                    else:
                        menu = MainMenu(False, idU, self.getUserName(userManager, idU))
                        messagebox.showinfo("Mensaje de inicio de sesión", "Entrando en modo cajero")
                    menu.show()
                    self.hide()
                    return
                else:
                    messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrecto(s)")
                    return

            except Exception as e:
                messagebox.showerror("Error de inicio de sesión", "ERROR: " + str(e))
                return

        messagebox.showerror("Error", "Debe rellenar todos los campos")

    def getUserName(self, userManager, id):
        usuario = userManager.Read(id)
        return usuario.getNombre() + " " + usuario.getApellido_paterno()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Login()
    ui.show()
    sys.exit(app.exec_())
