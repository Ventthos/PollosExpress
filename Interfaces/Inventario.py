from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector
import datetime


class Inventario(QMainWindow):
    def __init__(self):
        super().__init__()

        # Conexión a la base de datos
        self.__conection = mysql.connector.connect(
            user="u119126_pollos2LaVengazaDelPollo",
            host="174.136.28.78",
            port="3306",
            password="$ShotGunKin0805",
            database="u119126_pollos2LaVengazaDelPollo"
        )

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pollos Express | Inventario')
        self.resize(1200, 700)

        # Establecer ícono de la ventana
        self.setWindowIcon(QIcon('../img/logo.ico'))

        # Crear tabla y área de desplazamiento
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['ID Producto', 'Nombre Producto', 'Unidad', 'Cantidad', 'Estado'])

        # Establecer color de fondo de la tabla
        self.table_widget.setStyleSheet("background-color: white;")

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table_widget)
        scroll_area.setWidgetResizable(True)

        # Crear botón de búsqueda
        self.buscar_button = QPushButton('Buscar')
        self.buscar_button.setStyleSheet("background-color: #AFEEEE;")  # Establecer color de fondo

        # Conectar señal y slot
        self.buscar_button.clicked.connect(self.buscar_id)

        # Crear botón de información
        self.informacion_button = QPushButton('Ver Información')
        self.informacion_button.setStyleSheet("background-color: #AFEEEE;")  # Establecer color de fondo

        # Conectar señal y slot
        self.informacion_button.clicked.connect(self.mostrar_informacion)

        # Crear botón de actualización
        self.actualizar_button = QPushButton('Actualizar')
        self.actualizar_button.setStyleSheet("background-color: #AFEEEE;")  # Establecer color de fondo

        # Conectar señal y slot
        self.actualizar_button.clicked.connect(self.actualizar_datos)

        # Crear botón de candado
        self.candado_button = QPushButton('🔒')

        # Conectar señal y slot
        self.candado_button.clicked.connect(self.toggle_bloqueo)

        # Crear botón de exportar
        self.exportar_button = QPushButton('Exportar')
        self.exportar_button.setStyleSheet("background-color: #c9636c;")  # Establecer color de fondo

        # Conectar señal y slot
        self.exportar_button.clicked.connect(self.exportar_datos)

        # Crear cuadro de texto para ingresar ID
        self.id_producto_edit = QLineEdit()

        # Crear layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buscar_button)
        button_layout.addWidget(self.informacion_button)
        button_layout.addWidget(self.actualizar_button)
        button_layout.addWidget(self.candado_button)
        button_layout.addWidget(self.exportar_button)

        id_layout = QHBoxLayout()
        id_layout.addWidget(QLabel('ID Producto:'))
        id_layout.addWidget(self.id_producto_edit)

        layout = QVBoxLayout()
        layout.addLayout(id_layout)
        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Cargar datos
        self.cargar_datos()
        # Inicialmente los botones están habilitados
        self.botones_habilitados = True

        # Definir contraseñas para bloquear/desbloquear
        self.contraseña_bloqueo = "1234"
        self.contraseña_desbloqueo = "5678"
    def cargar_datos(self):
        cursor = self.__conection.cursor()
        #sql = "SELECT inventario.id_producto, inventario.nombre_producto, inventario.unidad, inventario.cantidad, inventario.estado FROM inventario INNER JOIN producto on producto.id_producto = inventario.id_producto"
        sql = "SELECT inventario.id_producto, inventario.nombre_producto, inventario.unidad, inventario.cantidad, inventario.estado FROM inventario INNER JOIN producto on producto.id_producto = inventario.id_producto"
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Limpiar la tabla antes de cargar nuevos datos
        self.table_widget.setRowCount(0)

        if not rows:
            QMessageBox.information(self, 'Información', 'No hay registros en la base de datos.')
            return

        for row_number, row_data in enumerate(rows):
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                # Alinear el texto al centro
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(row_number, column_number, item)

        # Ajustar el ancho de las columnas para que se ajusten al contenido
        self.table_widget.resizeColumnsToContents()

        # Establecer ancho mínimo para cada columna
        self.table_widget.setColumnWidth(0, 225)  # ID Producto
        self.table_widget.setColumnWidth(1, 260)  # Nombre Producto
        self.table_widget.setColumnWidth(2, 225)  # Unidad
        self.table_widget.setColumnWidth(3, 225)  # Cantidad
        self.table_widget.setColumnWidth(4, 220)  # Estado

    def buscar_id(self):
        id_producto = self.id_producto_edit.text()
        if id_producto:
            # Itera sobre las filas y compara el ID en la primera columna
            for row in range(self.table_widget.rowCount()):
                item = self.table_widget.item(row, 0)  # Suponiendo que el ID esté en la primera columna
                if item.text() == id_producto:
                    self.table_widget.selectRow(row)
                    self.table_widget.verticalScrollBar().setValue(row)
                    return
            QMessageBox.warning(self, 'Advertencia', 'El ID no se encuentra en la base de datos.')
        self.id_producto_edit.clear()

    def mostrar_informacion(self):
        # Obtener la fila seleccionada
        selected_row = self.table_widget.currentRow()
        
        # Verificar si se ha seleccionado una fila válida
        if selected_row != -1:
            # Obtener el ID del producto de la columna 0 (primera columna)
            id_producto = self.table_widget.item(selected_row, 0).text()

            # Realizar una consulta a la base de datos para obtener información detallada del producto
            cursor = self.__conection.cursor()
            sql = "SELECT * FROM inventario WHERE id_producto = %s"
            cursor.execute(sql, (id_producto,))
            producto_info = cursor.fetchone()

            # Mostrar la información del producto en un cuadro de diálogo
            if producto_info:
                informacion = f"ID Producto: {producto_info[0]}\n"
                informacion += f"Nombre Producto: {producto_info[1]}\n"
                informacion += f"Precio unitario: \n"
                informacion += f"Precio de inventario: \n"
                #informacion += f"Unidad: {producto_info[2]}\n"
                informacion += f"Cantidad: {producto_info[3]}\n"
                #informacion += f"Estado: {producto_info[4]}"
                QMessageBox.information(self, 'Información del Producto', informacion)
            else:
                QMessageBox.warning(self, 'Advertencia', 'No se encontró información para el producto seleccionado.')
        else:
            QMessageBox.warning(self, 'Advertencia', 'Por favor selecciona un producto de la tabla.')

    def exportar_datos(self):
        # Obtener la ruta de archivo seleccionada por el usuario
        file_path, _ = QFileDialog.getSaveFileName(self, 'Guardar como', '', 'Archivos de texto (*.txt)')

        if file_path:
            # Abrir el archivo en modo escritura
            with open(file_path, 'w') as file:
                # Iterar sobre las filas y columnas de la tabla para escribir los datos en el archivo
                for row in range(self.table_widget.rowCount()):
                    row_data = []
                    for column in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    file.write('\t'.join(row_data) + '\n')

                # Agregar la fecha y hora de la exportación al final del archivo
                export_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f'\nFecha y hora de exportación: {export_date_time}\n')

        QMessageBox.information(self, 'Exportar', 'Los datos han sido exportados correctamente.')

    def actualizar_datos(self):
        # Simplemente volvemos a cargar los datos
        self.cargar_datos()
        # Mostramos el mensaje de datos actualizados
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))

    def toggle_bloqueo(self):
        if self.botones_habilitados:
            # Pedir contraseña para bloquear
            contraseña, ok = QInputDialog.getText(self, 'Contraseña', 'Ingrese la contraseña para bloquear:')

            # Verificar si la contraseña es correcta
            if ok and contraseña == self.contraseña_bloqueo:
                self.botones_habilitados = False
                # Deshabilitar botones y caja de texto
                self.buscar_button.setEnabled(False)
                self.informacion_button.setEnabled(False)
                self.actualizar_button.setEnabled(False)
                self.exportar_button.setEnabled(False)
                self.id_producto_edit.setEnabled(False)
                self.candado_button.setText('🔓')
            else:
                QMessageBox.warning(self, 'Advertencia', 'Contraseña incorrecta.')
        else:
            # Pedir contraseña para desbloquear
            contraseña, ok = QInputDialog.getText(self, 'Contraseña', 'Ingrese la contraseña para desbloquear:')

            # Verificar si la contraseña es correcta
            if ok and contraseña == self.contraseña_desbloqueo:
                self.botones_habilitados = True
                # Habilitar botones y caja de texto
                self.buscar_button.setEnabled(True)
                self.informacion_button.setEnabled(True)
                self.actualizar_button.setEnabled(True)
                self.exportar_button.setEnabled(True)
                self.id_producto_edit.setEnabled(True)
                self.candado_button.setText('🔒')
            else:
                QMessageBox.warning(self, 'Advertencia', 'Contraseña incorrecta.')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Inventario()
    ventana.show()
    app.exec_()
