from PyQt5 import QtCore, QtGui, QtWidgets
from controller import Controller
from ui.main_widget import MainWidget

def show_splash(app):
    img = QtGui.QPixmap("src/splash_test.png")
    splash = QtWidgets.QSplashScreen(img, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(img.mask())
    splash.show()
    app.processEvents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_splash(app)
    controller = Controller()
    widget = MainWidget()
    controller.set_view(widget)
    controller.start()
    sys.exit(app.exec_())
