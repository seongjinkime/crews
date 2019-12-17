import os, shutil
import openpyxl

class Writer(object):
    template = "documents/template.xlsx"
    excel_path = None
    excel_file = None
    sheet = None
    row = 5

    def __init__(self):
        self.excel_path = "documents/2019_12_07_crews.xlsx"

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


    def create_crews_document(self, users):
        print("Do writing document")

        self.open_excel()
        self.sheet = self.excel_file.get_sheet_by_name('crews')

        for user in users:
            self.write_row(user)

        self.excel_file.save(self.excel_path)
        print("DONE")

    def get_file_path(self):
        return self.excel_path

