# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/crews.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from .crews_table import CrewsTable

class Ui_Crews(object):
    def setupUi(self, Crews):
        Crews.setObjectName("Crews")
        Crews.resize(572, 904)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Crews)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(-1, -1, -1, 5)
        self.main_layout.setObjectName("main_layout")
        self.title_lable = QtWidgets.QLabel(Crews)
        self.title_lable.setMinimumSize(QtCore.QSize(0, 42))
        self.title_lable.setMaximumSize(QtCore.QSize(16777215, 42))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_lable.setFont(font)
        self.title_lable.setObjectName("title_lable")
        self.main_layout.addWidget(self.title_lable)
        self.input_horizontal_layout = QtWidgets.QHBoxLayout()
        self.input_horizontal_layout.setContentsMargins(5, -1, 5, -1)
        self.input_horizontal_layout.setObjectName("input_horizontal_layout")
        self.input_line_edit = QtWidgets.QLineEdit(Crews)
        self.input_line_edit.setObjectName("input_line_edit")
        self.input_horizontal_layout.addWidget(self.input_line_edit)
        self.check_in_button = QtWidgets.QPushButton(Crews)
        self.check_in_button.setObjectName("check_in_button")
        self.input_horizontal_layout.addWidget(self.check_in_button)
        self.main_layout.addLayout(self.input_horizontal_layout)
        self.table_vertical_layout = QtWidgets.QVBoxLayout()
        self.table_vertical_layout.setContentsMargins(5, 5, 5, 5)
        self.table_vertical_layout.setObjectName("table_vertical_layout")
        self.crews_table = CrewsTable()
        self.crews_table.setObjectName("crews_table")
        self.table_vertical_layout.addWidget(self.crews_table)
        self.main_layout.addLayout(self.table_vertical_layout)
        self.bottom_horizontal_layout = QtWidgets.QHBoxLayout()
        self.bottom_horizontal_layout.setObjectName("bottom_horizontal_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_horizontal_layout.addItem(spacerItem)
        self.complete_button = QtWidgets.QPushButton(Crews)
        self.complete_button.setMinimumSize(QtCore.QSize(150, 50))
        self.complete_button.setMaximumSize(QtCore.QSize(150, 50))
        self.complete_button.setObjectName("complete_button")
        self.bottom_horizontal_layout.addWidget(self.complete_button)
        self.main_layout.addLayout(self.bottom_horizontal_layout)
        self.verticalLayout_2.addLayout(self.main_layout)

        self.retranslateUi(Crews)
        QtCore.QMetaObject.connectSlotsByName(Crews)

    def retranslateUi(self, Crews):
        _translate = QtCore.QCoreApplication.translate
        Crews.setWindowTitle(_translate("Crews", "Crews"))
        self.title_lable.setText(_translate("Crews", "  Crews"))
        self.check_in_button.setText(_translate("Crews", " Check In"))
        self.complete_button.setText(_translate("Crews", "작성 완료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crews = QtWidgets.QWidget()
    ui = Ui_Crews()
    ui.setupUi(Crews)
    Crews.show()
    sys.exit(app.exec_())
