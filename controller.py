from database.fb_manager import FBManager
from database.sql_manager import SQLManager
from model.crews import Crews
from modules.writer import Writer
import subprocess
import os
from PyQt5 import QtCore, QtGui, QtWidgets


def not_dict(data):
    return str(type(data)) != "<class 'dict'>"


class Controller(object):
    view = None
    fb_manager = None
    sql_manager = None
    crews = None
    writer = None
    recent_query = None

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
        self.view.add_user_event.connect(self.add_user)
        self.view.ui.crews_table.cancel_event.connect(self.cancel_abroad)
        self.view.ui.crews_table.note_edit_event.connect(self.edit_note)
        self.view.ui.crews_table.cell_click_event.connect(self.show_user_info)


    def update_crews(self, event):
        data = event.data

        if data is None:
            self.fb_manager.add_empty_crews()
            return

        if not_dict(data) or 'phones' not in data:
            return
        print("data from fb")
        print(data)
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

    def add_user(self, info):
        try:
            self.fb_manager.add_user(info)
            self.check_in(info['phone'], info['name'])
        except Exception as e:
            print(str(e))

    def cancel_abroad(self, row, phone):
        self.crews.del_phone(phone)
        self.fb_manager.push_crew(self.crews.get_all_phones())
        self.view.remove_info(row, phone)


    def edit_note(self, phone, note):
        self.crews.edit_note(phone, note)

    def show_user_info(self, phone):
        if self.recent_query == phone:
            return
        user_info = self.fb_manager.get_full_informations([phone])[0]
        self.view.show_user_info(user_info)
        self.recent_query = phone

    def complete(self):
        phones = self.crews.get_all_phones()
        users = self.fb_manager.get_full_informations(phones)
        self.writer.create_crews_document(users)
        os.system(self.writer.get_file_path())
        #subprocess.call(['open', self.writer.get_file_path()])


    def quit(self):
        self.fb_manager.close()
        self.view.hide()