
from Drive.drive import DriveManager
import threading


if __name__ != "__main__":

    class Producto:
        def __init__(self, nombre: str, descripcion: str, precio: float, esPaquete: bool, imagen: str = None, id: int = None,
                     driveCode: str = None, productosPaquete: list= None, activo = "V"):
            self.id = None
            if id is not None:
                self.id = id
            self.nombre = nombre
            self.descripcion = descripcion
            self.precio = precio
            if imagen is not None:
                self.imagen = imagen
            self.driveCode = None
            if driveCode is not None:
                self.driveCode = driveCode
            self.activo = activo
            self.esPaquete = esPaquete
            if esPaquete:
                self.productosPaquete = productosPaquete


    class Paquete(Producto):
        def __init__(self, nombre: str, descripcion: str, precio: float, imagen: str = None, id: int = None,
                     driveCode: str = None, activo = "V", productos: list = None):
            super().__init__(nombre, descripcion, precio,imagen, id, driveCode, activo)
            self.productos = productos

    class CrudProducto:
        def __init__(self, conection):
            self._conection = conection
            self._cursor = self._conection.cursor()
            self.__driveConnection = DriveManager()

        def Create(self, product: Producto):
            self._conection.reconnect()
            script = f"INSERT INTO producto(nombre, descripcion, precio, imagen, esPaquete) VALUES (%s, %s, %s, %s, %s)"
            datos_producto = (product.nombre, product.descripcion, product.precio, product.driveCode, product.esPaquete)
            self._cursor.execute(script, datos_producto) #seria fetch si pidiera datos
            self._conection.commit() # commit siempre que se modifique la tabla

        def Update(self, id, product: Producto):
            script = (f"UPDATE producto"
                      "SET nombre = %s, descripcion = %s, precio = %s, imagen = %s "
                      "WHERE id_producto = %s")
            datos_producto = (product.nombre, product.descripcion, product.precio, product.driveCode, id)

            producto = self.ReadSimplified(id)
            #self.__driveConnection.deleteImage(producto._driveCode)
            self._cursor.execute(script, datos_producto)
            self._conection.commit()

        def Delete(self, id):
            if isinstance(id, int):

                #self.__driveConnection.deleteImage(producto._driveCode)
                script = f"UPDATE producto SET activo = 'F' WHERE id_producto = {id}"
                self._cursor.execute(script)
                self._conection.commit()
            else:
                raise ValueError("Id must be an integer")

        def Read(self, id=None):
            self._conection.commit()
            if id is None:
                script = f"SELECT * from producto where activo = 'V' "
                self._cursor.execute(script)
                result = self._cursor.fetchall()
                productos = []
                for resultado in result:
                    print(resultado)
                    route = f"../userImages/product_{resultado[1]}.png"
                    #self.__driveConnection.downloadImage(resultado[4], route)
                    producto = Producto(resultado[1], resultado[2], resultado[3], resultado[6], route, resultado[0],
                                        driveCode=resultado[4], activo=resultado[5])
                    productos.append(producto)
                return productos

            elif isinstance(id, int):
                script = f"SELECT * from producto WHERE id_producto = {id} AND activo = 'V'"
                self._cursor.execute(script)
                resultado = self._cursor.fetchone()
                route = f"../userImages/product_{resultado[1]}.png"
                #self.__driveConnection.downloadImage(resultado[4], route)
                producto = Producto(resultado[1], resultado[2], resultado[3], resultado[6], route, resultado[0],
                                    driveCode=resultado[4], activo=resultado[5])
                return producto

            elif not isinstance(id, int):
                raise ValueError("Id must be an integer")

        # De preferencia no usen Read(), si no ReadSimplified
        def ReadSimplified(self, id=None) -> list[Producto] or Producto:
            self._conection.commit()
            if id is None:
                script = f"SELECT * from producto WHERE activo = 'V'"
                self._cursor.execute(script)
                result = self._cursor.fetchall()
                productos = []
                for resultado in result:
                    print(resultado[1])
                    route = f"../img/userImages/product_{resultado[1]}.png"
                    producto = Producto(resultado[1], resultado[2], resultado[3], resultado[6], route, resultado[0],
                                        driveCode=resultado[4], activo=resultado[5])

                    # Resultado 6 es si es que es paquete, si lo es, le agregamos sus productos
                    if resultado[6]:
                        print("Es paquete")
                        # Reconnect es para poder volver a lanzar otro comando SQL
                        self._conection.reconnect()
                        productosPaquete = self.readProductosPaquete(resultado[0])
                        print(productosPaquete)
                        producto.productosPaquete = productosPaquete

                    productos.append(producto)
                return productos

            elif isinstance(id, int):
                script = f"SELECT * from producto WHERE id_producto = {id} AND activo = 'V'"
                self._cursor.execute(script)
                resultado = self._cursor.fetchone()
                route = f"../userImages/product_{resultado[1]}.png"
                producto = Producto(resultado[1], resultado[2], resultado[3], resultado[6], route, resultado[0],
                                    driveCode=resultado[4])

                if resultado[6]:
                    print("Producto: ")
                    print(resultado[1])
                    # Reconnect es para poder volver a lanzar otro comando SQL
                    self._conection.reconnect()
                    productosPaquete = self.readProductosPaquete(resultado[0])
                    producto.productosPaquete = productosPaquete
                    print(productosPaquete)

                return producto

        def downloadImages(self, *elements):
            for element in elements:
                self.__driveConnection.downloadImage(element.driveCode, element.imagen)

        def UploadImage(self, url):
            id = self.__driveConnection.uploadImage(url)
            return id

        def countProducts(self):
            script = f"SELECT COUNT(*) from producto WHERE activo = 'V'"
            self._cursor.execute(script)
            result = self._cursor.fetchone()
            return result

        def getIds(self):
            script = f"SELECT id_producto from producto WHERE activo = 'V'"
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            return result

        def findSimilar(self, substring: str):
            script = f"SELECT * from producto WHERE nombre LIKE '%{substring}%' AND activo = 'V'"
            self._conection.commit()
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            productos = []
            for resultado in result:
                route = f"../userImages/product_{resultado[1]}.png"
                #self.__driveConnection.downloadImage(resultado[4], route)
                producto = Producto(resultado[1], resultado[2], resultado[3], route, resultado[0],
                                    driveCode=resultado[4], activo=resultado[5])
                productos.append(producto)
            return productos

        def agregarProductosPaquete(self,  id, productos: list[(int, int)]):
            for producto in productos:
                script = (f"INSERT INTO paquete_producto(id_paquete, id_producto, cantidad) "
                          f"VALUES({id}, {producto[0]}, {producto[1]});")
                self._cursor.execute(script)
                self._conection.commit()

        def getLastId(self):
            script = "SELECT id_producto FROM producto ORDER BY id_producto DESC LIMIT 1"
            self._conection.commit()
            self._cursor.execute(script)
            result = self._cursor.fetchone()
            return result[0]

        def editar_producto(self, id, productos: list[(int, int)]):
            self.Delete(id)
            producto = self.ReadSimplified("paquete")
            self.Create(producto)
            self.agregarProductosPaquete(self.getLastId(), productos)

        def readProductosPaquete(self, id):
            print(f"id: {id}")
            script = ("SELECT p1.*, p2.nombre, p3.nombre FROM paquete_producto as p1 INNER JOIN producto as p2 "
                      "ON p1.id_paquete = p2.id_producto INNER JOIN producto as p3 ON p1.id_producto = p3.id_producto "
                      f"WHERE p1.id_paquete = {id};")
            self._conection.commit()
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            print(result)
            return result


        """""
        def elimarProductoPaquete(self, id, productos: list[int]):
            for producto in productos:
                script = f"DELETE FROM paquete_producto WHERE id_paquete = {id} AND id_producto = {producto}"
                self._cursor.execute(script)
                self._conection.commit()
        """""
        """""
        def editarProducto(self, id, productos: list[int]):
            script = f"SELECT * FROM paquete_producto WHERE id_paquete= {id}"
            self._conection.commit()
            self._cursor.execute(script)
            result = self._cursor.fetchall()
            for resultado in result:
                if resultado[0] in productos:
                    index = productos.index(resultado[0])
                    productos.pop(index)
                else:
                    self.elimarProductoPaquete(id, [resultado[0]])
                    
            for producto in productos:
        """""