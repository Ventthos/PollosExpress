from Crud.AbstractCRUD import CRUD
from Drive.drive import DriveManager
import threading


if __name__ != "__main__":

    class Producto:
        def __init__(self, nombre: str, descripcion: str, precio: float, imagen: str = None, id: int = None, driveCode: str = None, activo = "V"):
            self.id = None
            if id is not None:
                self.id = id
            self.nombre = nombre
            self.descripcion = descripcion
            self.precio = precio
            if imagen is not None:
                self.imagen = imagen
            self._driveCode = None
            if driveCode is not None:
                self._driveCode = driveCode
            self.activo = activo


    class CrudProducto(CRUD):
        def __init__(self, conection):
            super().__init__(conection)
            self.__driveConnection = DriveManager()

        def Create(self, product: Producto):
            script = "INSERT INTO producto(nombre, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)"
            datos_producto = (product.nombre, product.descripcion, product.precio, product._driveCode)
            self._cursor.execute(script, datos_producto) #seria fetch si pidiera datos
            self._conection.commit() # commit siempre que se modifique la tabla

        def Update(self, id, product: Producto):
            script = ("UPDATE producto "
                      "SET nombre = %s, descripcion = %s, precio = %s, imagen = %s "
                      "WHERE id_producto = %s")
            datos_producto = (product.nombre, product.descripcion, product.precio, product._driveCode, id)

            producto = self.Read(id)
            self.__driveConnection.deleteImage(producto._driveCode)
            self._cursor.execute(script, datos_producto)
            self._conection.commit()

        def Delete(self, id):
            if isinstance(id, int):
                producto = self.Read(id)
                #self.__driveConnection.deleteImage(producto._driveCode)
                script = f"UPDATE producto SET activo = 'F' WHERE id_producto = {id}"
                self._cursor.execute(script)
                self._conection.commit()
            else:
                raise ValueError("Id must be an integer")

        def Read(self, id=None):
            self._conection.commit()
            if id is None:
                script = "SELECT * from producto where activo = 'V' "
                self._cursor.execute(script)
                result = self._cursor.fetchall()
                productos = []
                for resultado in result:
                    print(resultado)
                    route = f"../userImages/product_{resultado[1]}.png"
                    self.__driveConnection.downloadImage(resultado[4], route)
                    producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0], driveCode=resultado[4], activo=resultado[5])
                    productos.append(producto)
                return productos

            elif isinstance(id, int):
                script = f"SELECT * from producto WHERE id_producto = {id} AND activo = 'V'"
                self._cursor.execute(script)
                resultado = self._cursor.fetchone()
                route = f"../userImages/product_{resultado[1]}.png"
                self.__driveConnection.downloadImage(resultado[4], route)
                producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0], driveCode=resultado[4], activo=resultado[5])
                return producto

            elif not isinstance(id, int):
                raise ValueError("Id must be an integer")

        def ReadSimplified(self, id= None) -> list[Producto]:
            self._conection.commit()
            if id is None:
                script = "SELECT * from producto WHERE activo = 'V'"
                self._cursor.execute(script)
                result = self._cursor.fetchall()
                productos = []
                for resultado in result:
                    route = f"../userImages/product_{resultado[1]}.png"
                    producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0],
                                        driveCode=resultado[4], activo=resultado[5])
                    productos.append(producto)
                return productos

            elif isinstance(id, int):
                script = f"SELECT * from producto WHERE id_producto = {id} AND activo = 'V'"
                self._cursor.execute(script)
                resultado = self._cursor.fetchone()
                route = f"../userImages/product_{resultado[1]}.png"
                producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0],
                                    driveCode=resultado[4])
                return producto

        def downloadImages(self, *elements):
            for element in elements:
                self.__driveConnection.downloadImage(element.driveCode, element.imagen)

        def UploadImage(self, url):
            id = self.__driveConnection.uploadImage(url)
            return id

        def countProducts(self):
            script = "SELECT COUNT(*) from producto WHERE activo = 'V'"
            self._cursor.execute(script)
            result = self._cursor.fetchone()
            return result

        def getIds(self):
            script = "SELECT id_producto from producto WHERE activo = 'V'"
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            return result

        def findSimilar(self, substring: str):
            script = f"SELECT * from producto WHERE nombre LIKE '{substring}%' AND activo = 'V'"
            self._conection.commit()
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            productos = []
            for resultado in result:
                route = f"../userImages/product_{resultado[1]}.png"
                self.__driveConnection.downloadImage(resultado[4], route)
                producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0],
                                    driveCode=resultado[4], activo=resultado[5])
                productos.append(producto)
            return productos
