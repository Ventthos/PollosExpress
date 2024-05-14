import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
from datetime import datetime

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
        self.table_venta.setHorizontalHeaderLabels(['ID Venta', 'Fecha', 'Total Compra ($)', 'Tipo de Pago', 'Empleado', 'Cliente'])
        self.table_venta.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_venta.setSelectionMode(QAbstractItemView.SingleSelection)

        # Crear widget de tabla para la segunda tabla (venta_producto)
        self.table_venta_producto = QTableWidget()
        self.table_venta_producto.setColumnCount(4)
        self.table_venta_producto.setHorizontalHeaderLabels(['ID Venta Producto', 'ID Venta', 'Cantidad', 'Producto'])

        # Ajustar ancho de columnas de la tabla venta
        self.table_venta.setColumnWidth(0, 135)  # ID Venta
        self.table_venta.setColumnWidth(1, 200)  # Fecha
        self.table_venta.setColumnWidth(2, 200)  # Total Compra
        self.table_venta.setColumnWidth(3, 200)  # ID Pago
        self.table_venta.setColumnWidth(4, 200)  # ID Empleado
        self.table_venta.setColumnWidth(5, 200)  # ID Cliente

        # Ajustar ancho de columnas de la tabla venta_producto
        self.table_venta_producto.setColumnWidth(0, 255)  # ID Venta Producto
        self.table_venta_producto.setColumnWidth(1, 300)  # Cantidad
        self.table_venta_producto.setColumnWidth(2, 300)  # ID Venta
        self.table_venta_producto.setColumnWidth(3, 300)  # ID Producto

        # Crear botón para actualizar datos
        self.actualizar_button = QPushButton('Actualizar Datos')
        self.actualizar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.actualizar_button.clicked.connect(self.actualizar_datos)

        # Crear botón para eliminar ventas
        self.eliminar_button = QPushButton('Eliminar Venta')
        self.eliminar_button.setStyleSheet("background-color: #c9636c; color: white; font-weight: bold;")
        self.eliminar_button.clicked.connect(self.eliminar_venta)

        # Crear botón para generar reporte
        self.reporte_button = QPushButton('Generar Reporte')
        self.reporte_button.setStyleSheet("background-color: #6495ED; color: white; font-weight: bold;")
        self.reporte_button.clicked.connect(self.generar_reporte)

        # Crear layout para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.actualizar_button)
        botones_layout.addWidget(self.eliminar_button)
        botones_layout.addWidget(self.reporte_button)

        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_venta)
        main_layout.addWidget(self.table_venta_producto)
        main_layout.addLayout(botones_layout)

        # Crear widget central y establecer el diseño
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Conectar la señal itemSelectionChanged de la tabla venta a cargar_productos_venta
        self.table_venta.itemSelectionChanged.connect(self.cargar_productos_venta)

    def cargar_ventas(self):
        cursor = self.__connection.cursor()
        query_venta = ("SELECT id_venta, fecha_De_Venta, total_De_Compra, P.nombre, CONCAT(E.nombre,\" \" ,"
                       "E.apellido_paterno), id_cliente FROM venta as V JOIN pago as P ON V.id_pago = P.id_pago JOIN e"
                       "mpleado E ON E.id_empleado = V.id_empleado ORDER BY id_venta DESC;")

        cursor.execute(query_venta)
        ventas = cursor.fetchall()

        cursor.close()

        self.table_venta.setRowCount(0)

        for row_number, venta in enumerate(ventas):
            self.table_venta.insertRow(row_number)
            for column_number, data in enumerate(venta):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta.setItem(row_number, column_number, item)

    def cargar_productos_venta(self):
        selected_row = self.table_venta.currentRow()
        if selected_row != -1:
            id_venta = self.table_venta.item(selected_row, 0).text()
            cursor = self.__connection.cursor()
            query_productos_venta = ("SELECT id_venta_producto, cantidad, id_venta, P.nombre FROM venta_producto VP "
                                     "INNER JOIN producto P ON P.id_producto = VP.id_producto WHERE id_venta = %s;")
            cursor.execute(query_productos_venta, (id_venta,))
            productos_venta = cursor.fetchall()
            cursor.close()

            self.table_venta_producto.setRowCount(0)

            for row_number, producto_venta in enumerate(productos_venta):
                self.table_venta_producto.insertRow(row_number)

                item = QTableWidgetItem(str(producto_venta[0]))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta_producto.setItem(row_number, 0, item)

                item = QTableWidgetItem(str(producto_venta[2]))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta_producto.setItem(row_number, 1, item)

                item = QTableWidgetItem(str(producto_venta[1]))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta_producto.setItem(row_number, 2, item)

                item = QTableWidgetItem(str(producto_venta[3]))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_venta_producto.setItem(row_number, 3, item)
                """""
                for column_number, data in enumerate(producto_venta):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.table_venta_producto.setItem(row_number, column_number, item)
                """""
        else:
            # Limpiar la tabla venta_producto si no se selecciona ninguna venta
            self.table_venta_producto.setRowCount(0)

    def generar_reporte(self):
        # Solicitar el ID del administrador
        id_administrador, ok = QInputDialog.getText(self, 'ID de Administrador', 'Ingrese su ID de Administrador:')
        
        # Verificar si se presionó "Aceptar" en el cuadro de diálogo
        if ok:
            # Crear la carpeta para los reportes si no existe
            carpeta_reportes = "Reporte de ventas"
            if not os.path.exists(carpeta_reportes):
                os.makedirs(carpeta_reportes)

            # Obtener la fecha actual
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")

            # Obtener los datos de la tabla venta
            reporte_venta = []
            for row in range(self.table_venta.rowCount()):
                row_data = [self.table_venta.item(row, col).text() for col in range(self.table_venta.columnCount())]
                reporte_venta.append(row_data)

            # Crear el contenido del reporte
            reporte_content = f"{'=' * 30}\nReporte de ventas ({fecha_actual})\n{'=' * 30}\n\n"
            reporte_content += "Tabla Venta:\n"
            for row in reporte_venta:
                reporte_content += f"{'-' * 30}\n"
                reporte_content += f"ID Venta: {row[0]}\nFecha: {row[1]}\nTotal Compra ($): {row[2]}\n Tipo de Pago: {row[3]}\nEmpleado: {row[4]}\nCliente: {row[5]}\n"
            reporte_content += f"{'-' * 30}\n"
            reporte_content += f"Reporte generado en: {fecha_actual} por el administrador con el ID {id_administrador}."

            # Guardar el reporte en un archivo de texto
            nombre_archivo = f"{carpeta_reportes}/Reporte_de_ventas_{fecha_actual.replace(':', '')}.txt"
            try:
                with open(nombre_archivo, "w") as file:
                    file.write(reporte_content)
                QMessageBox.information(self, 'Reporte Generado', f'El reporte de ventas ha sido generado exitosamente como "{nombre_archivo}"')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Error al generar el reporte: {str(e)}')

    def eliminar_venta(self):
        selected_row = self.table_venta.currentRow()
        if selected_row != -1:
            id_venta = self.table_venta.item(selected_row, 0).text()
            confirmation = QMessageBox.question(self, 'Eliminar Venta', f'¿Estás seguro de eliminar la venta con ID {id_venta}? Esta acción no se puede deshacer.',
                                                 QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                try:
                    cursor = self.__connection.cursor()
                    delete_query = "DELETE FROM venta WHERE id_venta = %s"
                    cursor.execute(delete_query, (id_venta,))
                    self.__connection.commit()
                    QMessageBox.information(self, 'Venta Eliminada', f'Se ha eliminado la venta con ID {id_venta}.')
                    self.cargar_ventas()  # Recargar la tabla después de eliminar
                    self.cargar_productos_venta()  # Limpiar la tabla de productos
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'Error al eliminar la venta: {str(e)}')
                finally:
                    cursor.close()
        else:
            QMessageBox.warning(self, 'Error', 'Por favor, seleccione una venta para eliminar.')

    def actualizar_datos(self):
        self.cargar_ventas()
        self.cargar_productos_venta()
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana = Admin_Ventas()
    ventana.show()
    sys.exit(app.exec_())
