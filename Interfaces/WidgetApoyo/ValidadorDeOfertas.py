import datetime
import mysql.connector
from PyQt5 import QtWidgets, QtGui, QtCore
class Validador:
    def __init__(self, idProducto, table :QtWidgets.QTableWidget, parent):
        self.idproducto = idProducto
        self.table = table
        self.parent = parent
        self.keepActive = False
        self.allowed = False
        self.Promociones = []
        self.conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.cursor = self.conection.cursor()
    def BuscarPromocionesRelacionadas(self):
        if self.Promociones == [] and not self.keepActive:
            script = "SELECT p.id_promocion, tdp.nombre , p.fecha_de_inicio, p.fecha_de_finalizacion, pr.nombre FROM promocion p INNER JOIN producto pr ON p.id_producto = pr.id_producto INNER JOIN tipo_de_promocion tdp ON tdp.id_tipo_promocion = p.id_tipo_promocion WHERE pr.id_producto = %s"
            self.cursor.execute(script, [self.idproducto])
            self.Promociones = self.cursor.fetchall()
        if self.Promociones != [] and self.Promociones[0][2] <= self.Promociones[0][3] and not self.keepActive:
            respuesta = QtWidgets.QMessageBox.question(self.parent, "Promocion!", "Hay una promocion con este producto, desea aplicarla?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        else:
            return

        print(self.Promociones)
        if not self.keepActive and self.keepActive is not None:
            if respuesta == QtWidgets.QMessageBox.No:
                self.keepActive = False
            if respuesta == QtWidgets.QMessageBox.Yes:
                print("Le dio que si")
                self.keepActive = True
                self.allowed = True
        if self.allowed:
            self.ValidarPromocion()


    def ValidarPromocion(self):
        print("Validando")
        for result in self.Promociones:
            if result[1] == "2X1":
                columna, fila = self.encontrarFila()
                row_count = self.table.rowCount()
                self.table.insertRow(row_count)
                values = [self.table.item(columna, fila), self.table.item(columna + 1, fila), 0, 0, self.table.item(columna + 4, fila) ]
                for i in range(4):
                    self.table.setItem(row_count, i, QtWidgets.QTableWidgetItem(values[i]))
    def encontrarFila(self):
        for result in self.Promociones:
            texto_busqueda = result[4].strip().lower()
            for fila in range(self.table.rowCount()):
                for columna in range(self.table.columnCount()):
                    item = self.table.item(fila, columna)
                    if item is not None and texto_busqueda in item.text().strip().lower():
                        print(columna,fila)
                        return (columna, fila)



