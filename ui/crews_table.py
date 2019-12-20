from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from .messenger import Messenger



class CrewsTable(QtWidgets.QTableWidget):

    cancel_event = QtCore.pyqtSignal(int, str)
    note_edit_event = QtCore.pyqtSignal(str, str)
    cell_click_event = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setColumnCount(4)
        # column names
        self.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("번호"))
        self.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("전화번호"))
        self.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("이름"))
        self.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("비고"))
        # column sizes
        #self.setRowCount(20)
        self.setColumnWidth(0, 30)
        self.setColumnWidth(1, 130)
        self.setColumnWidth(2, 100)

        self.cellChanged.connect(self.note_edit)

        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)

        #Context Menu
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        cancle = QtWidgets.QAction("승선 취소", self)
        cancle.triggered.connect(self.cancle_abroad)
        self.addAction(cancle)

        self.cellClicked.connect(self.item_clicked)


    def add_row(self, idx, phone, info):
        self.insertRow(idx)
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


    def cancle_abroad(self):
        row = self.currentRow()
        phone_item = self.item(row, 1)
        name_item = self.item(row, 2)

        if phone_item is None or name_item is None:
            Messenger().show_msg("잘못된 선택", "선택된 손님이 없습니다", Messenger.Warning)
            return

        phone = phone_item.text()
        name = name_item.text()

        msg = "{0} 님의 승선을 취소 하시겠습니까?".format(name)
        ans = Messenger().show_confirm("확인", msg)

        if ans != 'OK':
            return

        self.cancel_event.emit(row, phone)

    def remove(self, row):
        self.removeRow(row)
        for row in range(self.rowCount()):
            item = self.item(row, 0)
            if item is None:
                continue
            item.setText(str(row+1))

    @pyqtSlot(int, int)
    def note_edit(self, row, col):
        if col is not 3:
            return
        phone_item = self.item(row, 1)
        if phone_item is None:
            return

        phone = phone_item.text()
        note = self.item(row, col).text()
        print("NOTE EDIT")
        print(col)

        self.note_edit_event.emit(phone, note)

    def item_clicked(self, row, col):
        phone_item = self.item(row, 1)
        if phone_item is None:
            return
        phone = phone_item.text()
        self.cell_click_event.emit(phone)
