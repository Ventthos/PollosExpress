from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
import datetime
import re

class Admin_Gastos(QMainWindow):
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
        self.cargar_datos()

    def initUI(self):
        self.setWindowTitle('Pollos Express | Gastos (Administrador)')
        self.resize(1200, 700)
        self.setWindowIcon(QIcon('../img/logo.ico'))

        # Crear widgets
        self.titulo_label = QLabel('Título:')
        self.titulo_edit = QLineEdit()  

        self.descripcion_label = QLabel('Descripción:')
        self.descripcion_edit = QLineEdit()
        self.monto_label = QLabel('Monto ($):')
        self.monto_edit = QLineEdit()
        
        # Crear el campo de fecha y hora
        self.fecha_label = QLabel('Fecha:')
        self.fecha_edit = QDateTimeEdit()
        self.fecha_edit.setDateTime(QDateTime.currentDateTime())  # Establecer la fecha y hora actuales
        self.fecha_edit.setDisplayFormat("yyyy-MM-dd HH:mm")  # Formato de visualización

        # Botón para establecer la fecha y hora actuales
        self.actual_button = QPushButton('Actual')
        self.actual_button.setFixedWidth(120)  # Ajustar el ancho del botón
        self.actual_button.clicked.connect(self.establecer_fecha_actual)

        self.id_empleado_label = QLabel('ID Empleado:')
        self.id_empleado_edit = QLineEdit()

        # Botón para guardar el gasto
        self.guardar_button = QPushButton('Guardar')
        self.guardar_button.clicked.connect(self.guardar_gasto)
        self.guardar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")

        # Botón para editar el gasto seleccionado
        self.editar_button = QPushButton('Editar')
        self.editar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.editar_button.clicked.connect(self.editar_gasto)
        
        # Botón para eliminar el gasto seleccionado
        self.eliminar_button = QPushButton('Eliminar')
        self.eliminar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.eliminar_button.clicked.connect(self.eliminar_gasto)
        
        # Botón para actualizar los datos
        self.actualizar_button = QPushButton('Actualizar')
        self.actualizar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.actualizar_button.clicked.connect(self.actualizar_lista)
        
        # Barra de búsqueda
        self.busqueda_edit = QLineEdit()
        self.busqueda_edit.setPlaceholderText('Buscar por ID, fecha o nombre')
        self.busqueda_edit.textChanged.connect(self.filtrar_datos)
        
        # Crear el diseño del formulario
        form_layout = QFormLayout()
        form_layout.addRow(self.titulo_label, self.titulo_edit)
        form_layout.addRow(self.descripcion_label, self.descripcion_edit)
        form_layout.addRow(self.monto_label, self.monto_edit)
        
        # Crear un layout horizontal para la fecha y el botón "Actual"
        fecha_layout = QHBoxLayout()
        fecha_layout.addWidget(self.fecha_edit)
        fecha_layout.addWidget(self.actual_button)

        form_layout.addRow(self.fecha_label, fecha_layout)
        form_layout.addRow(self.id_empleado_label, self.id_empleado_edit)
        form_layout.addRow(self.guardar_button)
        form_layout.addRow(self.editar_button)
        form_layout.addRow(self.eliminar_button)
        
        # Crear un diseño horizontal para la barra de búsqueda y el botón de actualización
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.busqueda_edit)
        search_layout.addWidget(self.actualizar_button)
        
        # Agregar el diseño horizontal al diseño del formulario
        form_layout.addRow(search_layout)

        # Crear el widget de la tabla
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Título','Descripción', 'Monto ($)', 'Fecha', 'ID Empleado'])

        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.table)

        # Crear widget central y establecer el diseño
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Conectar la señal itemClicked del QTableWidget a la función cargar_datos_seleccionados
        self.table.itemClicked.connect(self.cargar_datos_seleccionados)

    def cargar_datos(self):
        cursor = self.__connection.cursor()
        query = "SELECT id_gasto, titulo, descripcion, monto, fecha, id_empleado FROM gasto ORDER BY id_gasto ASC"
        cursor.execute(query)
        datos = cursor.fetchall()
        cursor.close()

        # Limpiar la tabla antes de cargar los nuevos datos
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(datos):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row_number, column_number, item)

        # Configurar manualmente el ancho de las columnas
        self.table.setColumnWidth(0, 175)  # ID
        self.table.setColumnWidth(1, 200)  # Título
        self.table.setColumnWidth(2, 200)  # Descripción
        self.table.setColumnWidth(3, 190)  # Monto
        self.table.setColumnWidth(4, 200)  # Fecha
        self.table.setColumnWidth(5, 190)  # ID Empleado
        
    def guardar_gasto(self):
        # Obtener los valores de los campos
        titulo = self.titulo_edit.text().strip()
        descripcion = self.descripcion_edit.text().strip()
        monto = self.monto_edit.text().strip()
        fecha = self.fecha_edit.dateTime().toString("yyyy-MM-dd hh:mm")
        id_empleado = self.id_empleado_edit.text().strip()

        # Verificar si algún campo está vacío
        if not titulo or not descripcion or not monto or not id_empleado:
            QMessageBox.warning(self, 'Advertencia', 'Todos los campos son obligatorios.')
            return

        # Validación del Monto ($)
        monto_valido = re.match(r'^\d+(\.\d+)?$', monto)
        if not monto_valido:
            QMessageBox.warning(self, 'Advertencia', 'El monto ingresado no es válido. Por favor, ingresa un valor numérico.')
            return

        # Validación del ID Empleado
        id_empleado_valido = re.match(r'^\d+$', id_empleado)
        if not id_empleado_valido:
            QMessageBox.warning(self, 'Advertencia', 'El ID de empleado ingresado no es válido. Por favor, ingresa un valor numérico entero.')
            return

        # Insertar los datos en la base de datos
        cursor = self.__connection.cursor()
        query = "INSERT INTO gasto (titulo, descripcion, monto, fecha, id_empleado) VALUES (%s, %s, %s, %s, %s)"
        values = (titulo, descripcion, monto, fecha, id_empleado)
        cursor.execute(query, values)
        self.__connection.commit()
        cursor.close()

        # Limpiar los campos después de guardar
        self.titulo_edit.clear()
        self.descripcion_edit.clear()
        self.monto_edit.clear()
        self.fecha_edit.setDateTime(QDateTime.currentDateTime())  # Establecer la fecha y hora actuales
        self.id_empleado_edit.clear()

        # Recargar los datos en la tabla
        self.cargar_datos()

        QMessageBox.information(self, 'Éxito', 'Gasto guardado exitosamente.')

    def filtrar_datos(self):
        filtro = self.busqueda_edit.text()

        # Realizar la consulta con el filtro
        cursor = self.__connection.cursor()
        query = "SELECT id_gasto, titulo, descripcion, monto, fecha, id_empleado FROM gasto WHERE id_gasto LIKE %s OR fecha LIKE %s OR titulo LIKE %s ORDER BY id_gasto ASC"
        cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
        datos = cursor.fetchall()
        cursor.close()

        # Limpiar la tabla antes de cargar los nuevos datos
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(datos):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row_number, column_number, item)

        # Configurar manualmente el ancho de las columnas
        self.table.setColumnWidth(0, 175)  # ID
        self.table.setColumnWidth(1, 200)  # Título
        self.table.setColumnWidth(2, 200)  # Descripción
        self.table.setColumnWidth(3, 190)  # Monto
        self.table.setColumnWidth(4, 200)  # Fecha
        self.table.setColumnWidth(5, 190)  # ID Empleado

    def cargar_datos_seleccionados(self, item):
        # Obtener el índice de la fila seleccionada
        row_index = item.row()

        # Obtener los datos de la fila seleccionada
        id_gasto = self.table.item(row_index, 0).text()
        titulo = self.table.item(row_index, 1).text()
        descripcion = self.table.item(row_index, 2).text()
        monto = self.table.item(row_index, 3).text()
        fecha = self.table.item(row_index, 4).text()
        id_empleado = self.table.item(row_index, 5).text()

        # Mostrar los datos en los campos de texto
        self.titulo_edit.setText(titulo)
        self.descripcion_edit.setText(descripcion)
        self.monto_edit.setText(monto)
        # Convertir la fecha al formato correcto para el QDateTimeEdit
        fecha_datetime = QDateTime.fromString(fecha, "yyyy-MM-dd hh:mm:ss")
        self.fecha_edit.setDateTime(fecha_datetime)
        self.id_empleado_edit.setText(id_empleado)

    def editar_gasto(self):
        # Obtener el índice de la fila seleccionada
        fila_seleccionada = self.table.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, 'Advertencia', 'Selecciona un gasto para editar.')
            return

        # Obtener los nuevos valores de los campos de texto
        titulo = self.titulo_edit.text().strip()
        descripcion = self.descripcion_edit.text().strip()
        monto = self.monto_edit.text().strip()
        fecha = self.fecha_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        id_empleado = self.id_empleado_edit.text().strip()

        # Verificar si algún campo está vacío
        if not titulo or not descripcion or not monto or not id_empleado:
            QMessageBox.warning(self, 'Advertencia', 'Todos los campos son obligatorios.')
            return

        # Validación del Monto ($)
        monto_valido = re.match(r'^\d+(\.\d+)?$', monto)
        if not monto_valido:
            QMessageBox.warning(self, 'Advertencia', 'El monto ingresado no es válido. Por favor, ingresa un valor numérico.')
            return

        # Validación del ID Empleado
        id_empleado_valido = re.match(r'^\d+$', id_empleado)
        if not id_empleado_valido:
            QMessageBox.warning(self, 'Advertencia', 'El ID de empleado ingresado no es válido. Por favor, ingresa un valor numérico entero.')
            return

        # Obtener el ID del gasto seleccionado
        id_gasto = self.table.item(fila_seleccionada, 0).text()

        # Actualizar los datos en la base de datos
        cursor = self.__connection.cursor()
        query = "UPDATE gasto SET titulo = %s, descripcion = %s, monto = %s, fecha = %s, id_empleado = %s WHERE id_gasto = %s"
        values = (titulo, descripcion, monto, fecha, id_empleado, id_gasto)
        cursor.execute(query, values)
        self.__connection.commit()
        cursor.close()

        # Recargar los datos en la tabla
        self.cargar_datos()

        QMessageBox.information(self, 'Éxito', 'Gasto actualizado exitosamente.')

    def eliminar_gasto(self):
        # Obtener el índice de la fila seleccionada
        fila_seleccionada = self.table.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, 'Advertencia', 'Selecciona un gasto para eliminar.')
            return

        # Obtener el ID del gasto seleccionado
        id_gasto = self.table.item(fila_seleccionada, 0).text()

        # Confirmar la eliminación
        respuesta = QMessageBox.question(self, 'Eliminar Gasto', f'¿Estás seguro de eliminar el gasto con ID {id_gasto}?', QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            # Eliminar el gasto de la base de datos
            cursor = self.__connection.cursor()
            query = "DELETE FROM gasto WHERE id_gasto = %s"
            cursor.execute(query, (id_gasto,))
            self.__connection.commit()
            cursor.close()

            # Recargar los datos en la tabla
            self.cargar_datos()

            QMessageBox.information(self, 'Éxito', 'Gasto eliminado exitosamente.')

    def actualizar_lista(self):
        # Cargamos los datos nuevamente
        self.cargar_datos()
        # Mensaje de los datos actualizados
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))
        # Limpiamos la barra de búsqueda
        self.busqueda_edit.clear()

    def establecer_fecha_actual(self):
        self.fecha_edit.setDateTime(QDateTime.currentDateTime())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana = Admin_Gastos()
    ventana.show()
    sys.exit(app.exec_())
