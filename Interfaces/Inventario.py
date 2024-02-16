from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QScrollArea, QHBoxLayout, QMessageBox, QDialog, QFormLayout
from PyQt5 import QtCore
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
        self.setWindowTitle('Inventario')
        self.resize(1200, 700)  # Tamaño más pequeño para la ventana

        # Crear tabla y área de desplazamiento
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['ID Producto', 'Nombre Producto', 'Unidad', 'Cantidad'])

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

        # Crear botón de actualización
        self.actualizar_button = QPushButton('Actualizar')
        self.actualizar_button.setStyleSheet("background-color: #AFEEEE;")  # Establecer color de fondo

        # Conectar señal y slot
        self.actualizar_button.clicked.connect(self.actualizar_datos)

        # Crear botón de candado
        self.candado_button = QPushButton('🔒')

        # Conectar señal y slot
        self.candado_button.clicked.connect(self.toggle_botones)

        # Crear cuadro de texto para ingresar ID
        self.id_producto_edit = QLineEdit()

        # Crear layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buscar_button)
        button_layout.addWidget(self.actualizar_button)
        button_layout.addWidget(self.candado_button)

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

    def toggle_botones(self):
        # Cambiar el estado habilitado/deshabilitado de los botones
        self.botones_habilitados = not self.botones_habilitados
        self.buscar_button.setEnabled(self.botones_habilitados)
        self.actualizar_button.setEnabled(self.botones_habilitados)
        
        # También deshabilitar el cuadro para buscar ID
        self.id_producto_edit.setEnabled(self.botones_habilitados)


    def cargar_datos(self):
        cursor = self.__conection.cursor()
        sql = "SELECT inventario.id_producto, inventario.nombre_producto, inventario.unidad, inventario.cantidad FROM inventario INNER JOIN producto on producto.id_producto = inventario.id_producto WHERE producto.activo = 'V'"
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Limpiar la tabla antes de cargar nuevos datos
        self.table_widget.setRowCount(0)

        for row_number, row_data in enumerate(rows):
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def buscar_id(self):
        id_producto = self.id_producto_edit.text()
        if id_producto:
            items = self.table_widget.findItems(id_producto, QtCore.Qt.MatchExactly)
            if items:
                for item in items:
                    item.setSelected(True)
                    row = item.row()
                    self.table_widget.verticalScrollBar().setValue(row)
            else:
                QMessageBox.warning(self, 'Advertencia', 'El ID no se encuentra en la tabla.')

    def actualizar_datos(self):
        # Simplemente volvemos a cargar los datos
        self.cargar_datos()
        # Mostramos el mensaje de datos actualizados
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    app = QApplication([])
    ventana = Inventario()
    ventana.show()
    app.exec_()
