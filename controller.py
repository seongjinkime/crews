from database.fb_manager import FBManager
from database.sql_manager import SQLManager
from model.crews import Crews
from modules.writer import Writer
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


def not_dict(data):
    return str(type(data)) != "<class 'dict'>"


class Controller(object):
    view = None
    fb_manager = None
    sql_manager = None
    crews = None
    writer = None

    def __init__(self):
        self.fb_manager = FBManager()
        self.sql_manager = SQLManager()
        self.crews = Crews(self.sql_manager)
        self.writer = Writer()
        self.crews.init_data()
        self.init_db()

    def init_db(self):
        self.fb_manager.auth_db()
        self.sql_manager.connect_db()
        self.sql_manager.init_table()
        users = self.fb_manager.get_users()
        self.sql_manager.insert_users(users)

    def set_view(self, widget):
        self.view = widget
        self.view.complete_event.connect(self.complete)
        self.view.close_event.connect(self.quit)
        self.view.check_in_event.connect(self.check_in)

    def update_crews(self, event):
        data = event.data

        if data is None:
            self.fb_manager.add_empty_crews()
            return

        if not_dict(data) or 'phones' not in data:
            return

        self.crews.update(data)
        self.view.update_data(self.crews.get_data())

    def start(self):
        self.fb_manager.register_callback_of_crews(self.update_crews)
        self.view.set_sql_manager_for_completer(self.sql_manager)
        #self.view.update_data(self.crews.get_data())
        self.view.show()

    def check_in(self, phone, name):
        self.crews.add_phone(phone, name)
        self.fb_manager.push_crew(self.crews.get_all_phones())
        self.view.clean()

    def complete(self):
        print("COMPLETE")
        phones = self.crews.get_all_phones()
        users = self.fb_manager.get_full_informations(phones)
        self.writer.create_crews_document(users)
        subprocess.call(['open', self.writer.get_file_path()])


    def quit(self):
        self.view.hide()
        self.fb_manager.close()