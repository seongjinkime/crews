from PyQt5 import QtCore, QtGui, QtWidgets

from .crews_ui import Ui_Crews
from .completer import Completer
from .add_user_dialog import AddUserDialog
from .messenger import Messenger

class MainWidget(QtWidgets.QWidget):

    ui = None
    phones = None
    crews_table = None
    completer = None
    messenger = None
    loading_box = None
    closed = False

    close_event = QtCore.pyqtSignal()
    complete_event = QtCore.pyqtSignal()
    check_in_event = QtCore.pyqtSignal(str, str)
    add_user_event = QtCore.pyqtSignal(dict)
    cancel_event = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Crews()

        self.ui.setupUi(self)
        self.messenger = Messenger()
        self.phones = []
        self.crews_table = self.ui.crews_table
        self.ui.address_text_edit.setReadOnly(True)
        #Set Completer
        self.completer = Completer()
        self.ui.input_line_edit.setCompleter(self.completer)
        #Signal Connect
        self.ui.complete_button.clicked.connect(self.emit_complete)
        self.ui.add_user_pushButton.clicked.connect(self.add_user)
        self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.activated.connect(self.do_check_in, QtCore.Qt.QueuedConnection)
        self.completer.activated.connect(self.ui.input_line_edit.clear, QtCore.Qt.QueuedConnection)

        #Image Set
        self.ui.complete_button.setIcon(QtGui.QIcon("src/ic_complete.png"))
        self.ui.complete_button.setIconSize(QtCore.QSize(25, 25))

        self.ui.add_user_pushButton.setIcon(QtGui.QIcon("src/ic_add_person.png"))
        self.ui.add_user_pushButton.setIconSize(QtCore.QSize(25, 25))

    def update_data(self, data):
        print("DATA ITEMS")
        print(data.items())
        for phone, info in data.items():
            if phone in self.phones:
                continue
            else:
                idx = len(self.phones)
                self.crews_table.add_row(idx, phone, info)
                self.phones.append(phone)
                self.crews_table.viewport().update()
        self.refresh_count()

    def refresh_count(self):
        self.ui.count_label.setText("{0} 명".format(len(self.phones)))

    def do_check_in(self, text):
        divider = '|'
        if divider not in text:
            return
        phone = text.split(divider)[0][:-1]
        name = text.split(divider)[1][1:]
        self.check_in_event.emit(phone, name)


    def clean(self):
        self.ui.input_line_edit.clear()

    def add_user(self):
        dialog = AddUserDialog()
        dialog.exec_()
        if dialog.info == {}:
            return

        self.add_user_event.emit(dialog.info)

    def show_user_info(self, user):
        self.ui.history_title_label.setText("탑승 기록")
        self.ui.history_list_widget.clear()
        self.ui.name_info_label.setText(user.get_name())
        self.ui.phone_info_label.setText(user.get_phone())
        self.ui.emegerncy_info_label.setText(user.get_emergency())
        self.ui.address_text_edit.setText(user.get_address())

        if user.get_sex() == 'male':
            self.ui.sex_info_label.setText("남")
        elif user.get_sex() == 'male':
            self.ui.sex_info_label.setText("여")

        if not user.get_history():
            return

        history = sorted(user.get_history())
        for date in history:
            date = date.replace("/", "-")
            self.ui.history_list_widget.addItem(date)

        self.ui.history_title_label.setText("탑승 기록 ({0}회)".format(len(history)))

    def remove_info(self, row, phone):
        self.crews_table.remove(row)
        self.phones.remove(phone)
        self.refresh_count()

    def show_loading_box(self, title):
        if self.loading_box :
            self.hide_loading_box()
        self.loading_box = self.messenger.create_loading_box(title)
        self.loading_box.show()

    def hide_loading_box(self):
        if self.loading_box is None:
            return
        self.loading_box.close()
        self.loading_box = None

    def set_sql_manager_for_completer(self, sql_manager):
        self.completer.set_sql_manager(sql_manager)

    def closeEvent(self, QCloseEvent):
        if self.closed:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
            self.close_event.emit()

    def emit_complete(self):
        self.complete_event.emit()
