from PyQt5 import QtCore, QtWidgets, QtGui
import mysql.connector
import datetime

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

        # Establecer ícono de la ventana
        self.setWindowIcon(QtGui.QIcon('icono_de_tu_aplicacion.ico'))

        # Crear tabla y área de desplazamiento
        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['titulo', 'descripcion', 'monto', 'fecha', 'id_empleado'])

        # Establecer color de fondo de la tabla
        self.table_widget.setStyleSheet("background-color: white;")

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(self.table_widget)
        scroll_area.setWidgetResizable(True)

        # Crear botón para agregar gasto
        self.agregar_button = QtWidgets.QPushButton('Agregar Gasto')
        self.agregar_button.setStyleSheet("background-color: #AFEEEE;")

        # Conectar señal y slot
        self.agregar_button.clicked.connect(self.agregar_gasto)

        # Crear botón para enviar gastos
        self.enviar_button = QtWidgets.QPushButton('Enviar Gastos')
        self.enviar_button.setStyleSheet("background-color: #90EE90;")

        # Conectar señal y slot
        self.enviar_button.clicked.connect(self.enviar_gastos)

        # Crear layout para los botones
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.agregar_button)
        button_layout.addWidget(self.enviar_button)

        # Crear layout principal
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def agregar_gasto(self):
        # Abrir diálogo para ingresar nuevo gasto
        dialog = NuevoGastoDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            titulo, descripcion, monto, fecha, id_empleado = dialog.get_datos()
            if titulo.strip() == '' or monto.strip() == '' or id_empleado.strip() == '':
                QtWidgets.QMessageBox.warning(self, 'Campos Vacíos', 'Por favor, complete todos los campos antes de agregar el gasto.')
                return
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titulo))
            self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(descripcion))
            self.table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(monto))
            self.table_widget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(fecha))
            self.table_widget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(id_empleado))

    def enviar_gastos(self):
        # Recorrer la tabla y enviar cada gasto a la base de datos
        for row in range(self.table_widget.rowCount()):
            titulo = self.table_widget.item(row, 0).text()
            descripcion = self.table_widget.item(row, 1).text()
            monto = self.table_widget.item(row, 2).text()
            fecha = self.table_widget.item(row, 3).text()
            id_empleado = self.table_widget.item(row, 4).text()

            # Crear la consulta SQL para insertar el gasto
            query = "INSERT INTO gasto (titulo, descripcion, monto, fecha, id_empleado) VALUES (%s, %s, %s, %s, %s)"
            values = (titulo, descripcion, monto, fecha, id_empleado)

            # Ejecutar la consulta
            cursor = self.__conection.cursor()
            try:
                cursor.execute(query, values)
                self.__conection.commit()
            except mysql.connector.Error as err:
                print(f"Error al agregar gasto: {err}")
            finally:
                cursor.close()

        # Limpiar la tabla después de enviar los gastos
        self.table_widget.setRowCount(0)

# Clase para el diálogo de nuevo gasto
class NuevoGastoDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Nuevo Gasto')
        self.setFixedSize(300, 200)

        # Crear campos de entrada para nuevo gasto
        self.titulo_edit = QtWidgets.QLineEdit()
        self.descripcion_edit = QtWidgets.QLineEdit()
        self.monto_edit = QtWidgets.QLineEdit()
        self.fecha_edit = QtWidgets.QDateEdit()
        self.fecha_edit.setCalendarPopup(True)
        self.fecha_edit.setDate(QtCore.QDate.currentDate())
        self.id_empleado_edit = QtWidgets.QLineEdit()

        # Crear layout para los campos de entrada
        layout = QtWidgets.QFormLayout()
        layout.addRow('Título:', self.titulo_edit)
        layout.addRow('Descripción:', self.descripcion_edit)
        layout.addRow('Monto:', self.monto_edit)
        layout.addRow('Fecha:', self.fecha_edit)
        layout.addRow('ID Empleado:', self.id_empleado_edit)

        # Crear botones de aceptar y cancelar
        self.buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        # Agregar botones al layout
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_datos(self):
        # Obtener los valores de los campos de entrada
        titulo = self.titulo_edit.text()
        descripcion = self.descripcion_edit.text()
        monto = self.monto_edit.text()
        fecha = self.fecha_edit.date().toString("yyyy-MM-dd")
        id_empleado = self.id_empleado_edit.text()
        return titulo, descripcion, monto, fecha, id_empleado

# Resto del código necesario para iniciar la aplicación
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = RegistroGastos()
    main_window.show()
    app.exec_()
