# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crews.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from .crews_table import CrewsTable


class Ui_Crews(object):
    def setupUi(self, Crews):
        Crews.setObjectName("Crews")
        Crews.resize(729, 876)
        Crews.setStyleSheet("QWidget{\n"
"    background: rgb(248, 249, 253);\n"
"\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Crews)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_horizontal_layout = QtWidgets.QHBoxLayout()
        self.title_horizontal_layout.setObjectName("title_horizontal_layout")
        self.title_lable = QtWidgets.QLabel(Crews)
        self.title_lable.setMinimumSize(QtCore.QSize(0, 50))
        self.title_lable.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_lable.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title_lable.setFont(font)
        self.title_lable.setStyleSheet("QLabel{\n"
"    color : rgb(70, 70, 70);\n"
"\n"
"}")
        self.title_lable.setObjectName("title_lable")
        self.title_horizontal_layout.addWidget(self.title_lable)
        self.verticalLayout_2.addLayout(self.title_horizontal_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.date_info_horizontal_layout = QtWidgets.QHBoxLayout()
        self.date_info_horizontal_layout.setObjectName("date_info_horizontal_layout")
        self.count_title_label = QtWidgets.QLabel(Crews)
        self.count_title_label.setMinimumSize(QtCore.QSize(60, 0))
        self.count_title_label.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.count_title_label.setFont(font)
        self.count_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(47,127,247);\n"
"}")
        self.count_title_label.setObjectName("count_title_label")
        self.date_info_horizontal_layout.addWidget(self.count_title_label)
        self.count_label = QtWidgets.QLabel(Crews)
        self.count_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.count_label.setObjectName("count_label")
        self.date_info_horizontal_layout.addWidget(self.count_label)
        self.date_title_label = QtWidgets.QLabel(Crews)
        self.date_title_label.setMinimumSize(QtCore.QSize(0, 30))
        self.date_title_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.date_title_label.setFont(font)
        self.date_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(47,127,247);\n"
"}")
        self.date_title_label.setObjectName("date_title_label")
        self.date_info_horizontal_layout.addWidget(self.date_title_label)
        self.date_label = QtWidgets.QLabel(Crews)
        self.date_label.setObjectName("date_label")
        self.date_info_horizontal_layout.addWidget(self.date_label)
        self.verticalLayout_6.addLayout(self.date_info_horizontal_layout)
        self.input_horizontal_layout = QtWidgets.QHBoxLayout()
        self.input_horizontal_layout.setContentsMargins(0, -1, 0, -1)
        self.input_horizontal_layout.setObjectName("input_horizontal_layout")
        self.input_line_edit = QtWidgets.QLineEdit(Crews)
        self.input_line_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.input_line_edit.setStyleSheet("QLineEdit{\n"
"    background : white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgba(47, 127, 247, 128);\n"
"}")
        self.input_line_edit.setObjectName("input_line_edit")
        self.input_horizontal_layout.addWidget(self.input_line_edit)
        self.verticalLayout_6.addLayout(self.input_horizontal_layout)
        self.crews_table = CrewsTable(Crews)
        self.crews_table.setMinimumSize(QtCore.QSize(450, 600))
        self.crews_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.crews_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.crews_table.setFont(font)
        self.crews_table.setStyleSheet("QTableWidget{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.crews_table.setObjectName("crews_table")

        self.verticalLayout_6.addWidget(self.crews_table)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.info_title_label = QtWidgets.QLabel(Crews)
        self.info_title_label.setMinimumSize(QtCore.QSize(0, 65))
        self.info_title_label.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.info_title_label.setFont(font)
        self.info_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(47,127,247);\n"
"}")
        self.info_title_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.info_title_label.setObjectName("info_title_label")
        self.verticalLayout_5.addWidget(self.info_title_label)
        self.into_horizontal_layout = QtWidgets.QHBoxLayout()
        self.into_horizontal_layout.setObjectName("into_horizontal_layout")
        self.info_left_vertical_layout = QtWidgets.QVBoxLayout()
        self.info_left_vertical_layout.setObjectName("info_left_vertical_layout")
        self.name_title_label = QtWidgets.QLabel(Crews)
        self.name_title_label.setMinimumSize(QtCore.QSize(75, 0))
        self.name_title_label.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.name_title_label.setFont(font)
        self.name_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.name_title_label.setObjectName("name_title_label")
        self.info_left_vertical_layout.addWidget(self.name_title_label)
        self.sex_title_label = QtWidgets.QLabel(Crews)
        self.sex_title_label.setMinimumSize(QtCore.QSize(75, 0))
        self.sex_title_label.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.sex_title_label.setFont(font)
        self.sex_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.sex_title_label.setObjectName("sex_title_label")
        self.info_left_vertical_layout.addWidget(self.sex_title_label)
        self.phone_title_label = QtWidgets.QLabel(Crews)
        self.phone_title_label.setMinimumSize(QtCore.QSize(75, 0))
        self.phone_title_label.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.phone_title_label.setFont(font)
        self.phone_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.phone_title_label.setObjectName("phone_title_label")
        self.info_left_vertical_layout.addWidget(self.phone_title_label)
        self.emergency_title_label = QtWidgets.QLabel(Crews)
        self.emergency_title_label.setMinimumSize(QtCore.QSize(75, 0))
        self.emergency_title_label.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.emergency_title_label.setFont(font)
        self.emergency_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(90, 90, 90);\n"
