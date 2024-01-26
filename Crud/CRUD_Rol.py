from Crud.AbstractCRUD import CRUD

if __name__ != "__main__":

    class Rol:
        def __init__(self, nombre:str, id: int = None):
            
            self.__id = None
            if id is not None:
                self._setId(id)
            self.setNombre(nombre)

        def _getId(self) -> int:
            return self.__id

        def _setId(self, id:int) -> None:
            if isinstance(id, int) and id > 0:
                self.__id = id
            else:
                raise ValueError("id must be an int and must be greater than 0")

        def getNombre(self) -> str:
            return self.__nombre

        def setNombre(self, nombre: str) -> None:
            if isinstance(nombre, str) and nombre != "":
                self.__nombre = nombre
            else:
                raise ValueError("Nombre must be a string and can't be an empty string")

    class CrudRol(CRUD):
        def __init__(self, conection):
            super().__init__(conection)

        def Read(self, id=None):
            if id is None:
                script = f"SELECT * FROM rol"
                self._cursor.execute(script)
                results = self._cursor.fetchall()
                roles = []
                for result in results:
                    roles.append(Rol(id=result[0], nombre=result[1]))
                return roles
            elif id is not None:
                script = f"SELECT * FROM rol WHERE id_rol={id}"
                self._cursor.execute(script)
                results = self._cursor.fetchone()
                return Rol(results[0], results[1])

        def Delete(self, id: int):
            if isinstance(id, int):
                script = f"DELETE FROM rol WHERE id_rol={id}"
                self._cursor.execute(script)
                self._conection.commit()
            else:
                raise ValueError("id must be an Int")

        def Update(self, id: int, object: Rol):
            if isinstance(id, int):
                if isinstance(object, Rol):
                    script = f"UPDATE rol SET nombre='{object.getNombre()}' WHERE id_rol={id}"
                    self._cursor.execute(script)
                    self._conection.commit()
                else:
                    raise ValueError("object was expected to be type: Rol")
            else:
                raise ValueError("id must be an Int")

        def Create(self, rol: Rol):
            script = ("INSERT INTO rol(nombre)"
                      f"VALUES('{rol.getNombre()}')")
            self._cursor.execute(script)
            self._conection.commit()
