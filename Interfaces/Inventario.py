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
        self.buscar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")  # Establecer color de fondo, texto y negrita

        # Conectar señal y slot
        self.buscar_button.clicked.connect(self.buscar_id)

        # Crear cuadro de texto para ingresar ID
        self.id_producto_edit = QLineEdit()

        # Crear label para el texto "Buscar ID"
        buscar_label = QLabel("Buscar ID:")

        # Crear layout horizontal para el cuadro de texto, el label y el botón de búsqueda
        search_layout = QHBoxLayout()
        search_layout.addWidget(buscar_label)
        search_layout.addWidget(self.id_producto_edit)
        search_layout.addWidget(self.buscar_button)

        # Crear botón de actualización
        self.actualizar_button = QPushButton('Actualizar')
        self.actualizar_button.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")  # Establecer color de fondo, texto y negrita

        # Conectar señal y slot
        self.actualizar_button.clicked.connect(self.actualizar_datos)

        # Crear layout para los botones
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.actualizar_button)

        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Cargar datos
        self.cargar_datos()

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
        id_producto_texto = self.id_producto_edit.text()

        # Verificar si el campo de búsqueda está vacío
        if not id_producto_texto:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, ingresa un ID antes de realizar la búsqueda.')
            return

        try:
            id_producto = int(id_producto_texto)
        except ValueError:
            QMessageBox.warning(self, 'Advertencia', 'El formato del ID no es válido. Por favor, ingresa un número entero.')
            self.id_producto_edit.clear()
            return

        # Ahora, id_producto es un número entero válido
        if id_producto:
            # Itera sobre las filas y compara el ID en la primera columna
            for row in range(self.table_widget.rowCount()):
                item = self.table_widget.item(row, 0)  # Suponiendo que el ID esté en la primera columna
                if item.text() == str(id_producto):
                    self.table_widget.selectRow(row)
                    self.table_widget.verticalScrollBar().setValue(row)
                    return
            QMessageBox.warning(self, 'Advertencia', 'El ID no se encuentra en la base de datos.')

        self.id_producto_edit.clear()

    def actualizar_datos(self):
        # Simplemente volvemos a cargar los datos
        self.cargar_datos()
        # Mostramos el mensaje de datos actualizados
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))


if __name__ == '__main__':
    app = QApplication([])
    ventana = Inventario()
    ventana.show()
    app.exec_()