"}")
        self.emergency_title_label.setObjectName("emergency_title_label")
        self.info_left_vertical_layout.addWidget(self.emergency_title_label)
        self.into_horizontal_layout.addLayout(self.info_left_vertical_layout)
        self.info_right_vertical_layout = QtWidgets.QVBoxLayout()
        self.info_right_vertical_layout.setObjectName("info_right_vertical_layout")
        self.name_info_label = QtWidgets.QLabel(Crews)
        self.name_info_label.setMinimumSize(QtCore.QSize(150, 30))
        self.name_info_label.setMaximumSize(QtCore.QSize(16777205, 30))
        self.name_info_label.setText("")
        self.name_info_label.setObjectName("name_info_label")
        self.info_right_vertical_layout.addWidget(self.name_info_label)
        self.sex_info_label = QtWidgets.QLabel(Crews)
        self.sex_info_label.setMinimumSize(QtCore.QSize(150, 30))
        self.sex_info_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sex_info_label.setText("")
        self.sex_info_label.setObjectName("sex_info_label")
        self.info_right_vertical_layout.addWidget(self.sex_info_label)
        self.phone_info_label = QtWidgets.QLabel(Crews)
        self.phone_info_label.setMinimumSize(QtCore.QSize(150, 30))
        self.phone_info_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.phone_info_label.setText("")
        self.phone_info_label.setObjectName("phone_info_label")
        self.info_right_vertical_layout.addWidget(self.phone_info_label)
        self.emegerncy_info_label = QtWidgets.QLabel(Crews)
        self.emegerncy_info_label.setMinimumSize(QtCore.QSize(150, 30))
        self.emegerncy_info_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.emegerncy_info_label.setText("")
        self.emegerncy_info_label.setObjectName("emegerncy_info_label")
        self.info_right_vertical_layout.addWidget(self.emegerncy_info_label)
        self.into_horizontal_layout.addLayout(self.info_right_vertical_layout)
        self.verticalLayout_5.addLayout(self.into_horizontal_layout)
        self.address_title_label = QtWidgets.QLabel(Crews)
        self.address_title_label.setMinimumSize(QtCore.QSize(0, 20))
        self.address_title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.address_title_label.setFont(font)
        self.address_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(47,127,247);\n"
