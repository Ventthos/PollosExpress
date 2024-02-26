from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, \
    QListWidget, QListWidgetItem, QGridLayout, QHBoxLayout, QMessageBox, QCheckBox
from PyQt5.QtGui import QIcon
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
        self.lista_layout.setSpacing(10)  # Establecer espacio entre elementos
        self.main_layout.addLayout(self.lista_layout)

        # Cuadro de búsqueda y botones
        self.layout_buscar = QHBoxLayout()
        self.lista_layout.addLayout(self.layout_buscar)

        self.label_buscar = QLabel('Buscar Producto:')
        self.layout_buscar.addWidget(self.label_buscar)

        self.input_buscar = QLineEdit()
        self.layout_buscar.addWidget(self.input_buscar)

        self.btn_buscar = QPushButton('Buscar')
        self.btn_buscar.setStyleSheet("background-color: #AFEEEE;")
        self.btn_buscar.clicked.connect(self.buscar_producto)
        self.layout_buscar.addWidget(self.btn_buscar)

        self.btn_actualizar = QPushButton('Actualizar')
        self.btn_actualizar.setStyleSheet("background-color: #AFEEEE;")
        self.btn_actualizar.clicked.connect(self.actualizar_lista)
        self.layout_buscar.addWidget(self.btn_actualizar)

        # Lista de productos
        self.lista_productos = QListWidget()
        self.lista_layout.addWidget(self.lista_productos)

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
        self.input_unidad.setText('--')  # Establecer el texto predeterminado
        self.input_layout.addWidget(self.label_unidad)
        self.input_layout.addWidget(self.input_unidad)

        self.label_cantidad = QLabel('Cantidad:')
        self.input_cantidad = QLineEdit()
        self.input_layout.addWidget(self.label_cantidad)
        self.input_layout.addWidget(self.input_cantidad)

        # Label y Checkbox para Estado
        self.label_estado = QLabel('Estado (0 o 1):')
        self.input_layout.addWidget(self.label_estado)
        self.checkbox_estado = QCheckBox()
        self.input_layout.addWidget(self.checkbox_estado)

        # Agregar un espacio entre los botones de editar y guardar
        self.input_layout.addSpacing(10)

        # Agregar botón de editar a la izquierda del botón de guardar
        self.btn_editar = QPushButton('Editar')
        #self.btn_editar.clicked.connect(self.activar_edicion)
        self.input_layout.addWidget(self.btn_editar)

        self.btn_guardar = QPushButton('Guardar')
        self.btn_guardar.clicked.connect(self.guardar_datos)
        self.input_layout.addWidget(self.btn_guardar)

        # Botón para eliminar producto
        self.btn_eliminar = QPushButton('Eliminar')
        self.btn_eliminar.setStyleSheet("background-color: #c9636c;")  # Establecer color de fondo
        self.btn_eliminar.clicked.connect(self.eliminar_producto)
        self.input_layout.addWidget(self.btn_eliminar)

        # Cargar lista de productos al inicio
        self.cargar_productos()

        # Conectar la señal itemClicked de la lista de productos a la función cargar_datos_producto_seleccionado
        self.lista_productos.itemClicked.connect(self.cargar_datos_producto_seleccionado)

    def cargar_productos(self):
        cursor = self.__conection.cursor()
        query = "SELECT nombre_producto FROM inventario"
        cursor.execute(query)
        productos = cursor.fetchall()
        
        if not productos:
            QMessageBox.information(self, 'Información', 'No hay registros en la base de datos.')
            return
    
        for producto in productos:
            self.lista_productos.addItem(producto[0])
        cursor.close()

    def cargar_datos_producto_seleccionado(self, item):
        # Obtener el nombre del producto seleccionado
        nombre_producto_seleccionado = item.text()

        # Realizar una consulta a la base de datos para obtener los detalles del producto
        cursor = self.__conection.cursor()
        query = "SELECT id_producto, nombre_producto, unidad, cantidad, estado FROM inventario WHERE nombre_producto = %s"
        cursor.execute(query, (nombre_producto_seleccionado,))
        producto = cursor.fetchone()
        cursor.close()

        # Verificar si se encontró el producto
        if producto:
            # Mostrar los datos del producto en los cuadros de texto
            self.input_id.setText(str(producto[0]))
            self.input_nombre.setText(producto[1])
            self.input_unidad.setText(producto[2])
            self.input_cantidad.setText(str(producto[3]))
            # Establecer el estado del checkbox
            if producto[4] == 1:
                self.checkbox_estado.setChecked(True)
            else:
                self.checkbox_estado.setChecked(False)
        else:
            # Limpiar los cuadros de texto si no se encontró el producto
            self.input_id.clear()
            self.input_nombre.clear()
            self.input_unidad.setText("--")
            self.input_cantidad.clear()
            self.checkbox_estado.setChecked(False)

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
        self.input_cantidad.clear()
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
            self.input_cantidad.clear()
            self.checkbox_estado.setChecked(False)

            # Actualizar la lista de productos
            QMessageBox.information(self, 'Información', f'El producto con ID {id_producto} ha sido eliminado correctamente.')
            self.actualizar_lista()

        else:
            QMessageBox.information(self, 'Información', 'La eliminación ha sido cancelada.')

    def buscar_producto(self):
        # Obtener el texto del cuadro de búsqueda
        texto_busqueda = self.input_buscar.text()

        # Realizar la búsqueda en la base de datos
        cursor = self.__conection.cursor()
        query = "SELECT nombre_producto FROM inventario WHERE nombre_producto LIKE %s"
        data = ("%" + texto_busqueda + "%",)
        cursor.execute(query, data)
        productos = cursor.fetchall()

        # Limpiar la lista actual
        self.lista_productos.clear()

        # Si no se encontraron productos, mostrar una advertencia
        if not productos:
            QMessageBox.warning(self, 'Advertencia', 'El producto no se encuentra en la base de datos')
        else:
            # Agregar los productos encontrados a la lista
            for producto in productos:
                self.lista_productos.addItem(producto[0])

        cursor.close()

    def actualizar_lista(self):
        # Limpiar la lista actual
        self.lista_productos.clear()
        # Recargar la lista de productos
        self.cargar_productos()
        # Mensaje de los datos actualizados
        QMessageBox.information(self, 'Información', 'Los datos han sido actualizados. \nFecha: {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))
        # Limpiamos la barra de búsqueda
        self.input_buscar.clear()

    def producto_existe(self, id_producto):
        cursor = self.__conection.cursor()
        query = "SELECT id_producto FROM producto WHERE id_producto = %s"
        cursor.execute(query, (id_producto,))
        producto = cursor.fetchone()
        cursor.close()
        return producto is not None
    
if __name__ == '__main__':
    app = QApplication([])
    ventana = Admin_Inventario()
    ventana.show()
    app.exec_()
