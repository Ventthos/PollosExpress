from RawInterfaces.Pagar import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem


class PagarInterface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

    def setTable(self, table:QTableWidget):
        self.TablaVenta.setRowCount(table.rowCount())
        for elemento in range(table.rowCount()):
            for column in range(table.columnCount()):
                dato = table.item(elemento, column).text()
                celda = QTableWidgetItem(dato)
                self.TablaVenta.setItem(elemento, column, celda)


    def dropTable(self):
        self.verticalLayout.removeWidget(self.table)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = PagarInterface()
    ui.show()
    sys.exit(app.exec_())