from PyQt5 import QtCore, QtGui, QtWidgets
from .crews_ui import Ui_Crews
from .completer import Completer

class MainWidget(QtWidgets.QWidget):

    ui = None
    phones = None
    crews_table = None
    completer = None
    close_event = QtCore.pyqtSignal()
    complete_event = QtCore.pyqtSignal()
    check_in_event = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Crews()
        self.ui.setupUi(self)
        self.phones = []
        self.crews_table = self.ui.crews_table
        self.completer = Completer()
        self.ui.input_line_edit.setCompleter(self.completer)
        self.ui.complete_button.clicked.connect(self.emit_complete)
        self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.activated.connect(self.do_check_in, QtCore.Qt.QueuedConnection)
        self.completer.activated.connect(self.ui.input_line_edit.clear, QtCore.Qt.QueuedConnection)

        #self.ui.input_line_edit.returnPressed.connect(self.check_in)

    def update_data(self, data):
        print(data)
        for phone, info in data.items():
            if phone in self.phones:
                continue
            else:
                idx = len(self.phones)
                self.crews_table.add_row(idx, phone, info)
                self.phones.append(phone)
                self.crews_table.viewport().update()

    def do_check_in(self, text):
        divider = '|'
        if divider not in text:
            return
        phone = text.split(divider)[0][:-1]
        name = text.split(divider)[1][1:]
        self.check_in_event.emit(phone, name)

    def clean(self):
        self.ui.input_line_edit.clear()



    def set_sql_manager_for_completer(self, sql_manager):
        self.completer.set_sql_manager(sql_manager)

    def closeEvent(self, QCloseEvent):
        self.close_event.emit()

    def emit_complete(self):
        self.complete_event.emit()
