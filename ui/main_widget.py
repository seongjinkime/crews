from PyQt5 import QtCore, QtGui, QtWidgets
from .crews_ui import Ui_Crews

class MainWidget(QtWidgets.QWidget):

    ui = None
    phones = None
    crews_table = None
    close_event = QtCore.pyqtSignal()
    complete_event = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Crews()
        self.ui.setupUi(self)
        self.phones = []
        self.crews_table = self.ui.crews_table
        self.ui.complete_button.clicked.connect(self.emit_complete)


    def update_data(self, data):
        print(data)
        for phone, info in data.items():
            print("Phone IN: " + phone)
            print("EXIST: " + phone in self.phones)
            print(self.phones)
            #print("Phone IN: " + phone)
            if phone in self.phones:
                continue
            else:
                idx = len(self.phones)
                print (idx)
                self.crews_table.add_row(idx, phone, info)
                self.phones.append(phone)
                self.crews_table.viewport().update()


    def closeEvent(self, QCloseEvent):
        self.close_event.emit()

    def emit_complete(self):
        self.complete_event.emit()
