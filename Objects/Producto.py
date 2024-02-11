from dataclasses import dataclass
@dataclass
class Producto:
        id : int
        nombre : str
        descripcion : str
        precio : float
        imagen : str
        activo : str


from dataclasses import dataclass


# @dataclass
# class MiClase:
#     _atributo1: int
#     _atributo2: str
#
#     # Getter y setter para atributo1
#     @property
#     def atributo1(self):
#         return self._atributo1
#
#     @atributo1.setter
#     def atributo1(self, value):
#         self._atributo1 = value
#
#     # Getter y setter para atributo2
#     @property
#     def atributo2(self):
#         return self._atributo2
#
#     @atributo2.setter
#     def atributo2(self, value):
#         self._atributo2 = value
#
#
# # Crear instancia de la clase con valores iniciales
# valores_atributos = [10, "texto"]
# objeto = MiClase(*valores_atributos)
#
# # Imprimir valores iniciales
# print(objeto.atributo1)  # 10
# print(objeto.atributo2)  # texto
#
# # Modificar valores usando setters
# objeto.atributo1 = 20
# objeto.atributo2 = "nuevo texto"
#
# # Imprimir valores modificados
# print(objeto.atributo1)  # 20
# print(objeto.atributo2)  # nuevo texto
