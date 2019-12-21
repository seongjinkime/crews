import os, shutil
import openpyxl
from PyQt5 import QtCore, QtWidgets

class Writer(QtCore.QThread):

    template = "documents/template.xlsx"
    excel_path = None
    excel_file = None
    sheet = None
    row = 5
    fb_manager = None
    phones = None
    finished = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)

    def __init__(self, fb_manager, phones):
        super().__init__()
        self.fb_manager = fb_manager
        self.phones = phones
        #self.excel_path = "documents/2019_12_07_crews.xlsx"
        self.excel_path = "C:/Users/admin/Documents/projects/crews/documents/2019_12_07_crews.xlsx"

    def __del__(self):
        self.wait()

    def run(self):
        users = self.fb_manager.get_full_informations(self.phones)
        self.create_crews_document(users)

    def open_excel(self):
        if os.path.exists(self.excel_path):
            os.remove(self.excel_path)

        shutil.copyfile(self.template, self.excel_path)
        self.excel_file = openpyxl.load_workbook(self.excel_path)

    def write_row(self, user):
        num = self.row-4
        self.sheet["A" + str(self.row)] = str(num)
        self.sheet["B" + str(self.row)] = user.get_name()
        self.sheet["C" + str(self.row)] = user.get_registration()
        self.sheet["D" + str(self.row)] = user.get_address()
        self.sheet["E" + str(self.row)] = user.get_phone()
        self.sheet["F" + str(self.row)] = user.get_emergency()
        self.sheet["G" + str(self.row)] = "선원"
        self.row += 1

    @QtCore.pyqtSlot(list)
    def create_crews_document(self, users):
        print("Do writing document")
        try:
            self.open_excel()
            self.sheet = self.excel_file.get_sheet_by_name('crews')

            for user in users:
                self.write_row(user)

            self.excel_file.save(self.excel_path)
            print("DONE")
            self.moveToThread(QtWidgets.QApplication.instance().thread())
            self.finished.emit(self.excel_path)
        except Exception as e:
            print(str(e))
            self.error.emit(str(e))

    def get_file_path(self):
        return self.excel_path

