import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from model.user import User
from PyQt5 import QtCore, QtWidgets

class FBManager(QtCore.QObject):

    registration = None
    date = "2019/12/07"
    queried = QtCore.pyqtSignal(list)
    closed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        print("FB Manager init")

    def auth_db(self):
        print("Auth Realtime Database")
        cred = credentials.Certificate("database/serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://fishingmanager-4f88b.firebaseio.com'
        })


    def get_users(self):
        return db.reference("users").get()

    def register_callback_of_crews(self, func):
        self.registration = db.reference("crews/{0}".format(self.date)).listen(func)

    def add_empty_crews(self):
        empty = {'date' : '2019/12/08', 'phones' : [], 'total' : 0}
        db.reference("crews/{0}".format(self.date)).update(empty)

    @QtCore.pyqtSlot(list)
    def get_full_informations(self, phones):
        users = []
        for p in phones:
            data = db.reference("users/{0}".format(p)).get()
            user = User()
            user.parse_data_using_dict(data)
            users.append(user)
        self.moveToThread(QtWidgets.QApplication.instance().thread())
        self.queried.emit(users)
        return users

    def push_crew(self, phones):
        path = "crews/{0}/".format(self.date)
        db.reference(path).update({'phones' : phones, 'total' : len(phones)})

    def add_user(self, info):
        path = "users/{0}".format(info['phone'])
        info['history'] = []
        info['visitCount'] = 0
        db.reference(path).update(info)

    @QtCore.pyqtSlot()
    def close(self):
        print("Closing...")
        try:
            self.registration.close()
            self.closed.emit()
            print("closed")
        except Exception as e:
            print(str(e))
