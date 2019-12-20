# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_user_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddUserDialog(object):
    def setupUi(self, AddUserDialog):
        AddUserDialog.setObjectName("AddUserDialog")
        AddUserDialog.resize(361, 638)
        AddUserDialog.setStyleSheet("QDialog{\n"
"    background: rgb(248, 249, 253);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddUserDialog)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_vertical_layout = QtWidgets.QVBoxLayout()
        self.main_vertical_layout.setObjectName("main_vertical_layout")
        self.title_label = QtWidgets.QLabel(AddUserDialog)
        self.title_label.setMinimumSize(QtCore.QSize(0, 30))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.title_label.setObjectName("title_label")
        self.main_vertical_layout.addWidget(self.title_label)
        self.sex_title_label = QtWidgets.QLabel(AddUserDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sex_title_label.setFont(font)
        self.sex_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.sex_title_label.setObjectName("sex_title_label")
        self.main_vertical_layout.addWidget(self.sex_title_label)
        self.sex_horizontal_layout = QtWidgets.QHBoxLayout()
        self.sex_horizontal_layout.setObjectName("sex_horizontal_layout")
        self.male_radio_button = QtWidgets.QRadioButton(AddUserDialog)
        self.male_radio_button.setObjectName("male_radio_button")
        self.sex_horizontal_layout.addWidget(self.male_radio_button)
        self.female_radio_button = QtWidgets.QRadioButton(AddUserDialog)
        self.female_radio_button.setObjectName("female_radio_button")
        self.sex_horizontal_layout.addWidget(self.female_radio_button)
        self.main_vertical_layout.addLayout(self.sex_horizontal_layout)
        self.name_title_label = QtWidgets.QLabel(AddUserDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.name_title_label.setFont(font)
        self.name_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.name_title_label.setObjectName("name_title_label")
        self.main_vertical_layout.addWidget(self.name_title_label)
        self.name_line_edit = QtWidgets.QLineEdit(AddUserDialog)
        self.name_line_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.name_line_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.name_line_edit.setStyleSheet("QLineEdit{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.name_line_edit.setObjectName("name_line_edit")
        self.main_vertical_layout.addWidget(self.name_line_edit)
        self.registration_title_label = QtWidgets.QLabel(AddUserDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.registration_title_label.setFont(font)
        self.registration_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.registration_title_label.setObjectName("registration_title_label")
        self.main_vertical_layout.addWidget(self.registration_title_label)
        self.registration_line_edit = QtWidgets.QLineEdit(AddUserDialog)
        self.registration_line_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.registration_line_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.registration_line_edit.setStyleSheet("QLineEdit{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.registration_line_edit.setObjectName("registration_line_edit")
        self.main_vertical_layout.addWidget(self.registration_line_edit)
        self.phone_title_label = QtWidgets.QLabel(AddUserDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.phone_title_label.setFont(font)
        self.phone_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.phone_title_label.setObjectName("phone_title_label")
        self.main_vertical_layout.addWidget(self.phone_title_label)
        self.phone_line_edit = QtWidgets.QLineEdit(AddUserDialog)
        self.phone_line_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.phone_line_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.phone_line_edit.setStyleSheet("QLineEdit{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.phone_line_edit.setObjectName("phone_line_edit")
        self.main_vertical_layout.addWidget(self.phone_line_edit)
        self.emergency_title_label = QtWidgets.QLabel(AddUserDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.emergency_title_label.setFont(font)
        self.emergency_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.emergency_title_label.setObjectName("emergency_title_label")
        self.main_vertical_layout.addWidget(self.emergency_title_label)
        self.emergency_line_edit = QtWidgets.QLineEdit(AddUserDialog)
        self.emergency_line_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.emergency_line_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.emergency_line_edit.setStyleSheet("QLineEdit{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.emergency_line_edit.setInputMask("")
        self.emergency_line_edit.setObjectName("emergency_line_edit")
        self.main_vertical_layout.addWidget(self.emergency_line_edit)
        self.address_title_label = QtWidgets.QLabel(AddUserDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.address_title_label.setFont(font)
        self.address_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.address_title_label.setObjectName("address_title_label")
        self.main_vertical_layout.addWidget(self.address_title_label)
        self.address_text_edit = QtWidgets.QTextEdit(AddUserDialog)
        self.address_text_edit.setStyleSheet("QTextEdit{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.address_text_edit.setObjectName("address_text_edit")
        self.main_vertical_layout.addWidget(self.address_text_edit)
        self.verticalLayout_2.addLayout(self.main_vertical_layout)
        self.register_button = QtWidgets.QPushButton(AddUserDialog)
        self.register_button.setMinimumSize(QtCore.QSize(0, 35))
        self.register_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.register_button.setStyleSheet("QPushButton{\n"
"    background-color:rgba(47,127,247);\n"
"    \n"
"    border-radius:3px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(31, 84, 165);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(24, 66, 129);\n"
"}\n"
"")
        self.register_button.setObjectName("register_button")
        self.verticalLayout_2.addWidget(self.register_button)

        self.retranslateUi(AddUserDialog)
        QtCore.QMetaObject.connectSlotsByName(AddUserDialog)

    def retranslateUi(self, AddUserDialog):
        _translate = QtCore.QCoreApplication.translate
        AddUserDialog.setWindowTitle(_translate("AddUserDialog", "새 손님 등록"))
        self.title_label.setText(_translate("AddUserDialog", "새 손님 등록"))
        self.sex_title_label.setText(_translate("AddUserDialog", "성별"))
        self.male_radio_button.setText(_translate("AddUserDialog", "남"))
        self.female_radio_button.setText(_translate("AddUserDialog", "여"))
        self.name_title_label.setText(_translate("AddUserDialog", "이름"))
        self.registration_title_label.setText(_translate("AddUserDialog", "주민등록번호"))
        self.phone_title_label.setText(_translate("AddUserDialog", "전화번호"))
        self.emergency_title_label.setText(_translate("AddUserDialog", "비상 연락처"))
        self.address_title_label.setText(_translate("AddUserDialog", "주소"))
        self.register_button.setText(_translate("AddUserDialog", "등록"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUserDialog = QtWidgets.QDialog()
    ui = Ui_AddUserDialog()
    ui.setupUi(AddUserDialog)
    AddUserDialog.show()
    sys.exit(app.exec_())