"}")
        self.address_title_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.address_title_label.setObjectName("address_title_label")
        self.verticalLayout_5.addWidget(self.address_title_label)
        self.address_text_edit = QtWidgets.QTextEdit(Crews)
        self.address_text_edit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.address_text_edit.setStyleSheet("QTextEdit{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}\n"
"")
        self.address_text_edit.setReadOnly(True)
        self.address_text_edit.setObjectName("address_text_edit")
        self.verticalLayout_5.addWidget(self.address_text_edit)
        self.history_title_label = QtWidgets.QLabel(Crews)
        self.history_title_label.setMinimumSize(QtCore.QSize(220, 30))
        self.history_title_label.setMaximumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.history_title_label.setFont(font)
        self.history_title_label.setStyleSheet("QLabel{\n"
"    color : rgb(47,127,247);\n"
"}")
        self.history_title_label.setObjectName("history_title_label")
        self.verticalLayout_5.addWidget(self.history_title_label)
        self.history_list_widget = QtWidgets.QListWidget(Crews)
        self.history_list_widget.setMinimumSize(QtCore.QSize(0, 250))
        self.history_list_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.history_list_widget.setStyleSheet("QListView{\n"
"    background: white;\n"
"    border-style:solid;\n"
"    border-width:0.5px;\n"
"    border-radius : 5px;\n"
"    border-color: rgb(213, 213, 213);\n"
"}")
        self.history_list_widget.setObjectName("history_list_widget")
        self.verticalLayout_5.addWidget(self.history_list_widget)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.bottom_horizontal_layout = QtWidgets.QHBoxLayout()
        self.bottom_horizontal_layout.setObjectName("bottom_horizontal_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_horizontal_layout.addItem(spacerItem)
        self.add_user_pushButton = QtWidgets.QPushButton(Crews)
        self.add_user_pushButton.setMinimumSize(QtCore.QSize(120, 40))
        self.add_user_pushButton.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_user_pushButton.setFont(font)
        self.add_user_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(157, 157, 157);\n"
"    border-radius:3px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(180, 180, 180);\n"
"}")
        self.add_user_pushButton.setObjectName("add_user_pushButton")
        self.bottom_horizontal_layout.addWidget(self.add_user_pushButton)
        self.complete_button = QtWidgets.QPushButton(Crews)
        self.complete_button.setMinimumSize(QtCore.QSize(120, 40))
        self.complete_button.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.complete_button.setFont(font)
        self.complete_button.setStyleSheet("QPushButton{\n"
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
        self.complete_button.setObjectName("complete_button")
        self.bottom_horizontal_layout.addWidget(self.complete_button)
        self.verticalLayout_2.addLayout(self.bottom_horizontal_layout)

        self.retranslateUi(Crews)
        QtCore.QMetaObject.connectSlotsByName(Crews)

    def retranslateUi(self, Crews):
        _translate = QtCore.QCoreApplication.translate
        Crews.setWindowTitle(_translate("Crews", "Crews"))
        self.title_lable.setText(_translate("Crews", "승선명부"))
        self.count_title_label.setText(_translate("Crews", "탑승 인원"))
        self.count_label.setText(_translate("Crews", "TextLabel"))
        self.date_title_label.setText(_translate("Crews", "출항 일"))
        self.date_label.setText(_translate("Crews", "2019.12.20"))
        self.input_line_edit.setPlaceholderText(_translate("Crews", "전화번호 혹은 이름을 입력하세요 "))
        self.info_title_label.setText(_translate("Crews", "손님 정보"))
        self.name_title_label.setText(_translate("Crews", "이름"))
        self.sex_title_label.setText(_translate("Crews", "성별"))
        self.phone_title_label.setText(_translate("Crews", "전화번호"))
        self.emergency_title_label.setText(_translate("Crews", "비상 연락망"))
        self.address_title_label.setText(_translate("Crews", "주소"))
        self.history_title_label.setText(_translate("Crews", "탑승 기록 "))
        self.add_user_pushButton.setText(_translate("Crews", "새 손님"))
        self.complete_button.setText(_translate("Crews", "작성 완료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crews = QtWidgets.QWidget()
    ui = Ui_Crews()
    ui.setupUi(Crews)
    Crews.show()
    sys.exit(app.exec_())
