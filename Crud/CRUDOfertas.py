import mysql.connector.errors
from Crud.AbstractCRUD import CRUD

class Promocion():
    def __init__(self,id, id_producto : int, descripcion : str, fechaInicio : str, fechaFinal : str, id_tipopromocion : int ):
        self.id = None
        if id is not None:
            self.id = id
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.fechainicio = fechaInicio
        self.fechafinal = fechaFinal
        self.id_tipopromocion = id_tipopromocion


class CRUDPromociones(CRUD):
    def __init__(self, conection):
        super().__init__(conection)


    def Create(self, promocion):
        script = ("INSERT INTO promocion(id_producto, descripcion, fecha_de_inicio, fecha_de_finalizacion, "
                  "id_tipo_promocion) VALUES (%s, %s, %s, %s,%s)")
        datos_promocion = (promocion.id_producto, promocion.descripcion, promocion.fechainicio, promocion.fechafinal, promocion.id_tipopromocion)
        self._cursor.execute(script, datos_promocion)  # seria fetch si pidiera datos
        self._conection.commit()  # commit siempre que se modifique la tabla

    def Read(self, id=None):
        con = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        if id is None:
            script = "SELECT * from promocion where activo = 'V'"
            cursor = con.cursor()
            cursor.execute(script)
            result = cursor.fetchall()
            promociones = []
            for resultado in result:
                promocion = Promocion(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                promociones.append(promocion)
            con.close()
            return promociones
        elif isinstance(id, int):
            script = f"SELECT * from promocion WHERE id_promocion = {id}"
            self._cursor.execute(script)
            resultado = self._cursor.fetchone()
            promocion = Promocion( resultado[0],resultado[1], resultado[2], resultado[3], resultado[4],resultado[5])
            con.close()
            return promocion
        else:
            raise ValueError("Id must be an integer")

    def Delete(self, id):
        if isinstance(id, int):
            oferta = self.Read(id)
            script = f"UPDATE promocion SET activo = 'F' WHERE id_promocion = {id}"
            self._cursor.execute(script)
            self._conection.commit()
        else:
            raise ValueError("Id must be an integer")

    def Update(self, id: int, promocion: Promocion):
        script = ("UPDATE promocion "
                  "SET id_producto = %s, descripcion = %s, fecha_de_inicio = %s, fecha_de_finalizacion = %s, id_promocion = %s  "
                  "WHERE id_promocion = %s")
        datos_promocion = (promocion.id_producto, promocion.descripcion, promocion.fechainicio, promocion.fechafinal, promocion.id, id)
        promocion = self.Read(id)
        self._cursor.execute(script, datos_promocion)
        self._conection.commit()

