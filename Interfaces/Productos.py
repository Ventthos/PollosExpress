from PyQt5.QtWidgets import QWidget
from RawInterfaces.Productos import Ui_Form
import mysql.connector
from Crud.CRUD_producto import CrudProducto, Producto

class ProductosInterface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.__productManager = CrudProducto(conection=self.__conection)