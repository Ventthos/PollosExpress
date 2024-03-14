from RawInterfaces.Login import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui

from Crud.CRUD_Usuario import CrudEmpleado
import mysql.connector
from tkinter import messagebox


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
                        print("Entrando en modo administrador...")
                        messagebox.showinfo("Mensaje de inicio de sesión", "Entrando en modo administrador")

                    return
                else:
                    messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrecto(s)")
                    return

            except Exception as e:
                messagebox.showerror("Error de inicio de sesión", "ERROR: " + str(e))
                return

        messagebox.showerror("Error", "Debe rellenar todos los campos")


kk
