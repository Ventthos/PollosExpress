from RawInterfaces.Pagar import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIntValidator
import time
from tkinter import messagebox

class PagarInterface(QWidget, Ui_Form):
    def __init__(self, conection, idUsuario, parent):
        super().__init__()
        super().setupUi(self)
        self.lineEditPagado.setValidator(QIntValidator(0,100000))
        self.lineEditPagado.textChanged.connect(self.calcularCambio)
        self.buttonFinalizarCompra.setEnabled(False)
        self.connection = conection
        self.cursor = self.connection.cursor()
        self.idU = idUsuario
        self.buttonFinalizarCompra.clicked.connect(self.subirVenta)
        self.parentWidget = parent

    def setTable(self, table:QTableWidget, total:str):
        self.lineEditPagado.setText("")
        self.lineEditCambio.setText("")
        self.lineEditCambio.setEnabled(False)
        self.TablaVenta.setRowCount(table.rowCount())
        for elemento in range(table.rowCount()):
            for column in range(table.columnCount()):
                dato = table.item(elemento, column).text()
                celda = QTableWidgetItem(dato)
                self.TablaVenta.setItem(elemento, column, celda)
        self.LabelPrecioTotalDecimal.setText(total)
        self.lineEditPagado_2.setEnabled(True)
        total = total.split("$")[1]
        self.lineEditPagado_2.setText(total)
        self.lineEditPagado_2.setEnabled(False)

    def calcularCambio(self):
        self.lineEditCambio.setEnabled(True)
        if self.lineEditPagado.text() != "":
            cambio = float(self.lineEditPagado.text()) - float(self.lineEditPagado_2.text())
            if cambio >= 0:
                self.lineEditCambio.setText(f"{cambio}")
                self.buttonFinalizarCompra.setEnabled(True)
            else:
                self.lineEditCambio.setText(f"Fondos insuficientes")
                self.buttonFinalizarCompra.setEnabled(False)
        self.lineEditCambio.setEnabled(False)


    def subirVenta(self):
        scrip = "INSERT INTO venta(fecha_De_Venta, total_De_Compra, id_pago, id_empleado) VALUES(%s, %s, %s, %s);"
        actual_time = time.localtime()
        timeFormatted = time.strftime("%Y/%m/%d", actual_time)

        values = (timeFormatted, float(self.LabelPrecioTotalDecimal.text().split("$")[1]), 1, self.idU)
        self.connection.cursor().execute(scrip, values)
        self.connection.commit()

        scrip2 = "SELECT MAX(id_Venta) FROM venta;"
        cursor = self.cursor
        cursor.execute(scrip2)
        idelast = cursor.fetchone()
        scrip3 = "INSERT INTO venta_producto(id_venta, id_producto, cantidad, subtotal) VALUES(%s, %s, %s, %s);"

        for i in range(self.TablaVenta.rowCount()):
            # Obtiene el Id
            values = (
                idelast[0], int(self.TablaVenta.item(i, 4).text()), int(self.TablaVenta.item(i, 1).text()),
                float(self.TablaVenta.item(i, 3).text()))
            self.connection.cursor().execute(scrip3, values)
            self.connection.commit()

        messagebox.showinfo("Listo", "La venta ha sido agregada")

        self.lineEditPagado.setText("")
        self.lineEditCambio.setText("")
        self.parentWidget.TablaVenta.setRowCount(0)
        self.parentWidget.LabelPrecioTotalDecimal.setText("$0")
        self.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = PagarInterface()
    ui.show()
    sys.exit(app.exec_())