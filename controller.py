from database.fb_manager import FBManager
from database.sql_manager import SQLManager
from model.crews import Crews
from modules.writer import Writer
import subprocess
import functools
import os
from PyQt5 import QtCore, QtGui, QtWidgets


def not_dict(data):
    return str(type(data)) != "<class 'dict'>"

class Controller(QtCore.QObject):
    view = None
    fb_manager = None
    sql_manager = None
    crews = None
    writer = None
    recent_query = None

    init_finished = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.fb_manager = FBManager()
        self.fb_manager.auth_db()
        self.sql_manager = SQLManager()
        self.crews = Crews(self.sql_manager)
        self.crews.init_data()


    def init_db(self):
        self.sql_manager.connect_db()
        self.sql_manager.init_table()
        users = self.fb_manager.get_users()
        self.sql_manager.insert_users(users)
        self.moveToThread(QtWidgets.QApplication.instance().thread())
        self.init_finished.emit()


    def set_view(self, widget):
        self.view = widget
        self.view.complete_event.connect(self.complete)
        self.view.close_event.connect(self.close)
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
        self.init_thread = QtCore.QThread()
        self.init_finished.connect(self.view.hide_loading_box)
        self.moveToThread(self.init_thread)
        self.init_thread.started.connect(self.init_db)
        self.init_thread.finished.connect(self.init_thread.wait)
        self.init_thread.start()

        self.fb_manager.register_callback_of_crews(self.update_crews)
        self.view.set_sql_manager_for_completer(self.sql_manager)
        #self.view.update_data(self.crews.get_data())
        self.view.show()
        self.view.show_loading_box("시작 준비중")


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
        writer = Writer(self.fb_manager, phones)
        writer.finished.connect(self.open_file)
        writer.error.connect(self.write_error)
        writer.start()
        self.view.show_loading_box("문서 작성 중")

    def open_file(self, path):
        self.view.hide_loading_box()
        if os.path.exists(path):
            os.system(path)

    def write_error(self, msg):
        self.view.hide_loading_box()
        self.view.show_msg("파일 작성 오류", msg)

    def close(self):
        self.close_thread = QtCore.QThread()
        self.fb_manager.moveToThread(self.close_thread)
        self.fb_manager.closed.connect(self.quit)
        self.close_thread.started.connect(self.fb_manager.close)
        self.close_thread.finished.connect(self.close_thread.quit)
        self.close_thread.start()
        self.view.show_loading_box("종료중")

    def quit(self):
        self.view.hide_loading_box()
        self.view.closed = True
        self.view.close()

