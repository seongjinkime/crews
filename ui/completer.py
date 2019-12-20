from PyQt5 import QtCore, QtGui, QtWidgets

class Completer(QtWidgets.QCompleter):

    sql_manager = None

    def __init__(self):
        super().__init__()

    def splitPath(self, text):
        matched_list = self.sql_manager.get_matched_user(text)
        self.setModel(QtCore.QStringListModel(matched_list))
        return [text]

    def set_sql_manager(self, sql_manager):
        self.sql_manager = sql_manager