from RawInterfaces.WidgetApoyo.LoadingScreen import Ui_Form
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QApplication

class LoadingScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gif = QMovie("../img/polloGif.gif")
        self.gif.start()

        self.gif_loadingScreen.setMovie(self.gif)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = LoadingScreen()
    Form.show()
    sys.exit(app.exec_())