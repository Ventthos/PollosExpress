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
    def BuscarPromocionesRelacionadas(self, arrDatos):
        today = datetime.date.today()
        dias = []
        if self.Promociones == [] and not self.keepActive:
            script = ("SELECT p.id_promocion, tdp.nombre , p.fecha_de_inicio, p.fecha_de_finalizacion, pr.nombre, dp.dias, p.descripcion "
                      "FROM promocion p "
                      "INNER JOIN producto pr "
                      "ON p.id_producto = pr.id_producto "
                      "INNER JOIN tipo_de_promocion tdp "
                      "ON tdp.id_tipo_promocion = p.id_tipo_promocion "
                      "INNER JOIN promocion_dia dp "
                      "ON dp.id_promocion = p.id_promocion "
                      "WHERE pr.id_producto = %s and p.activo = 'V'")
            self.cursor.execute(script, [self.idproducto])
            self.Promociones = self.cursor.fetchall()

            for dia in self.Promociones:
                if dia[5] == 'Lunes':
                    dias.append(0)
                if dia[5] == 'Martes':
                    dias.append(1)
                if dia[5] == 'Miercoles':
                    dias.append(2)
                if dia[5] == 'Jueves':
                    dias.append(3)
                if dia[5] == 'Viernes':
                    dias.append(4)
                if dia[5] == 'Sábado':
                    dias.append(5)
                if dia[5] == 'Domingo':
                    dias.append(6)
        print("Los dias de tu promocion de aplicar son ", dias)
        if self.Promociones != [] and self.Promociones[0][2] <= self.Promociones[0][3] and not self.keepActive and today.weekday() in dias:
            respuesta = QtWidgets.QMessageBox.question(self.parent, "Promocion!", f"Hay una promocion para este producto, desea aplicarla?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        else:
            respuesta = QtWidgets.QMessageBox.No

        print(self.Promociones)
        if not self.keepActive and self.keepActive is not None:
            if respuesta == QtWidgets.QMessageBox.No:
                self.keepActive = False
            if respuesta == QtWidgets.QMessageBox.Yes:
                print("Le dio que si")
                self.keepActive = True
                self.allowed = True
        if self.allowed:
            print("Voy a hacer valida la promocion")
            self.ValidarPromocion(arrDatos)


    def ValidarPromocion(self, arrDatos):
        print("Validando")
        arrDatosCopia = arrDatos
        self.subtotal_actual = 0.0
        for result in self.Promociones:
            if result[1] == "2X1":
                if int(arrDatosCopia[1]) == 1:
                    cantidadAAplicar = 1
                    break
                if int(arrDatosCopia[1]) % 2 == 0:
                    cantidadAAplicar = int(arrDatosCopia[1]) // 2
                    print(f"Puedo aplicar {cantidadAAplicar} promociones de 2x1")
                    arrDatosCopia[1] = str(int(arrDatosCopia[1]) - cantidadAAplicar)
                    break
                if int(arrDatosCopia[1]) % 2 != 0:
                    cantidadAAplicar = int(arrDatosCopia[1]) // 2
                    sobrante = int(arrDatosCopia[1]) % 2
                    print(f"Puedo aplicar {cantidadAAplicar} y sobran {sobrante}")
                    arrDatosCopia[1] = str(int(arrDatosCopia[1]) - cantidadAAplicar)
                    break
        arrDatosCopia[3] = str(int(arrDatosCopia[1]) * float(arrDatosCopia[2]))
        print(f"Mi arr quedo asi: {arrDatosCopia}")


        #Agregamos la row para mi promocioncita ay como la quiero a mi promocioncita
        yaexiste = False
        IndiceNombre = self.BuscarEnTablaVentas(arrDatos[0] + " 2X1")
        if IndiceNombre != None:
            yaexiste = True
            print(f"Ya existe un producto con el nombre: {arrDatos[0] + ' 2X1'}")
        else:
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
        values = [arrDatos[0] + " 2X1",
                  str(cantidadAAplicar),
                  "0.0",
                  "0.0",
                  arrDatos[4]]
        if yaexiste:
            cantidadprevia = self.table.item(IndiceNombre,1)
            self.table.setItem(IndiceNombre, 1, QtWidgets.QTableWidgetItem(str(int(cantidadprevia.text()) + int(values[1]))))
        if not yaexiste:
            for i in range(5):
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

    def CalcularTotal(self):
        if self.allowed:
            total_anterior = 0.0
            if self.row_count > 0:  # Verificar si hay filas anteriores en la tabla
                total_anterior = float(self.table.item(self.row_count - 1, 4).text())  # Obtener el total de la fila anterior
            total_actual = total_anterior + self.subtotal_actual

            # Agregar el total actual a la tabla
            self.table.setItem(self.row_count, 4, QtWidgets.QTableWidgetItem(str(total_actual)))

    def BuscarEnTablaVentas(self, name: str):
        if self.table.rowCount() > 0:
            for fila in range(self.table.rowCount()):
                if self.table.item(fila, 0) != None:
                    nombreProducto = self.table.item(fila, 0).text()
                else:
                    nombreProducto = None
                print(nombreProducto)
                if nombreProducto == name:
                    return fila
        return None