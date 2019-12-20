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

    def create_loading_box(self, title):
        try:
            #Create message box
            msg_box = QtWidgets.QMessageBox()
            msg_box.setStandardButtons(QtWidgets.QMessageBox.NoButton)
            msg_box.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            #set gif
            gif_path = "src/loading_2.gif"
            gif = QtGui.QPixmap(gif_path).scaled(10, 10)
            msg_box.setIconPixmap(gif)
            icon_label = msg_box.findChild(QtWidgets.QLabel, "qt_msgboxex_icon_label")
            movie = QtGui.QMovie(gif_path)
            setattr(msg_box, 'icon_label', movie)
            icon_label.setMovie(movie)
            movie.start()

            #set center
            layout = msg_box.layout()
            print(layout)
            margin = layout.contentsMargins()
            margin.setLeft(40)
            layout.setContentsMargins(margin)

            msg_box.setWindowTitle(title)
            msg_box.setModal(False)
            return msg_box

        except Exception as e:
            print(str(e))

