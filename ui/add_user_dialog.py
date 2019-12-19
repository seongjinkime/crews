from PyQt5 import QtCore, QtGui, QtWidgets
from .add_user_dialog_ui import Ui_AddUserDialog
from .messenger import Messenger

class AddUserDialog(QtWidgets.QDialog):

    ui = None
    info = None
    messenger = None
    info_list = [('name', "이름"),
                 ('registration', "주민등록번호"),
                 ('phone', "전화번호"),
                 ('emergency', "비상연락망"),
                 ('address', "주소")]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddUserDialog()
        self.ui.setupUi(self)
        self.info = {}
        self.ui.registration_line_edit.setInputMask("000000-0000000")
        self.ui.phone_line_edit.setInputMask("000-0000-0000")
        self.ui.emergency_line_edit.setInputMask("000-0000-0000")
        self.ui.male_radio_button.toggle()
        self.ui.register_button.clicked.connect(self.close_with_info)
        self.messenger = Messenger()

    def validate(self):
        for key, title in self.info_list:
            if self.info[key] == "" or len(self.info[key]) < 3:
                self.messenger.show_msg("입력 실패", "{0}을 입력해주세요".format(title), Messenger.Warning)
                print("Please input {0}".format(key))
                self.info = {}
                return False

        if self.info['phone'] == self.info['emergency']:
            self.messenger.show_msg("입력 실패", "전화번호와 비상연락망이 동일합니다", Messenger.Warning)
            print("Phone and emergency is same")
            self.info = {}
            return False

        return True


    def set_info(self):
        if self.ui.male_radio_button.isChecked():
            self.info['sex'] = 'male'
        elif self.ui.male_radio_button.isChecked():
            self.info['sex'] = 'female'

        self.info['name'] = str(self.ui.name_line_edit.text())
        self.info['registration'] = str(self.ui.registration_line_edit.text())
        self.info['phone'] = str(self.ui.phone_line_edit.text())
        self.info['emergency'] = str(self.ui.emergency_line_edit.text())
        self.info['address'] = str(self.ui.address_text_edit.toPlainText())

    def close_with_info(self):
        self.set_info()
        if self.validate():
            self.close()