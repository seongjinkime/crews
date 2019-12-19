from PyQt5 import QtCore, QtGui, QtWidgets

class Messenger(QtCore.QObject):

    Question = 0
    Information = 1
    Warning = 2
    Critical = 3

    def show_msg(self, title, msg, msg_type):
        msg_box = QtWidgets.QMessageBox()
        if msg_type == self.Question:
            msg_box.setIcon(QtWidgets.QMessageBox.Question)
        elif msg_type == self.Information:
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
        elif msg_type == self.Warning:
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        elif msg_type == self.Critical:
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)

        msg_box.setWindowTitle(title)
        msg_box.setText(title)
        msg_box.setInformativeText(msg)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.show()
        msg_box.exec_()

    def show_confirm(self, title, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(title)
        msg_box.setWindowTitle(title)
        msg_box.setInformativeText(msg)
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        msg_box.show()
        msg_box.exec_()
        return msg_box.clickedButton().text()
