from RawInterfaces.Analisis import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import mysql.connector
import datetime
import math

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

        self.GananciasTotales.setText(str(ventas-gastos))
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