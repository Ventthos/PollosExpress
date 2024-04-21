import decimal

from RawInterfaces.Analisis import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QFont
from tkinter import messagebox
import mysql.connector
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from dateutil.relativedelta import relativedelta

class Analisis(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )
        self.cursor = self.conection.cursor()
        self.ticks = 0

        # Conectar boton de regresar a evento
        self.buttonRewind.clicked.connect(self.rewind)

        # tambien el de avanzar semanas
        self.buttonFord.clicked.connect(self.next)

        # Poner las opciones el combo box
        self.comboBoxModos.addItems(["Semanal", "Mensual"])

        # Activar la gráfica
        self.figura = plt.Figure()
        self.canvas = FigureCanvas(self.figura)

        self.horizontalLayout_5.addWidget(self.canvas)

        # datosGrafica
        self.ventasGraphic = []
        self.gastosGrapic = []

        # Conectar eventos de cambiar graficas
        self.pushButtonGraf_L.clicked.connect(self.changeGraphicToVentas)
        self.pushButtonGraf_R.clicked.connect(self.changeGraphicToGastos)

        # Inicializar el programa
        self.setFecha()

        self.calcularGastosPorMes("2024-03-26")

        # Automaticamente cambiar de modo
        self.comboBoxModos.currentIndexChanged.connect(self.changeMode)

        # Refresh
        self.buttonBuscar.setText("")
        self.buttonBuscar.setIcon(QIcon("../img/refreshNegro.png"))
        self.buttonBuscar.clicked.connect(self.refrescar)

        # Responsividad
        self.referenceSize = 841

    def changeGraphicToGastos(self):
        if self.labelPaginaDatos_Graf.text()[0] == "1":
            self.setGrafic(self.gastosGrapic[0], self.gastosGrapic[1],self.gastosGrapic[2],
                           self.gastosGrapic[3],self.gastosGrapic[4])
        self.labelPaginaDatos_Graf.setText("2/2")

    def changeGraphicToVentas(self):
        if self.labelPaginaDatos_Graf.text()[0] == "2":
            self.setGrafic(self.ventasGraphic[0], self.ventasGraphic[1], self.ventasGraphic[2],
                           self.ventasGraphic[3], self.ventasGraphic[4])
        self.labelPaginaDatos_Graf.setText("1/2")

    def setGrafic(self, datos, names, title, xLabel, yLabel):
        self.figura.clear()
        cosas = names
        valores = datos
        ax = self.figura.add_subplot(111)  # Añadir una barra
        ax.bar(cosas, valores, color='red', width=0.4)
        ax.set_title(title)  # Establecer el título del gráfico
        ax.set_xlabel(xLabel)  # Establecer la etiqueta del eje x
        ax.set_ylabel(yLabel)  # Establecer la etiqueta del eje y
        self.canvas.draw()

    def calcularVentas(self, fecha):
        self.conection.commit()
        script = ""
        if self.comboBoxModos.currentText() == "Semanal":
            script = (f"SELECT SUM(total_De_Compra) FROM venta WHERE WEEK(fecha_De_Venta, 1) = week(\"{fecha}\", 1)"
                      f" AND YEAR(fecha_De_Venta) = YEAR(\"{fecha}\");")
        elif self.comboBoxModos.currentText() == "Mensual":
            script = (f"SELECT SUM(total_De_Compra) FROM venta WHERE MONTH(fecha_De_Venta) = MONTH(\"{fecha}\")"
                      f" AND YEAR(fecha_De_Venta) = YEAR(\"{fecha}\");")
        self.cursor.execute(script)
        total = self.cursor.fetchone()[0]
        return total

    def calcularGastos(self, fecha):
        self.conection.commit()
        script = ""
        if self.comboBoxModos.currentText() == "Semanal":
            script = (f"SELECT SUM(monto) FROM gasto WHERE WEEK(fecha, 1) = week(\"{fecha}\", 1)"
                      f" AND YEAR(fecha) = YEAR(\"{fecha}\");")
        elif self.comboBoxModos.currentText() == "Mensual":
            script = (f"SELECT SUM(monto) FROM gasto WHERE MONTH(fecha) = MONTH(\"{fecha}\")"
                      f" AND YEAR(fecha) = YEAR(\"{fecha}\");")
        self.cursor.execute(script)
        total = self.cursor.fetchone()[0]
        return total

    def calcularSumasDia(self, fecha):
        self.conection.commit()
        script = (f"SELECT DATE(fecha_De_Venta), SUM(total_De_Compra) FROM venta WHERE WEEK(fecha_De_Venta,1) = week(\"{fecha}\",1) "
                  f"AND YEAR(fecha_De_Venta) = YEAR(\"{fecha}\") GROUP BY DATE(fecha_De_Venta);")
        self.cursor.execute(script)
        sumas = self.cursor.fetchall()

        fecha -= datetime.timedelta(days=1)
        sumasSimplidified = []
        fechas = []
        for i in range(7):
            fecha = fecha + datetime.timedelta(days=1)
            fechas.append(fecha)

        for fechaInd in fechas:
            encontrado = False
            for elemento in sumas:
                if elemento[0] == fechaInd:
                    encontrado = True
                    sumasSimplidified.append(elemento[1])
            if not encontrado:
                sumasSimplidified.append(0)

        print("sumas finales")
        print(sumasSimplidified)
        return sumasSimplidified

    def calcularGastosDia(self, fecha:datetime.date):
        self.conection.commit()
        script = (f"SELECT DATE(fecha), SUM(monto) FROM gasto WHERE WEEK(fecha,1) = week(\"{fecha}\",1) "
                  f"AND YEAR(fecha) = YEAR(\"{fecha}\") GROUP BY DATE(fecha);")
        self.cursor.execute(script)
        sumas = self.cursor.fetchall()

        fecha -= datetime.timedelta(days=1)
        sumasSimplidified = []
        fechas = []
        for i in range(7):
            fecha = fecha + datetime.timedelta(days=1)
            fechas.append(fecha)

        for fechaInd in fechas:
            encontrado = False
            for elemento in sumas:
                if elemento[0] == fechaInd:
                    encontrado = True
                    sumasSimplidified.append(elemento[1])
            if not encontrado:
                sumasSimplidified.append(0)

        print("sumas finales")
        print(sumasSimplidified)
        return sumasSimplidified

    def calcularGastosPorMes(self, fecha):
        self.conection.commit()
        script = (f"SELECT MONTH(fecha), SUM(monto) FROM gasto WHERE MONTH(fecha) = MONTH(\"{fecha}\") "
                  f"AND YEAR(fecha) = YEAR(\"{fecha}\") GROUP BY MONTH(fecha);")
        self.cursor.execute(script)
        sumas = self.cursor.fetchall()

        sumasSimplidified = []
        for i in range(1, 13, 1):
            encontrado = False
            for elemento in sumas:
                if elemento[0] == i:
                    encontrado = True
                    sumasSimplidified.append(elemento[1])
            if not encontrado:
                sumasSimplidified.append(0)
        return sumasSimplidified

    def calcularVentasPorMes(self, fecha):
        self.conection.commit()
        script = (
            f"SELECT MONTH(fecha_De_Venta), SUM(total_De_Compra) FROM venta WHERE  "
            f"YEAR(fecha_De_Venta) = YEAR(\"{fecha}\") GROUP BY MONTH(fecha_De_Venta);")
        self.cursor.execute(script)
        sumas = self.cursor.fetchall()

        sumasSimplidified = []
        for i in range(1, 13, 1):
            encontrado = False
            for elemento in sumas:
                if elemento[0] == i:
                    encontrado = True
                    sumasSimplidified.append(elemento[1])
            if not encontrado:
                sumasSimplidified.append(0)
        return sumasSimplidified

    def rewind(self):
        self.ticks -= 1
        self.setFecha()

    def next(self):
        self.ticks += 1
        self.setFecha()

    def setFecha(self):
        # Moday es el lunes de la semana si esta en modo semanal y el dia actual hace X meses
        # si esta en mensual por un pequeño error xd
        if self.comboBoxModos.currentText() == "Semanal":
            monday, sunday = self.calcularSemana()
        else:
            monday = self.calcularMes()

        ventas = self.calcularVentas(monday)
        if ventas is not None:
            self.lineEditVentasTot.setText(f"${ventas}")
        else:
            ventas = 0
            self.lineEditVentasTot.setText("$0.0")
        gastos = self.calcularGastos(monday)
        if gastos is not None:
            self.lineEditGastosTot.setText(f"${gastos}")
        else:
            gastos = 0
            self.lineEditGastosTot.setText("$0.0")
        self.GananciasTotales.setText(f"${decimal.Decimal(ventas)-gastos}")

        if self.comboBoxModos.currentText() == "Semanal":
            self.operacionesSemanales(monday)
            monday = monday.strftime("%d/%m/%Y")
            sunday = sunday.strftime("%d/%m/%Y")
            self.labelTiempo.setText(f"Semana {monday} - {sunday}")
        elif self.comboBoxModos.currentText() == "Mensual":
            self.operacionesMensuales(monday)
            mes = monday.strftime("%B")
            self.labelTiempo.setText(f"Mes: {mes}")

    def operacionesSemanales(self, monday):
        # Calcula venta
        sumas = self.calcularSumasDia(monday)
        sumaTotal = 0
        for suma in sumas:
            sumaTotal += suma

        sumaTotal = round(sumaTotal / 7, 2)
        self.lineEditPromedioGananciaDia.setText(f"${sumaTotal}")

        self.ventasGraphic = [sumas, ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                              "Ventas", "Dia", "Total"]

        self.setGrafic(sumas, ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                       "Ventas", "Dia", "Total")
        self.labelPaginaDatos_Graf.setText("1/2")

        # Calcula gastos
        sumas = self.calcularGastosDia(monday)
        sumaTotal = 0
        for suma in sumas:
            sumaTotal += suma

        sumaTotal = round(sumaTotal / 7, 2)
        self.PromGastos.setText(f"${sumaTotal}")

        self.gastosGrapic = [sumas, ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                             "Gastos", "Dia", "Total"]


    def operacionesMensuales(self, dia:datetime.datetime):
        # Calcula ventas del mes
        sumas = self.calcularVentasPorMes(dia)

        # Esto obtiene la cantidad de días que tiene un mes
        siguiente_mes = dia + relativedelta(months=1)
        dias_en_mes = (siguiente_mes - dia).days

        sumaTotal = round(sumas[dia.month-1] / dias_en_mes, 2)
        self.lineEditPromedioGananciaDia.setText(f"${sumaTotal}")

        self.ventasGraphic = [sumas, ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"],
                              "Ventas", "Mes", "Total"]

        self.setGrafic(sumas, ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"],
                              "Ventas", "Mes", "Total")
        self.labelPaginaDatos_Graf.setText("1/2")

        # Calcula gastos del mes
        sumas = self.calcularGastosPorMes(dia)
        sumaTotal = round(sumas[dia.month-1] / dias_en_mes, 2)
        self.PromGastos.setText(f"${sumaTotal}")
        self.gastosGrapic = [sumas,
                              ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"],
                              "Gastos", "Mes", "Total"]


    def calcularSemana(self):
        today = datetime.date.today()
        monday = today + datetime.timedelta(days=-today.weekday(), weeks=self.ticks)
        sunday = today + datetime.timedelta(days=6 - today.weekday(), weeks=self.ticks)
        return monday, sunday

    def calcularMes(self):
        today = datetime.date.today()
        mesActual = today + relativedelta(months=self.ticks)
        return mesActual

    def changeMode(self):
        self.ticks = 0
        self.setFecha()

    def refrescar(self):
        self.setFecha()
        messagebox.showinfo("Reload", "Los datos han sido actualizados")

    def resizeEvent(self, event):
        font = QFont()
        font.setFamily("MS Shell Dlg 2")

        font.setPointSize(int((10/self.referenceSize) * self.width()))
        self.labelTiempo.setFont(font)

        font.setPointSize(int((8 / self.referenceSize) * self.width()))
        self.buttonRewind.setFont(font)
        self.buttonFord.setFont(font)
        self.pushButtonGraf_R.setFont(font)
        self.pushButtonGraf_L.setFont(font)
        self.buttonBuscar.setFont(font)

        font.setPointSize(int((11 / self.referenceSize) * self.width()))
        self.labelVentasTot.setFont(font)
        self.lineEditVentasTot.setFont(font)
        self.labelGastosTot.setFont(font)
        self.lineEditGastosTot.setFont(font)
        self.labelRendimientoTotal.setFont(font)
        self.GananciasTotales.setFont(font)
        self.text.setFont(font)
        self.lineEditPromedioGananciaDia.setFont(font)
        self.labelPromedioGastoDia.setFont(font)
        self.PromGastos.setFont(font)
        self.comboBoxModos.setFont(font)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Analisis()
    ui.show()
    sys.exit(app.exec_())