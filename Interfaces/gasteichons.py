from PyQt5 import QtCore, QtWidgets, QtGui
import mysql.connector

class RegistroGastos(QtWidgets.QMainWindow):
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
        self.setWindowTitle('Registro de Gastos | Empleados')
        self.resize(800, 600)
        self.setWindowIcon(QtGui.QIcon('icono_de_tu_aplicacion.ico'))

        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['Título', 'Descripción', 'Monto', 'Fecha', 'Empleado'])
        self.table_widget.setStyleSheet("background-color: white;")

        self.titulo_edit = QtWidgets.QLineEdit()
        self.descripcion_edit = QtWidgets.QLineEdit()
        self.monto_edit = QtWidgets.QLineEdit()
        self.fecha_edit = QtWidgets.QDateEdit()
        self.fecha_edit.setCalendarPopup(True)
        self.fecha_edit.setDate(QtCore.QDate.currentDate())
        self.empleado_combo = QtWidgets.QComboBox()

        # Agregar el primer elemento como "Seleccione un Empleado"
        self.empleado_combo.addItem("")

        self.cargarEmpleados()

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('Título:', self.titulo_edit)
        form_layout.addRow('Descripción:', self.descripcion_edit)
        form_layout.addRow('Monto:', self.monto_edit)
        form_layout.addRow('Fecha:', self.fecha_edit)
        form_layout.addRow('Empleado:', self.empleado_combo)

        form_widget = QtWidgets.QWidget()
        form_widget.setLayout(form_layout)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(form_widget)
        scroll_area.setWidgetResizable(True)

        self.agregar_button = QtWidgets.QPushButton('Agregar Gasto')
        self.agregar_button.setStyleSheet("background-color: #AFEEEE;")
        self.agregar_button.clicked.connect(self.agregar_gasto)

        self.enviar_button = QtWidgets.QPushButton('Enviar Gastos')
        self.enviar_button.setStyleSheet("background-color: #90EE90;")
        self.enviar_button.clicked.connect(self.enviar_gastos)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.agregar_button)
        button_layout.addWidget(self.enviar_button)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def agregar_gasto(self):
        titulo, descripcion, monto, fecha, id_empleado = self.get_datos()

        # Lista para almacenar mensajes de error
        error_messages = []

        # Verificar campos vacíos y agregar mensajes de error
        if not titulo.strip():
            error_messages.append("Campo obligatorio: Título")
            self.show_error_message(self.titulo_edit, "Campo obligatorio")
        if not monto.strip():
            error_messages.append("Campo obligatorio: Monto")
            self.show_error_message(self.monto_edit, "Campo obligatorio")

        # Mostrar mensaje general si hay campos vacíos
        if error_messages:
            QtWidgets.QMessageBox.warning(self, 'Campos Vacíos', '\n'.join(error_messages))
            return

        # Limpiar mensajes de error si los campos están llenos
        self.clear_error_messages()

        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titulo))
        self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(descripcion))
        self.table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(monto))
        self.table_widget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(fecha))
        self.table_widget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(id_empleado))

        # Limpiar campos después de agregar a la tabla
        self.titulo_edit.clear()
        self.descripcion_edit.clear()
        self.monto_edit.clear()
        self.fecha_edit.setDate(QtCore.QDate.currentDate())
        self.empleado_combo.setCurrentIndex(0)

    def enviar_gastos(self):
        for row in range(self.table_widget.rowCount()):
            titulo = self.table_widget.item(row, 0).text()
            descripcion = self.table_widget.item(row, 1).text()
            monto = self.table_widget.item(row, 2).text()
            fecha = self.table_widget.item(row, 3).text()
            id_empleado = self.table_widget.item(row, 4).text()

            query = "INSERT INTO gasto (titulo, descripcion, monto, fecha, id_empleado) VALUES (%s, %s, %s, %s, %s)"
            values = (titulo, descripcion, monto, fecha, id_empleado)

            cursor = self.__conection.cursor()
            try:
                cursor.execute(query, values)
                self.__conection.commit()
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, 'Error', f"Error al agregar gasto: {err}")
            finally:
                cursor.close()

        self.table_widget.setRowCount(0)

    def cargarEmpleados(self):
        cursor = self.__conection.cursor()
        cursor.execute("SELECT id_empleado, nombre FROM empleado WHERE activo = 'V'")
        empleados = cursor.fetchall()
        
        # Creamos un diccionario para mapear nombre -> id_empleado
        self.empleados_dict = {}
        
        for id_empleado, nombre in empleados:
            self.empleados_dict[nombre] = id_empleado
            self.empleado_combo.addItem(f"{nombre} - {id_empleado}")

        cursor.close()

    def get_datos(self):
        titulo = self.titulo_edit.text()
        descripcion = self.descripcion_edit.text()
        monto = self.monto_edit.text()
        fecha = self.fecha_edit.date().toString("yyyy-MM-dd")
        
        # Obtenemos el valor seleccionado (nombre - id_empleado)
        nombre_id_empleado = self.empleado_combo.currentText()
        
        # Separamos el nombre del id_empleado
        nombre, id_empleado = nombre_id_empleado.split(' - ')
        
        return titulo, descripcion, monto, fecha, id_empleado

    def show_error_message(self, widget, message):
        error_label = QtWidgets.QLabel(message)
        error_label.setStyleSheet("color: red;")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(error_label)
        widget.setLayout(layout)

    def clear_error_messages(self):
        self.titulo_edit.setStyleSheet("")
        self.monto_edit.setStyleSheet("")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = RegistroGastos()
    main_window.show()
    app.exec_()
