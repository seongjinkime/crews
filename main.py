from PyQt5 import QtCore, QtGui, QtWidgets
from controller import Controller
from ui.main_widget import MainWidget
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCompleter, QLineEdit
from PyQt5.QtCore import QStringListModel

# def get_data(model):
#     model.setStringList(["completion", "data", "goes", "here"])
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     edit = QLineEdit()
#     completer = QCompleter()
#     edit.setCompleter(completer)
#
#     model = QStringListModel()
#     completer.setModel(model)
#     get_data(model)
#
#     edit.show()
#     sys.exit(app.exec_())


def show_splash(app):
    import time
    img = QtGui.QPixmap("src/splash.png")
    splash = QtWidgets.QSplashScreen(img, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(img.mask())
    splash.show()
    start = time.time()
    while time.time() - start < 2:
        time.sleep(0.001)
        app.processEvents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    controller = Controller()
    controller.set_view(widget)
    show_splash(app)


    controller.start()
    sys.exit(app.exec_())


"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.item(0,0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
        self.tableWidget.cellChanged.connect(self.test)

    @pyqtSlot(int, int)
    def test(self, row, col):
        print(self.tableWidget.item(row, col).text())


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

"""