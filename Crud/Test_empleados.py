from Crud.CRUD_Usuario import CrudEmpleado
from Crud.CRUD_producto import CrudProducto
import mysql.connector

def test_inicio_sesion():
    conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3306",
        database="pollosexpress"
    )
    Crud = CrudEmpleado(conection)
    assert Crud.iniciarSesion("1", "a") == (True,True, 1)

def test_Read_Product():
    conection = mysql.connector.connect(
        user="root",
        host="localhost",
        port="3306",
        database="pollosexpress"
    )
    Crud = CrudProducto(conection)
    assert Crud.ReadSimplified(1).nombre == "Spaguetti"
