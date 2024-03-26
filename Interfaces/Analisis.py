from RawInterfaces.Analisis import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import mysql.connector
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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
        script = (f"SELECT SUM(total_De_Compra) FROM venta WHERE WEEK(fecha_De_Venta, 1) = week(\"{fecha}\", 1)"
                  f" AND YEAR(fecha_De_Venta) = YEAR(\"{fecha}\");")
        self.cursor.execute(script)
        total = self.cursor.fetchone()[0]
        return total

    def calcularGastos(self, fecha):
        self.conection.commit()
        script = (f"SELECT SUM(monto) FROM gasto WHERE WEEK(fecha, 1) = week(\"{fecha}\", 1)"
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

    def rewind(self):
        self.ticks -= 1
        self.setFecha()

    def next(self):
        self.ticks += 1
        self.setFecha()

    def setFecha(self):
        monday, sunday = self.calcularSemana()
        #toDo Cambiar esto a una función más organizada
        ventas = self.calcularVentas(monday)
        if ventas is not None:
            self.lineEditVentasTot.setText(f"${ventas}")
        else:
            ventas = 0
            self.lineEditVentasTot.setText("$0.0")

        gastos = self.calcularGastos(monday)
        # toDo de preferencia poner esto a que lo regrese y ya en otra funcion ponerlo
        if gastos is not None:
            self.lineEditGastosTot.setText(f"${gastos}")
        else:
            gastos = 0
            self.lineEditGastosTot.setText("$0.0")

        self.GananciasTotales.setText(f"${ventas-gastos}")

        # Calcula venta
        sumas = self.calcularSumasDia(monday)
        sumaTotal = 0
        for suma in sumas:
            sumaTotal+=suma

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



        #############
        monday = monday.strftime("%d/%m/%Y")
        sunday = sunday.strftime("%d/%m/%Y")
        self.labelTiempo.setText(f"Semana {monday} - {sunday}")

    def calcularSemana(self):
        today = datetime.date.today()
        monday = today + datetime.timedelta(days=-today.weekday(), weeks=self.ticks)
        sunday = today + datetime.timedelta(days=6 - today.weekday(), weeks=self.ticks)
        return monday, sunday

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Analisis()
    ui.show()
    sys.exit(app.exec_())