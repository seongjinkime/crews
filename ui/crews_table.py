from PyQt5 import QtCore, QtGui, QtWidgets

class CrewsTable(QtWidgets.QTableWidget):

    def __init__(self):
        super().__init__()
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setColumnCount(4)
        # column names
        self.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("번호"))
        self.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("전화번호"))
        self.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("이름"))
        self.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("비고"))
        # column sizes
        self.setRowCount(20)
        self.setColumnWidth(0, 30)
        self.setColumnWidth(1, 130)
        self.setColumnWidth(2, 100)

        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)

    def add_row(self, idx, phone, info):
        #self.insertRow(idx)
        number = QtWidgets.QTableWidgetItem(str(idx + 1))
        number.setTextAlignment(QtCore.Qt.AlignCenter)
        number.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        phone = QtWidgets.QTableWidgetItem(phone)
        phone.setTextAlignment(QtCore.Qt.AlignCenter)
        phone.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        name = QtWidgets.QTableWidgetItem(info['name'])
        name.setTextAlignment(QtCore.Qt.AlignCenter)
        name.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        note = QtWidgets.QTableWidgetItem(info['note'])

        self.setItem(idx, 0, number)
        self.setItem(idx, 1, phone)
        self.setItem(idx, 2, name)
        self.setItem(idx, 3, note)