from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import mysql.connector
import datetime

class Admin_Inventario(QMainWindow):
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
        self.setWindowTitle('Pollos Express | Inventario (Administrador)')
        self.resize(1200, 700)
        self.setWindowIcon(QIcon('../img/logo.ico'))

        # Definir widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Layout para la lista de productos
        self.lista_layout = QVBoxLayout()
        self.lista_layout.setSpacing(10)
        self.main_layout.addLayout(self.lista_layout)

        # Cuadro de búsqueda y botones
        self.layout_buscar = QHBoxLayout()
        self.lista_layout.addLayout(self.layout_buscar)

        self.label_buscar = QLabel('Buscar en Inventario:')
        self.layout_buscar.addWidget(self.label_buscar)

        self.input_buscar = QLineEdit()
        self.layout_buscar.addWidget(self.input_buscar)

        self.btn_buscar = QPushButton('Buscar')
        self.btn_buscar.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.btn_buscar.clicked.connect(self.buscar_producto)
        self.layout_buscar.addWidget(self.btn_buscar)

        self.btn_actualizar = QPushButton('Actualizar')
        self.btn_actualizar.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.btn_actualizar.clicked.connect(self.actualizar_lista)
        self.layout_buscar.addWidget(self.btn_actualizar)

        # Data Grid para los productos
        self.table_widget = QTableWidget()
        self.lista_layout.addWidget(self.table_widget)

        # Configuración del Data Grid
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Nombre'])

        # Layout para los campos de entrada y botón
        self.input_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_layout)
        self.label_id = QLabel('ID del Producto:')
        self.input_id = QLineEdit()
        self.input_layout.addWidget(self.label_id)
        self.input_layout.addWidget(self.input_id)

        self.label_nombre = QLabel('Nombre del Producto:')
        self.input_nombre = QLineEdit()
        self.input_layout.addWidget(self.label_nombre)
        self.input_layout.addWidget(self.input_nombre)

        self.label_unidad = QLabel('Unidad:')
        self.input_unidad = QLineEdit()
        self.input_unidad.setText('--')
        self.input_layout.addWidget(self.label_unidad)
        self.input_layout.addWidget(self.input_unidad)

        self.label_cantidad = QLabel('Cantidad:')
        self.input_cantidad = QLineEdit()
        self.input_cantidad.setText("0")
        self.input_layout.addWidget(self.label_cantidad)
        self.input_layout.addWidget(self.input_cantidad)

        # Label y Checkbox para Estado
        self.label_estado = QLabel('Activo:')
        self.input_layout.addWidget(self.label_estado)
        self.checkbox_estado = QCheckBox()
        self.input_layout.addWidget(self.checkbox_estado)

        # Agregar un espacio entre los botones de editar y guardar
        self.input_layout.addSpacing(10)

        # Agregar botón de editar a la izquierda del botón de guardar
        self.btn_editar = QPushButton('Editar')
        self.btn_editar.clicked.connect(self.editar_producto)
        self.btn_editar.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.input_layout.addWidget(self.btn_editar)

        self.btn_guardar = QPushButton('Guardar')
        self.btn_guardar.clicked.connect(self.guardar_datos)
        self.btn_guardar.setStyleSheet("background-color: #F08080; color: white; font-weight: bold;")
        self.input_layout.addWidget(self.btn_guardar)

        # Botón para eliminar producto
        self.btn_eliminar = QPushButton('Eliminar')
        self.btn_eliminar.setStyleSheet("background-color: #c9636c; color: white; font-weight: bold;")
        self.btn_eliminar.clicked.connect(self.eliminar_producto)
        self.input_layout.addWidget(self.btn_eliminar)

        # Cargar lista de productos al inicio
        self.cargar_inventario()

        # Conectar la señal cellClicked a la función cargar_datos_celda_seleccionada
        self.table_widget.cellClicked.connect(self.cargar_datos_celda_seleccionada_inventario)

        # Agregar un nuevo DataGrid para la tabla "producto"
        self.table_widget_producto = QTableWidget()
        self.lista_layout.addWidget(self.table_widget_producto)

        # Configurar el nuevo DataGrid
        self.table_widget_producto.setColumnCount(4)
        self.table_widget_producto.setHorizontalHeaderLabels(['ID', 'Nombre', 'Precio', 'Activo'])

        # Conectar la señal cellClicked a la función cargar_datos_celda_seleccionada
        self.table_widget_producto.cellClicked.connect(self.cargar_datos_celda_seleccionada_producto)

        # Cargar y mostrar los datos de la tabla "producto"
        self.cargar_productos()

    def cargar_inventario(self):
        cursor = self.__conection.cursor()
        query = "SELECT id_producto, nombre_producto FROM inventario"
        cursor.execute(query)
        productos = cursor.fetchall()

        if not productos:
            QMessageBox.information(self, 'Información', 'No hay registros en la base de datos.')
            return

        self.table_widget.setRowCount(len(productos))

        for row, producto in enumerate(productos):
            id_producto_item = QTableWidgetItem(str(producto[0]))
            nombre_producto_item = QTableWidgetItem(producto[1])
            self.table_widget.setItem(row, 0, id_producto_item)
            self.table_widget.setItem(row, 1, nombre_producto_item)

        cursor.close()

        # Centrar datos en la tabla
        for row in range(self.table_widget.rowCount()):
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

    def cargar_productos(self):
        cursor = self.__conection.cursor()
        query = "SELECT id_producto, nombre, precio, activo FROM producto"
        cursor.execute(query)
        productos = cursor.fetchall()

        if not productos:
            QMessageBox.information(self, 'Información', 'No hay registros en la tabla "producto".')

        self.table_widget_producto.setRowCount(len(productos))

        for row, producto in enumerate(productos):
            for col, data in enumerate(producto):
                item = QTableWidgetItem(str(data))
                self.table_widget_producto.setItem(row, col, item)

        # Ajustar manualmente el ancho de las columnas
        self.table_widget_producto.setColumnWidth(0, 130)  # ID
        self.table_widget_producto.setColumnWidth(1, 134)  # Nombre
        self.table_widget_producto.setColumnWidth(2, 134)  # Precio
        self.table_widget_producto.setColumnWidth(3, 134)  # Activo

        cursor.close()

        # Centrar datos en la tabla
        for row in range(self.table_widget_producto.rowCount()):
            for column in range(self.table_widget_producto.columnCount()):
                item = self.table_widget_producto.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

    def guardar_datos(self):
        # Obtener los datos de los campos de entrada
        id_producto = self.input_id.text()
        nombre_producto = self.input_nombre.text()
        unidad = self.input_unidad.text()
        cantidad = self.input_cantidad.text()
        # Obtener el estado del checkbox
        estado = '1' if self.checkbox_estado.isChecked() else '0'

        # Verificar si alguno de los campos está vacío
        if not id_producto or not nombre_producto or not unidad or not cantidad:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete todos los campos para guardar el producto.')
            return

        # Verificar si el producto ya existe en la base de datos
        if self.producto_existe(id_producto):
            QMessageBox.warning(self, 'Advertencia', f'El producto con ID {id_producto} ya existe en la base de datos.')
            return

        # Insertar los datos en la base de datos
        cursor = self.__conection.cursor()
        query = "INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (%s, %s, %s, %s, %s)"
        data = (id_producto, nombre_producto, unidad, cantidad, estado)
        cursor.execute(query, data)
        self.__conection.commit()
        cursor.close()

        # Limpiar los campos de entrada después de guardar
        self.input_id.clear()
        self.input_nombre.clear()
        self.input_unidad.setText("--")
        self.input_cantidad.setText("0")
        self.checkbox_estado.setChecked(False)

        # Actualizar la lista de productos después de guardar
        QMessageBox.information(self, 'Información', 'El producto ha sido guardado correctamente.')
        self.actualizar_lista()

    def eliminar_producto(self):
        # Obtener el ID del producto a eliminar
        id_producto = self.input_id.text()

        # Verificar si se proporcionó un ID de producto
        if not id_producto:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, ingrese el ID del producto a eliminar.')
            return

        # Verificar si el ID del producto existe en la tabla de inventario
        cursor = self.__conection.cursor()
        query = "SELECT id_producto FROM inventario WHERE id_producto = %s"
        cursor.execute(query, (id_producto,))
        producto_existente = cursor.fetchone()
        cursor.close()

        if not producto_existente:
            QMessageBox.warning(self, 'Advertencia', f'El ID del producto {id_producto} no se encuentra en el inventario.')
            return

        # Confirmar si el usuario realmente desea eliminar el producto
        confirmacion = QMessageBox.question(self, 'Confirmar Eliminación', 
                                            f'¿Está seguro de que desea eliminar el producto con ID {id_producto}?',
                                            QMessageBox.Yes | QMessageBox.No)

        if confirmacion == QMessageBox.Yes:
            # Eliminar el producto de la base de datos
            cursor = self.__conection.cursor()
            query = "DELETE FROM inventario WHERE id_producto = %s"
            cursor.execute(query, (id_producto,))
            self.__conection.commit()
            cursor.close()

            # Limpiar los campos después de eliminar
            self.input_id.clear()
            self.input_nombre.clear()
            self.input_unidad.setText("--")
            self.input_cantidad.setText("0")
            self.checkbox_estado.setChecked(False)

            # Actualizar la lista de productos
            QMessageBox.information(self, 'Información', f'El producto con ID {id_producto} ha sido eliminado correctamente.')
            self.actualizar_lista()

        else:
            QMessageBox.information(self, 'Información', 'La eliminación ha sido cancelada.')

    def buscar_producto(self):
        # Obtener el texto del cuadro de búsqueda
        texto_busqueda = self.input_buscar.text().strip()  # Eliminar espacios al inicio y final del texto

        # Verificar si el campo de búsqueda está vacío
        if not texto_busqueda:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, ingrese un término para buscar.')
            return  # Salir del método sin hacer más acciones

        # Realizar la búsqueda en la base de datos
        cursor = self.__conection.cursor()
        query = "SELECT id_producto, nombre_producto FROM inventario WHERE nombre_producto LIKE %s"
        data = ("%" + texto_busqueda + "%",)
        cursor.execute(query, data)
        productos = cursor.fetchall()

        # Limpiar la tabla de productos
        self.table_widget.clearContents()

        # Si no se encontraron productos, mostrar una advertencia
        if not productos:
            QMessageBox.warning(self, 'Advertencia', 'El producto no se encuentra en la base de datos')
            self.input_buscar.clear()
        else:
            # Actualizar la tabla con los productos encontrados
            self.table_widget.setRowCount(len(productos))
            for row, producto in enumerate(productos):
                id_producto_item = QTableWidgetItem(str(producto[0]))
                nombre_producto_item = QTableWidgetItem(producto[1])
                self.table_widget.setItem(row, 0, id_producto_item)
                self.table_widget.setItem(row, 1, nombre_producto_item)

        # Centrar datos en la tabla
        for row in range(self.table_widget.rowCount()):
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

        cursor.close()

    def actualizar_lista(self):
        # Recargar la lista de productos para la primera tabla
        self.cargar_inventario()
        # Recargar la lista de productos para la segunda tabla
        self.cargar_productos()
        # Mensaje de los datos actualizados
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))
        # Limpiamos la barra de búsqueda
        self.input_buscar.clear()

    def editar_producto(self):
        # Obtener los datos de los campos de entrada
        id_producto = self.input_id.text()
        nombre_producto = self.input_nombre.text()
        unidad = self.input_unidad.text()
        cantidad = self.input_cantidad.text()
        # Obtener el estado del checkbox
        estado = '1' if self.checkbox_estado.isChecked() else '0'

        # Verificar si alguno de los campos está vacío
        if not id_producto or not nombre_producto or not unidad or not cantidad:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete todos los campos para editar el producto.')
            return

        # Verificar si el producto existe en la base de datos
        if not self.producto_existe(id_producto):
            QMessageBox.warning(self, 'Advertencia', f'El producto con ID {id_producto} no existe en el inventario.')
            return

        # Actualizar el registro en la base de datos
        cursor = self.__conection.cursor()
        query = "UPDATE inventario SET nombre_producto = %s, unidad = %s, cantidad = %s, estado = %s WHERE id_producto = %s"
        data = (nombre_producto, unidad, cantidad, estado, id_producto)
        cursor.execute(query, data)
        self.__conection.commit()
        cursor.close()

        # Limpiar los campos de entrada después de editar
        self.input_id.clear()
        self.input_nombre.clear()
        self.input_unidad.setText("--")
        self.input_cantidad.setText("0")
        self.checkbox_estado.setChecked(False)

        QMessageBox.information(self, 'Información', f'El producto con ID {id_producto} ha sido editado correctamente.')

    def producto_existe(self, id_producto):
        cursor = self.__conection.cursor()
        query = "SELECT id_producto FROM inventario WHERE id_producto = %s"
        cursor.execute(query, (id_producto,))
        producto = cursor.fetchone()
        cursor.close()
        return producto is not None

    def cargar_datos_celda_seleccionada_inventario(self, row, column):
        # Obtener los datos de la celda seleccionada
        id_producto = self.table_widget.item(row, 0).text()
        nombre_producto = self.table_widget.item(row, 1).text()

        # Buscar el índice de la fila seleccionada en la tabla de inventario
        index = self.table_widget.indexFromItem(self.table_widget.item(row, 0))

        # Colocar los datos en los cuadros de texto correspondientes
        self.input_id.setText(id_producto)
        self.input_nombre.setText(nombre_producto)

    def cargar_datos_celda_seleccionada_producto(self, row, column):
        # Obtener los datos de la celda seleccionada
        id_producto = self.table_widget_producto.item(row, 0).text()
        nombre_producto = self.table_widget_producto.item(row, 1).text()

        # Colocar los datos en los cuadros de texto correspondientes
        self.input_id.setText(id_producto)
        self.input_nombre.setText(nombre_producto)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Admin_Inventario()
    ventana.show()
    app.exec_()
