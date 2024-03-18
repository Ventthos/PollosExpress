from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
import datetime

class Admin_Ventas(QMainWindow):
    def __init__(self):
        super().__init__()

        # Conexión a la base de datos
        self.__connection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )

        self.initUI()
        self.cargar_ventas()

    def initUI(self):
        self.setWindowTitle('Pollos Express | Ventas (Administrador)')
        self.resize(1200, 700)
        self.setWindowIcon(QIcon('../img/logo.ico'))

        # Crear widget de tabla para la primera tabla (venta)
        self.table_venta = QTableWidget()
        self.table_venta.setColumnCount(6)
        self.table_venta.setHorizontalHeaderLabels(['ID Venta', 'Fecha', 'Total Compra ($)', 'ID Pago', 'ID Empleado', 'ID Cliente'])
        self.table_venta.cellClicked.connect(self.seleccionar_venta)

        # Crear widget de tabla para la segunda tabla (venta_producto)
        self.table_venta_producto = QTableWidget()
        self.table_venta_producto.setColumnCount(4)
        self.table_venta_producto.setHorizontalHeaderLabels(['ID Venta Producto', 'Cantidad', 'ID Venta', 'ID Producto'])

        # Crear botón para actualizar los datos
        self.actualizar_button = QPushButton('Actualizar Datos')
        self.actualizar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.actualizar_button.clicked.connect(self.actualizar_lista)

        # Crear botón para eliminar ventas
        self.eliminar_venta_button = QPushButton('Eliminar Venta')
        self.eliminar_venta_button.setStyleSheet("background-color: #c9636c; color: white; font-weight: bold;")
        self.eliminar_venta_button.clicked.connect(self.eliminar_venta)

        # Crear layout para los botones de actualizar y eliminar
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.actualizar_button)
        button_layout.addWidget(self.eliminar_venta_button)

        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_venta)
        main_layout.addWidget(self.table_venta_producto)
        main_layout.addLayout(button_layout)  # Agregar el layout de botones al layout principal

        # Crear widget central y establecer el diseño
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def cargar_ventas(self):
        cursor = self.__connection.cursor()
        query_venta = "SELECT id_venta, fecha_De_Venta, total_De_Compra, id_pago, id_empleado, id_cliente FROM venta ORDER BY id_venta ASC"
        query_venta_producto = "SELECT id_venta_producto, cantidad, id_venta, id_producto FROM venta_producto ORDER BY id_venta_producto ASC"

        cursor.execute(query_venta)
        ventas = cursor.fetchall()
        cursor.execute(query_venta_producto)
        ventas_producto = cursor.fetchall()

        cursor.close()

        self.table_venta.setRowCount(0)
        self.table_venta_producto.setRowCount(0)

        for row_number, venta in enumerate(ventas):
            self.table_venta.insertRow(row_number)
            for column_number, data in enumerate(venta):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta.setItem(row_number, column_number, item)

        for row_number, venta_producto in enumerate(ventas_producto):
            self.table_venta_producto.insertRow(row_number)
            for column_number, data in enumerate(venta_producto):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta_producto.setItem(row_number, column_number, item)

    def actualizar_lista(self):
        self.cargar_ventas()
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))

    def seleccionar_venta(self, row, column):
        self.selected_venta_id = self.table_venta.item(row, 0).text()

    def eliminar_venta(self):
        if not hasattr(self, 'selected_venta_id'):
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una venta para eliminar.')
            return

        cursor = self.__connection.cursor()

        # Eliminar registros de venta_producto asociados a la venta seleccionada
        delete_venta_producto_query = "DELETE FROM venta_producto WHERE id_venta = %s"
        cursor.execute(delete_venta_producto_query, (self.selected_venta_id,))
        self.__connection.commit()

        # Ahora puedes eliminar la venta seleccionada
        delete_query = "DELETE FROM venta WHERE id_venta = %s"
        cursor.execute(delete_query, (self.selected_venta_id,))
        self.__connection.commit()

        cursor.close()

        self.cargar_ventas()
        QMessageBox.information(self, 'Información', 'La venta ha sido eliminada correctamente.')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana = Admin_Ventas()
    ventana.show()
    sys.exit(app.exec_())
