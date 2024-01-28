class Empleado:
    __contraseña = str
    __id = int
    __nombre = str
    __apellido_paterno = str
    __apellido_materno = str
    __celular = str
    __sueldo = float
    __id_rol = int
    __administrador = bool

    def __init__(self, nombre: str, apellido_paterno: str, apellido_materno: str, celular: str, sueldo: float,
                 id_rol: int, administrator: bool, active: str, contraseña: str = None, id: int = None):
        if id is not None:
            self._setId(id)
        if contraseña is not None:
            self.setContraseña(contraseña)
        self.setNombre(nombre)
        self.setApellido_paterno(apellido_paterno)
        self.setApellido_materno(apellido_materno)
        self.setCelular(celular)
        self.setSueldo(sueldo)
        self.setIdRol(id_rol)
        self.setAdministrador(administrator)
        self.activo = active

    def getActivo(self):
        return self.activo
    def getId(self):
        return self.__id

    def _setId(self, id: int):
        if isinstance(id, int):
            if id > 0:
                self.__id = id
            else:
                raise ValueError("El id debe ser mayor a 0")
        else:
            raise ValueError("El id debe ser un número, sin decimales")

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre: str):
        if nombre != "":
            self.__nombre = nombre
        else:
            raise ValueError("El campo nombre no puede ir vacío")

    def getApellido_paterno(self):
        return self.__apellido_paterno

    def setApellido_paterno(self, apellido_paterno):
        if apellido_paterno != "":
            self.__apellido_paterno = apellido_paterno
        else:
            raise ValueError("El campo Apellido paterno no puede ir vacío")

    def getApellido_materno(self):
        return self.__apellido_materno

    def setApellido_materno(self, apellido_materno):
        if apellido_materno != "":
            self.__apellido_materno = apellido_materno
        else:
            raise ValueError("El campo Apellido materno no puede ir vacío")

    def getCelular(self):
        return self.__celular

    def setCelular(self, celular: str):
        if celular != "":
            self.__celular = celular
        else:
            raise ValueError("El campo celular no puede ir vacío")

    def getSueldo(self):
        return self.__sueldo

    def setSueldo(self, sueldo: float):
        if isinstance(sueldo, float) or isinstance(sueldo, int):
            if sueldo >= 0:
                self.__sueldo = sueldo
            else:
                raise ValueError("El campo sueldo no puede ser menor a 0")
        else:
            raise ValueError("El sueldo debe ser un numero entero o decimal")

    def getIdRol(self):
        return self.__id_rol

    def setIdRol(self, id_rol: int):
        self.__id_rol = id_rol



    def getAdministrador(self):
        return self.__administrador

    def setAdministrador(self, administrador: bool):
        self.__administrador = administrador


    def getContraseña(self):
        return self.__contraseña

    def setContraseña(self, contraseña: str):
        self.__contraseña = contraseña
