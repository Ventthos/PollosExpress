from RawInterfaces.Pagar import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIntValidator


class PagarInterface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.lineEditPagado.setValidator(QIntValidator(0,100000))
        self.lineEditPagado.textChanged.connect(self.calcularCambio)
        self.buttonFinalizarCompra.setEnabled(False)


    def setTable(self, table:QTableWidget, total:str):
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

    def dropTable(self):
        self.verticalLayout.removeWidget(self.table)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = PagarInterface()
    ui.show()
    sys.exit(app.exec_())